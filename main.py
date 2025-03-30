

def main():
    import app.io.input as input
    import app.io.output as output
    str1 = input.console_read()
    str2 = input.file_read("data/read_file.txt")
    str3 = input.pandas_read("data/read_file.txt")
    output.console_write("Console input: %s" % str1)
    output.console_write("File input: %s" % str2)
    output.console_write("File input using pandas: %s" % str3)
    output.file_write("data/write_file1.txt", "Console input: %s" % str1)
    output.file_write("data/write_file2.txt", "File input: %s" % str2)
    output.file_write("data/write_file3.txt", "File input using pandas: %s" % str3)


if __name__ == '__main__':
    main()