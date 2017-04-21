import sys


class UtilConsole:

    def __init__(self, *args):
        pass

    @staticmethod
    def printCmd(line):
        sys.stdout.write(line)
        sys.stdout.flush()

    @staticmethod
    def printCmdLn(line):
        sys.stdout.write(line + '\n')
        sys.stdout.flush()
