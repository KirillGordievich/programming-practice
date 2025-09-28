class MyOpen:
    def __init__(self, file_name: str):
        self._file_name = file_name
        self._file = None

    def __enter__(self):
        self._file = open(self._file_name, "r")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._file.close()

    def get_content(self):
        return self._file.read()


with MyOpen("nedra/some_file.txt") as f:
    content = f.get_content()
    print(content)
