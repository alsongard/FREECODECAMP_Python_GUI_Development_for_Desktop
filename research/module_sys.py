import sys
print(sys.version) # get the current version of python running on your machine




print(f"PythonScript FileName: {sys.argv[0]} ")
print(f"Lenght of sys.argv is {len(sys.argv)}")
if len(sys.argv) >= 2:
    print(f"Checking for any other arguments: {sys.argv[1]}")


# terminate a script use sys.exit()

if len(sys.argv) >= 3:
    print("Too many arguments given")
    sys.exit(1)

print("sys.path is a list of file paths in which python searches for modules")
print(f"Python Search File Paths: ${sys.path} ") # sys.path is a list of file paths in which python searches for modules
for item in sys.path:
    print(item)