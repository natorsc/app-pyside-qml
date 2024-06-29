# -*- coding: utf-8 -*-
"""."""

from PySide6 import QtCore


class MainWindow(QtCore.QObject):
    def __init__(self, **kwargs):
        super().__init__()
        self.application = kwargs.get('application')

    @QtCore.Slot(str, result=str)
    def on_button_python_clicked(self, value):
        if value.split():
            return value
        else:
            return self.tr('Digite algo no campo de texto ;).')


if __name__ == '__main__':
    pass
