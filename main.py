# Returns the contents of the given file as a string
def read_file(path: str) -> str:
    with open(path, "r") as file:
        return file.read()

if __name__ == '__main__':
    read_file("data.txt")