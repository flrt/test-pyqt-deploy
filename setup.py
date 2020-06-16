import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = ["tkinter"])



# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"


executables = [
    Executable('main.py', base=base, targetName = 'banana', icon='assets/banana.ico')
]



setup(  name = "banana",
        version = "0.1",
        description = "My Banana!",
        options = {"build_exe": buildOptions},
        executables = executables)