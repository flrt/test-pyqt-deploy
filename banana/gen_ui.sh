#!/bin/bash
python -m PyQt5.uic.pyuic -x app.ui -o app.py
python -m PyQt5.uic.pyrcc5 resources.qrc -o resources_rc.py

# windows
# python -m PyQt5.pyrcc_main resources.qrc -o resources_rc.py