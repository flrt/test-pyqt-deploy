import sys
import requests
import json

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

import app
import elements

#curl -X GET "https://www.data.gouv.fr/api/1/datasets/?format=xml&reuses=many&page=0&page_size=20" -H "accept: application/json"
URL = "https://www.data.gouv.fr/api/1/datasets/?format=xml&reuses=many&page=0&page_size=20"

class Ui(QtWidgets.QMainWindow, app.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)
        self.setupUi(self)
        self.model=elements.TitleModel()
        self.listView.setModel(self.model)

    def main(self):
        self.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.get_infos()

    def get_infos(self):
        req = requests.get(URL)
        titles = set()
        if req.status_code == 200:
            data = json.loads(req.text)
            for item in data["data"]:
                for res in item["resources"]:
                    titles.add(item["title"])

        self.model.titles=list(titles)
        self.model.layoutChanged.emit()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    ui.main()
    app.exec_()
