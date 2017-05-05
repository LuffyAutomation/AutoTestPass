import os
from fwk.base.InitFwk import InitFwk
from fwk.utils.newProjectCreator import NewProjectCreator

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

if __name__ == '__main__':
    # project is defined in env>main.conf>[DefaultProject].

    initFwk = InitFwk()

