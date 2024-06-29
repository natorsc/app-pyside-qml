import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: root

    property color systemTextColor: systemPalette.text

    height: Screen.height / 2
    minimumHeight: Screen.height / 3
    minimumWidth: Screen.height / 3
    title: qsTr('Python - PySide6 - Qt')
    visible: true
    width: Screen.width / 2
    x: 40
    y: 50

    menuBar: MenuBar {
        Menu {
            id: mainMenu

            title: qsTr('Arquivo')

            Action {
                id: actionExit

                icon.name: 'application-exit'
                icon.source: 'qrc:/icons/application-exit'
                shortcut: "Ctrl+q"
                text: qsTr('Sair')

                onTriggered: Qt.quit()
            }
        }
    }

    SystemPalette {
        id: systemPalette

        colorGroup: SystemPalette.Active
    }
    ColumnLayout {
        id: columnLayout

        anchors.fill: parent
        anchors.margins: 12
        spacing: 6

        Label {
            id: label

            Layout.fillHeight: true
            Layout.fillWidth: true
            // color: systemTextColor
            horizontalAlignment: Text.AlignHCenter
            text: qsTr('Este texto será alterado.')
            verticalAlignment: Text.AlignVCenter
            wrapMode: Text.WordWrap
        }
        TextField {
            id: textField

            Layout.fillWidth: true
            placeholderText: qsTr('Digite algo')
        }
        Button {
            id: buttonQML

            Layout.fillWidth: true
            text: qsTr('Clique aqui (QML)')

            onClicked: {
                var value = textField.text;
                if (value.trim().length === 0) {
                    label.text = qsTr('Digite algo no campo de texto ;).');
                } else {
                    label.text = value;
                }
            }
        }
        Button {
            id: buttonPython

            Layout.fillWidth: true
            text: qsTr('Clique aqui (Python)')

            onClicked: {
                label.text = mainwindow.on_button_python_clicked(textField.text);
            }
        }
    }
}
