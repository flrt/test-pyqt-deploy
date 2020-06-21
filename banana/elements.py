from PyQt5.Qt import *
from PyQt5 import QtCore


class TitleModel(QtCore.QAbstractListModel):
    def __init__(self, *args, titles=None, **kwargs):
        super(TitleModel, self).__init__(*args, **kwargs)
        self.titles = titles or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.titles[index.row()]

    def rowCount(self, index):
        return len(self.titles)
