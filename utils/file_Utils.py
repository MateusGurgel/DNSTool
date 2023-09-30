def getFileLines(path):
    try:
        with open(path, "r") as file:
            return file.readlines()
    except:
        raise ValueError(f"The '{path}' file could not be acessed")
