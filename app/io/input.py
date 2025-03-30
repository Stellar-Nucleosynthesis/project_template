def console_read():
    return input()

def file_read(file_name):
    return open(file_name).read()

def pandas_read(file_name):
    import pandas as pd
    return pd.read_csv(file_name)