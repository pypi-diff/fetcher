def write(curSerial, serialFile):
    with open(serialFile, "w") as fh:
        fh.write(str(curSerial))

def read(serialFile):
    try:
        with open(serialFile, "r") as fh:
            return fh.read()
    except FileNotFoundError:
        return ""
