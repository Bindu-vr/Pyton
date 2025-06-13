# Read and print content of a file

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")

read_file("example.txt")
