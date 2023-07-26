def write_file(file_name, file_content):
#writes content to a file
    with open(str(file_name) + '.txt', 'w') as f: 
        f.write(file_content)

def append_file(file_name:str, append_content:str):
#Appends content to a file
    with open(str(file_name) + '.txt', 'a') as f:
        f.write(append_content)

def read_file(file_name):
#Reads content from a file
    with open(str(file_name) + '.txt', 'r') as f:
        return f.read()

# This way, you can use these functions with any type of file, not just '.txt' files.
# def write_file(file_name, file_content):
#     Writes content to a file
#     with open(str(file_name), 'w') as f: 
#         f.write(file_content)

# def append_file(file_name, append_content):
#     Appends content to a file
#     with open(str(file_name), 'a') as f:
#         f.write(append_content)

# def read_file(file_name):
#     Reads content from a file
#     with open(str(file_name), 'r') as f:
#         return f.read()

# def write_file(file_name, file_content):: Here, we're defining a function called write_file that takes two arguments: file_name and file_content. file_name is expected to be the path to a file (including the file name), and file_content is expected to be the content you want to write to the file.

# with open(str(file_name), 'w') as f:: This line is using the built-in open function to open a file. The open function takes two arguments. The first argument is the path to the file we want to open, and the second argument is the mode in which we want to open the file. 'w' stands for "write mode", which means we intend to write to the file. This mode will overwrite the file if it already exists, or create it if it doesn't exist.

# The open function returns a file object, which we're storing in the variable f. We're using with to manage this file object because it automatically closes the file once we're done with it, even if an error occurs while we're working with the file. This is good practice and helps prevent resource leaks.

# str(file_name) is used to ensure that the file name is a string. This is important because the open function expects a string argument for the file path, but the file_name argument could be a different type, like a pathlib.Path object. By calling str(file_name), we're ensuring that we pass a string to open.

# f.write(file_content): This line is using the write method of the file object to write file_content to the file. This method takes a string and writes it to the file. In this case, we're writing the contents of the file_content argument to the file. After this line runs, the contents of file_name will be exactly what was in file_content.