#!/bin/bash
APPDIR=/usr/share/banana
echo "Install banana in $APPDIR..."

sudo mkdir $APPDIR
sudo cp banana $APPDIR/
sudo cp -r lib $APPDIR/
sudo cp banana.desktop /usr/share/applications/banana.desktop
sudo cp banana.ico /usr/share/pixmaps/banana.ico
