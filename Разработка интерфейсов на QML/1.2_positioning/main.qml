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

    title: qsTr("Task for layout")

    Item
    {
        id: root
        anchors.fill: parent

        property int margin:5
        property int headHeight:win.height/10
        property int bottomHeight:win.height/6
        property color backColor:"black"
        property color headColor:"lightpink"
        property color contentColor:"moccasin"
        property color btnColor:"lightseagreen"


        Rectangle
        {
            id:background
            anchors.fill: parent
            color:root.backColor

        }
        Rectangle
        {
            id:rect_top
            color: root.headColor
            anchors.top: parent.top
            anchors.left: parent.left
            anchors.right:parent.right
            anchors.margins:root.margin
            height:root.headHeight

            Text{
                id: text_top
                text: "Header"
                anchors.centerIn: parent

            }
        }

        Rectangle
        {
            id:rect_mid
            color: root.contentColor
            anchors.top: rect_top.bottom
            anchors.left: parent.left
            anchors.right:parent.right
            anchors.bottom: rect_btn_1.top
            anchors.margins:root.margin

            Text{
                id: text_mid
                text: "Contetnt"
                anchors.centerIn: parent

            }
        }

        Rectangle
        {
            id:rect_btn_1
            color: root.btnColor
            anchors.left: parent.left
            anchors.bottom: parent.bottom
            width:(root.width - root.margin*4)/3
            height:root.bottomHeight
            anchors.margins:root.margin

            Text{
                id: text_btn_1
                text: "1"
                anchors.centerIn: parent

            }
        }
        Rectangle
        {
            id:rect_btn_2
            color: root.btnColor
            anchors.left: rect_btn_1.right
            anchors.bottom: parent.bottom
            width:(root.width - root.margin*4)/3
            height:root.bottomHeight
            anchors.margins:root.margin

            Text{
                id: text_btn_2
                text: "2"
                anchors.centerIn: parent

            }
        }
        Rectangle
        {
            id:rect_btn_3
            color: root.btnColor
            anchors.left: rect_btn_2.right
            anchors.bottom: parent.bottom
            width:(root.width - root.margin*4)/3
            height:root.bottomHeight
            anchors.margins:root.margin

            Text{
                id: text_btn_3
                text: "3"
                anchors.centerIn: parent

            }
        }
    }
}
