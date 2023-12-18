import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.5


Window {
    property int winWidth:360
    property int winHeight:640
    width: winWidth
    height: winHeight
    minimumWidth: winWidth
    minimumHeight: winHeight
    visible: true
    title: qsTr("List")

    Page{
        id:page
        anchors.fill:parent

        Rectangle {
            anchors.fill:parent
            anchors.topMargin: 50

            gradient: Gradient {
                GradientStop { position: 0.0; color: "white" }
                GradientStop { position: 0.33; color: "yellow" }
                GradientStop { position: 1.0; color: "green" }
            }

            ListModel{
                id:my_model
                ListElement{ message:"Hello!"; time:"11:09"}
                ListElement{ message:"How are you?"; time:"11:10"}
            }
            Component{
                id:my_delegate
                MyDelegate{
                    message:model.message
                    time:model.time
                    width:200
                    height:50
                    //anchors.horizontalCenter: parent.horizontalCenter
                    anchors.left:parent.left
                    anchors.margins: 20
                }
            }
            ListView{
                id:my_list
                anchors.fill:parent
                spacing: 10
                model:my_model
                delegate:my_delegate
            }
        }

        footer: PageFooter {
            onNewMessage: {
                //Append new message
                var newMsg = {};
                newMsg.message = msg;
                newMsg.time = Qt.formatTime(new Date(), "hh:mm");
                my_model.append(newMsg);
            }
        }
    }
}
