import sys
from cx_Freeze import setup, Executable

APPNAME = 'banana'
APPDESCR = 'banana test'
MAIN = 'main.py'
__version__ = '1.0'

buildOptions = dict(packages=["multiprocessing"], excludes=["tkinter"])

# On Mac OS
# python setup.py bdist_mac --iconfile=assets/banana.icns --custom-info-plist=Info.plist
# in setup , "bdist_mac":macOptions, "bdist_dmg":dmgOptions},
macOptions = {"iconfile": "assets/banana.icns", "custom_info_plist": "Info.plist"}
dmgOptions = {"volume_label": "banana", "applications_shortcut": True}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(MAIN, base=base, targetName=APPNAME, icon='assets/banana.ico')
]

setup(name=APPNAME,
      version=__version__,
      description=APPDESCR,
      packages=[APPNAME],
      options={"build_exe": buildOptions},
      executables=executables,
      entry_points={
          'console_scripts': ['banana = banana.banana:main']
      },
      data_files=[
          ('share/applications/', ['banana.desktop'])
      ],
      classifiers=[
          "License :: OSI Approved :: BSD License",
      ],
      )

# https://stackoverflow.com/questions/17401381/debianzing-a-python-program-to-get-a-deb
