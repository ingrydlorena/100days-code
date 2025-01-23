class Error(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    raise Error("Something went wrong!")
except Error as erro:
    print(f"Caught an error:{erro}")
