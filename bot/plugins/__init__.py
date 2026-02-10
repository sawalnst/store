from glob import glob
from os.path import basename, dirname, isfile

def load_plugins():
    files = glob(f"{dirname(__file__)}/*.py")
    return [basename(f)[:-3] for f in files if isfile(f) and not f.endswith("__init__.py")]

PLUGINS = load_plugins()
