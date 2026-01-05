class FileHandling:
    def __init__(self,filename:str, mode='r'):
        self.filename = filename
        self.mode=mode

    def __enter__(self):
        self.file = open(self.filename, mode=self.mode)
        print(f"File {self.filename} is opened.")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

        print(f"Exception class raised is {exc_type}")
        print(f"Exception value is {exc_val}")
        print(f"Exception traceback is {exc_tb}")

        print(f"File {self.filename} is closed.")


if __name__ == "__main__":
    file_name = "random_file.txt"
    with FileHandling(file_name) as f:
        #data = f.read()
        a = 1/0
        print(a)
        #print(data)







