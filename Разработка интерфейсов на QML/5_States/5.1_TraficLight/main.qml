import QtQuick 2.15
import QtQuick.Window 2.15
Window
{
    id:win
    property int winWidth:360
    property int winHeight:480
    width: winWidth
    height: winHeight
    minimumWidth: winWidth
    minimumHeight: winHeight
    visible: true


    Item
    {
        id: root
        anchors.fill: parent

        Rectangle
        {
            property int rect_size:120
            id:rect
            anchors.centerIn: parent
            width: rect_size
            height: winHeight-50
            color:"gray"

            Rectangle
            {
                id:rect_red
                anchors.top: parent.top
                //anchors.verticalCenter: parent.verticalCenter
                width: rect.rect_size
                height: rect.rect_size
                color:"black"

            }
            Rectangle
            {
                id:rect_yellow
                anchors.centerIn: parent
                width: rect.rect_size
                height: rect.rect_size
                color:"black"
            }
            Rectangle
            {
                id:rect_green
                anchors.bottom: parent.bottom
                //anchors.verticalCenter: parent.verticalCenter
                width: rect.rect_size
                height: rect.rect_size
                color:"black"
            }
        }
        states:[
            State {
                name: "stop"
                PropertyChanges {target: rect_red; color:"red"}
                PropertyChanges {target:rect_yellow;color:"black"}
                PropertyChanges {target:rect_green;color:"black"}
            },
            State {
                name: "caution"
                PropertyChanges {target: rect_red;color:"black"}
                PropertyChanges {target:rect_yellow;color:"yellow"}
                PropertyChanges {target:rect_green;color:"black"}
            },
            State {
                name: "go"
                PropertyChanges {target: rect_red;color:"black"}
                PropertyChanges {target:rect_yellow;color:"black"}
                PropertyChanges {target:rect_green;color:"green"}
            } ]

        transitions:[
            Transition {
                from: "stop"
                to: "caution"
                ColorAnimation  {
                    target: rect_red
                    properties: "color"
                    duration: 1000
                }
            },
            Transition {
                from: "caution"
                to: "stop"
                ColorAnimation  {
                    target: rect_red
                    properties: "color"
                    duration: 1000
                }
            },

            Transition {
                from: "caution"
                to: "go"
                ColorAnimation  {
                    target: rect_yellow
                    properties: "color"
                    duration: 1000
                }
            },
            Transition {
                from: "go"
                to: "caution"
                ColorAnimation  {
                    target: rect_yellow
                    properties: "color"
                    duration: 1000
                }
            },

            Transition {
                from: "go"
                to: "stop"
                ColorAnimation  {
                    target: rect_green
                    properties: "color"
                    duration: 1000
                }
            },
            Transition {
                from: "stop"
                to: "go"
                ColorAnimation  {
                    target: rect_green
                    properties: "color"
                    duration: 1000
                }
            }
        ]

        MouseArea{
            anchors.fill:parent
            onClicked: {
                if (parent.state === "stop") {
                    parent.state = "caution";
                } else if (parent.state === "caution") {
                    parent.state = "go";
                } else {
                    parent.state = "stop";
                }
            }
        }

    }

}
