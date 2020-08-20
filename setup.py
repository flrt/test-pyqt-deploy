import sys
from cx_Freeze import setup, Executable

APPNAME = 'banana'
APPDESCR = 'banana test'
MAIN = f'{APPNAME}/main.py'
__version__ = '1.0'

winOptions = {"upgrade-code": "44aad47f-38bd-4fcf-b70c-b0b4cf3f246b",
              "initial_target_dir": r'[ProgramFilesFolder]\%s' % APPNAME,
              "install_icon": "banana/img/banana.ico",
              "target_name": "banana"}
buildOptions = dict(packages=["multiprocessing"], excludes=["tkinter"])

# On Mac OS
# python setup.py bdist_mac --iconfile=assets/banana.icns --custom-info-plist=Info.plist
# in setup , "bdist_mac":macOptions, "bdist_dmg":dmgOptions},
macOptions = {"iconfile": f"{APPNAME}/img/banana.icns", "custom_info_plist": "Info.plist"}
dmgOptions = {"volume_label": APPNAME, "applications_shortcut": True}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(MAIN, base=base, targetName=APPNAME, icon=f'{APPNAME}/img/banana.ico')
]

if sys.platform == "win32":
    setup(name=APPNAME,
          version=__version__,
          description=APPDESCR,
          packages=[APPNAME],
          options={"build_exe": buildOptions, "sdist_msi": winOptions},
          executables=executables,
          )
elif sys.platform == "linux":
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
              ('share/applications/', [f'{APPNAME}.desktop'])
          ],
          classifiers=[
              "License :: OSI Approved :: BSD License",
          ],
          )

# https://stackoverflow.com/questions/17401381/debianzing-a-python-program-to-get-a-deb
