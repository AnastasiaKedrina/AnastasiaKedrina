import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls
import QtQuick.Layouts 1.3

Window {
    id:win;
    property int winWidth:320
    property int winHeight:480
    width: winWidth
    height: winHeight
    minimumWidth: winWidth
    minimumHeight: winHeight
    visible: true
    title: qsTr("LogIn")

    Rectangle{
        id:background
        anchors.fill:parent
        color:"#F0F0F0"
        Rectangle{
            anchors.centerIn:parent
            width: parent.width-50
            height: parent.height-180
            color:parent.color
            ColumnLayout{
                anchors.fill:parent
                spacing: 20
                Text {
                    text: "Enter your password:"
                    font.pixelSize: 16
                    Layout.alignment: Qt.AlignCenter
                }
                Text{
                    id: passwordField
                    text: passwordField.text
                    color:background.color
                    visible: false
                }
                Rectangle {
                    id: passwordField1
                    color: "white"
                    border.width: 2
                    border.color: "black"
                    width: parent.width
                    height: 50
                    Layout.alignment: Qt.AlignCenter
                    Row {
                        spacing: 6
                        anchors.centerIn: parent
                        // Добавляем 6 элементов Label для отображения введенных символов
                        Repeater {
                            model:6
                            Label {
                                width: 20
                                height: 20
                                font.pixelSize: 36
                                text: "*"
                                Layout.alignment: Qt.AlignCenter
                                color:index <passwordField.text.length ? "black" : "light grey"
                            }
                        }
                    }
                }

                GridLayout {
                    id: keypad
                    rows: 4
                    columns: 3
                    Button {
                        text: "1"
                        onClicked: passwordField.text += "1"
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                    }
                    Button {
                        text: "2"
                        onClicked: passwordField.text+= "2"
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                    }
                    Button {
                        text: "3"
                        onClicked: passwordField.text+= "3"
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                    }
                    Button {
                        text: "4"
                        onClicked: passwordField.text+= "4"
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                    }
                    Button {
                        text: "5"
                        onClicked: passwordField.text+= "5"
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                    }
                    Button {
                        text: "6"
                        onClicked: passwordField.text+= "6"
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                    }
                    Button {
                        text: "7"
                        onClicked: passwordField.text+= "7"
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                    }
                    Button {
                        text: "8"
                        onClicked: passwordField.text+= "8"
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                    }
                    Button {
                        text: "9"
                        onClicked: passwordField.text+= "9"
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                    }
                    Button {
                        text: ""
                        onClicked: passwordField.text+= ""
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                    }
                    Button {
                        text: "0"
                        onClicked: passwordField.text+= "0"
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                    }
                    Button {
                        text: "Clear"
                        onClicked: passwordField.text= ""
                        Layout.fillHeight: true
                        Layout.fillWidth: true
                    }
                }
                Button {
                    Layout.fillWidth: true
                    text: "Log In"
                    onClicked: model.submit()
                    background: Rectangle {
                        color: parent.down ? "#bbbbbb" :
                                             (parent.hovered ? "#B5B5B5" : "#C7C7C7")
                    }

                }
            }
        }
    }
}
