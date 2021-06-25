from setuptools import setup

APP = ['MoviePicker.py']
DATA_FILES = ['seen.json', 'watchlist.json']
OPTIONS = {
    'argv_emulation' : True,
}

setup(
    app = APP,
    data_files = DATA_FILES,
    options = {'py2app':OPTIONS},
    setup_requires = ['py2app']
)