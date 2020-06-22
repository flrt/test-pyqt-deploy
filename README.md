Test the deployment of a simple app on

- windows
- macos
- linux

Tested Tool

-pyinstaler
-cxFreeze



# cxFreeze
python setup.py build
sudo cp app.desktop /usr/share/applications/banana.desktop
sudo cp -r venv/lib/banana-1.0/ /usr/share/banana
sudo cp assets/banana.ico /usr/share/pixmaps/banana.ico


# Deploiement sur windows
./Scripts\Activate.ps1
python setup.py bdist_msi
