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
            width: parent.width - 100
            height: 150
            color:parent.color
            ColumnLayout{
                anchors.fill:parent
                TextField {
                    id: usernameField
                    Layout.fillWidth: true
                    placeholderText: "Username"
                    font.pixelSize: 16
                }
                TextField {
                    id: passwordField
                    Layout.fillWidth: true
                    placeholderText: "Password"
                    font.pixelSize: 16
                    echoMode: TextInput.Password
                }
                RowLayout {
                    Button {
                        Layout.fillWidth: true
                        text: "Log in"
                        onClicked: model.submit()
                        background: Rectangle {
                            color: parent.down ? "#bbbbbb" :
                                                 (parent.hovered ? "#d6d6d6" : "#C7C7C7")
                        }
                    }
                    Button {
                        Layout.fillWidth: true
                        text: "Clear"
                        onClicked: {usernameField.clear(); passwordField.clear()}
                        background: Rectangle {
                            color: parent.down ? "#bbbbbb" :
                                                 (parent.hovered ? "#d6d6d6" : background.color)
                        }
                    }
                }
            }
        }
    }
}
