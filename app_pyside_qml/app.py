# -*- coding: utf-8 -*-
"""."""

import locale
import sys
from ctypes import windll

from PySide6 import QtCore, QtGui, QtQml, QtWidgets

try:
    import resources_rc
    from components.MainWindow import MainWindow
except ModuleNotFoundError:
    from app_pyside_qml import resources_rc
    from app_pyside_qml.components.MainWindow import MainWindow


RESOURCES_RC = resources_rc


def main() -> None:
    APPLICATION_NAME = 'br.com.justcode.Qt'
    ORGANIZATION_NAME = APPLICATION_NAME.split('.')[2]
    ORGANIZATION_DOMAIN = '.'.join(APPLICATION_NAME.split('.')[0:3])

    application = QtWidgets.QApplication(sys.argv)
    application.setOrganizationName(ORGANIZATION_NAME)
    application.setOrganizationDomain(ORGANIZATION_DOMAIN)
    application.setApplicationName(APPLICATION_NAME)
    application.setDesktopFileName(APPLICATION_NAME)
    application.setWindowIcon(QtGui.QIcon(':/icons/br.com.justcode.Qt'))

    loc, _ = locale.getlocale()
    translator = QtCore.QTranslator(application)
    if translator.load(QtCore.QLocale(loc), APPLICATION_NAME, '.', ':/i18n'):
        application.installTranslator(translator)

    if QtCore.QSysInfo.productType() == 'windows':
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            APPLICATION_NAME,
        )

    mainwindow = MainWindow(application=application)

    engine = QtQml.QQmlApplicationEngine()
    engine.rootContext().setContextProperty('mainwindow', mainwindow)
    engine.load(QtCore.QUrl('qrc:/ui/MainWindow'))

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(application.exec())


def get_engine() -> QtQml.QQmlApplicationEngine:
    engine = QtQml.QQmlApplicationEngine()
    engine.load(QtCore.QUrl('qrc:/ui/MainWindow'))

    if not engine.rootObjects():
        sys.exit(-1)
    return engine


if __name__ == '__main__':
    main()
