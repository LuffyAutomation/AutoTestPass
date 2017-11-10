import os
from fwk.utils.utilIO.UtilFolder import UtilFolder

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

if __name__ == '__main__':
    UtilFolder.walk_folder(os.path.dirname(__file__), UtilFolder.DoMode.DEL_SPECIFIED, [".*.pyc", ".*.log"])
