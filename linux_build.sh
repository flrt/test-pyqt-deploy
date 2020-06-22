#!/bin/bash
APP=banana
VERSION=1.0
DESTDIR=build/exe.linux-x86_64-3.8
APPDIR=build/$APP

python setup.py build
cp linux_install.sh $DESTDIR/install.sh
chmod a+x $DESTDIR/install.sh
cp $APP.desktop $DESTDIR

mv $DESTDIR $APPDIR
cd build

tar zcvf $APP-$VERSION.tar.gz $APP
