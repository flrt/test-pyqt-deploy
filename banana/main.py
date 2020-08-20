import sys
import platform

import requests
import json
from jsonpath_ng import parse

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSlot

from banana import elements, app

# curl -X GET "https://www.data.gouv.fr/api/1/datasets/?format=xml&reuses=many&page=0&page_size=20" -H "accept: application/json"
URL = "https://www.data.gouv.fr/api/1/datasets/?format=xml&reuses=many&page=0&page_size=20"
PATH = "data.[*].title"

STYLES = {"Windows": """
QWidget   { font-family:'Segoe UI';font-size:9pt; }
QLineEdit { font-family:"DejaVu Sans Mono";font-size:9pt; }""",
          "Darwin": """
QWidget   { font-family:'Lucida Grande';font-size:12pt; }
QLineEdit { font-family:"Menlo";font-size:12pt; }""",
          "Linux": """
QWidget   { font-family:'Lucida Grande';font-size:9pt; }
QLineEdit { font-family:"Menlo";font-size:9pt; }"""}


class Ui(QtWidgets.QMainWindow, app.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)
        self.setupUi(self)
        self.url = URL
        self.path = PATH
        self.urlEdit.setText(self.url)
        self.jsonpathEdit.setText(self.path)
        self.model = elements.TitleModel()
        self.listView.setModel(self.model)
        if platform.system() in STYLES:
            self.setStyleSheet(STYLES[platform.system()])
        #self.setWindowIcon(QtGui.QIcon("img/banana.ico"))

    def main(self):
        self.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.get_infos()

    @pyqtSlot(str)
    def on_urlEdit_textChanged(self, s):
        self.url = str(self.urlEdit.text())

    @pyqtSlot(str)
    def on_jsonpathEdit_textChanged(self, s):
        self.path = str(self.jsonpathEdit.text())

    def get_infos(self):
        req = requests.get(self.url)
        titles = set()
        if req.status_code == 200:
            data = json.loads(req.text)
            [titles.add(match.value) for match in parse(self.path).find(data)]
        self.model.titles = list(titles)
        self.model.layoutChanged.emit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    ui.main()
    app.exec_()
