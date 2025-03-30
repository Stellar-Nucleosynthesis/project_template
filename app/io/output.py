def console_write(string):
    print(string)

def file_write(file_name, string):
    with open(file_name, "w") as f:
        f.write(string)