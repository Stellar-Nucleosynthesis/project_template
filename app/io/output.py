def console_write(string):
    """Prints a string to the console.

    Args:
        string (str): The string to print.
    """
    print(string)


def file_write(file_name, string):
    """Writes a string to a file.

    Args:
        file_name (str): The name or path of the file.
        string (str): The content to write to the file.
    """
    with open(file_name, "w") as f:
        f.write(string)