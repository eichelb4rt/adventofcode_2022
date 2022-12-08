MAX_SIZE = 100000
TOTAL_SPACE = 70000000
WANTED_FREE_SPACE = 30000000

# directory name
Directory = str
# complete (not just base) filename, filesize
File = tuple[str, int]


class FileTree:
    def __init__(self):
        # directory -> contained files/directories
        self.children: dict[Directory, list[File | Directory]] = {}
        # file/directory size for every node in the tree
        self._sizes: dict[File | Directory, int] = {}

    def add_child(self, parent: Directory, child: File | Directory):
        # if the parent doesn't have children yet
        if parent not in self.children:
            self.children[parent] = []
        self.children[parent].append(child)

    def dir_sizes(self) -> dict[File | Directory, int]:
        """Calculates the size of every directory in the tree."""

        self._update_sizes("/")
        # only show directories
        return {dir: size for dir, size in self._sizes.items() if type(dir) == Directory}

    def _update_sizes(self, root: File | Directory) -> None:
        """Updates `self._sizes` for the subtree with root `root`."""

        # if it's a file, we know the size
        if type(root) == tuple:
            filename, filesize = root
            self._sizes[root] = filesize
            return
        # if it's a directory, update all its children and add the sizes
        for child in self.children[root]:
            self._update_sizes(child)
        # sum up the sizes of all the children
        self._sizes[root] = sum([self._sizes[child] for child in self.children[root]])

    def __repr__(self) -> str:
        return repr(self.children)


class TreeParser:
    def __init__(self) -> None:
        self.tree = FileTree()
        # list of directory names
        self.current_path: list[str] = []

        self.line_index: int
        self.lines: list[str]
        self.current_line: str | None

    def parse(self, lines: list[str]) -> FileTree:
        # start before the list
        self.line_index = -1
        self.lines = lines

        # now start at the actual start
        self.next_line()
        while self.current_line is not None:
            if has_command(self.current_line):
                if self.current_line[2:].startswith("cd"):
                    self.cd()
                    self.next_line()
                    continue
                if self.current_line[2:].startswith("ls"):
                    self.ls()
        return self.tree

    def next_line(self) -> None:
        self.line_index += 1
        if self.line_index >= len(self.lines):
            self.current_line = None
            return
        self.current_line = self.lines[self.line_index]

    def ls(self) -> None:
        """Reads ls output."""

        parent = self.pwd()
        # skip ls command
        self.next_line()
        while self.current_line is not None and not has_command(self.current_line):
            child: File | Directory = to_file(parent, self.current_line)
            self.tree.add_child(parent, child)
            self.next_line()

    def cd(self) -> None:
        """Changes the current directory."""

        # $ cd directory
        directory = self.current_line[5:]
        if directory == "..":
            self.current_path.pop()
        elif directory == "/":
            self.current_path = []
        else:
            self.current_path.append(directory)

    def pwd(self) -> str:
        return "/" + join_paths(*self.current_path)


def has_command(line: str) -> bool:
    return line[0] == '$'


def trim_connector(path: str) -> str:
    if path[-1] == "/":
        return path[:-1]
    return path


def join_paths(*paths: str) -> str:
    return "/".join([trim_connector(path) for path in paths])


def to_file(parent_dir: Directory, line: str) -> File | Directory:
    """Reads the file or directory from the line."""

    if line.startswith("dir"):
        # dir dirname
        base_dirname = line[4:]
        return join_paths(parent_dir, base_dirname)
    # filesize filename
    filesize, base_filename = line.split(" ")
    filename = join_paths(parent_dir, base_filename)
    return (filename, int(filesize))


def get_dir_to_delete(input_file: str) -> int:
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    parser = TreeParser()
    filetree = parser.parse(lines)
    sizes = filetree.dir_sizes()
    used_space = sizes["/"]
    free_space = TOTAL_SPACE - used_space
    space_to_be_freed = WANTED_FREE_SPACE - free_space
    relevant_sizes = [size for dir, size in sizes.items() if size >= space_to_be_freed]
    return min(relevant_sizes)


def main():
    assert get_dir_to_delete("test_input.txt") == 24933642
    answer = get_dir_to_delete("input.txt")
    print(f"The size of the deleted directory is: {answer}")


if __name__ == "__main__":
    main()
