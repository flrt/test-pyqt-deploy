## MacOS

Taille onefile = 50,9 Mb
1er demarrage - 20 sec
Temps de démarrage - 12 sec

Taille onedir =
Temps de démarrage 1ere ouverture = 11 sec
ouverture suivante 1 sec

Avec UPX
Taille onefile = 50,9 Mb
1ere ouverture 24 sec
ouverture suivante 12 sec

Taille onedir = 136,6 Mb
1ere ouverture 10 sec
ouverture suivante 1sec

## Windows
Taille onedir : 181 Mb 
Temps de démarrage : 1ere ouverture = 2 sec
ouverture suivante 1 sec

taille onefile : 54,9 mb
temps de démarrage : 5 à 7 sec


# cx_Freeze
## Macos
1 répertoire : 
temps de démarrage :
    - 1ere demarrage : entre 12 et 20 sec
    - démarrages suivants : 1 sec
    
## windows
1 répertoire : 166 mb
temps de démarrage : 1 sec


# Nuitka
Installation 
http://nuitka.net/doc/user-manual.html#windows-standalone-program-redistribuation
https://sourceforge.net/projects/mingw-w64/

repertoire 69 mb

python -m nuitka --standalone --windows-dependency-tool=pefile --plugin-enable=qt-plugins --follow-imports main.py
