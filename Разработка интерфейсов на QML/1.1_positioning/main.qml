import QtQuick 2.15
import QtQuick.Window 2.15
Window {
    id:win

    property int winWidth:360
    property int winHeight:480
    width: winWidth
    height: winHeight
    minimumWidth: winWidth
    minimumHeight: winHeight

    visible: true
    title: qsTr("Hearts")

    Item{
        id:pattern_container
        anchors.fill: parent

        Rectangle{
            id:background
            anchors.fill: parent
            color:"pink"
        }

        Heart_pattern{
            id:line_1
            x:-30
            y:-20
            marginLeft:win.width/20
            marginTop:win.height/8
        }

    }

}
