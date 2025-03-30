def console_read():
    """Reads a line of input from the console.

    Returns:
        str: The input string entered by the user.
    """
    return input()

def file_read(file_name):
    """Reads the contents of a file.

    Args:
        file_name (str): The name or path of the file to read.

    Returns:
        str: The contents of the file as a string.
    """
    return open(file_name).read()

def pandas_read(file_name):
    """Reads a CSV file into a pandas DataFrame.

    Args:
        file_name (str): The name or path of the CSV file.

    Returns:
        pandas.DataFrame: The data from the CSV file as a pandas DataFrame.
    """
    import pandas as pd
    return pd.read_csv(file_name)