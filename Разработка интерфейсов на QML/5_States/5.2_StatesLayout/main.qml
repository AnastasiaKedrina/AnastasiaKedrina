import QtQuick 2.15
import QtQuick.Layouts 1.3
import QtQuick.Window 2.15

Window {
    id:win;
    property int winWidth:320
    property int winHeight:480
    width: winWidth
    height: winHeight
    minimumWidth: winWidth
    minimumHeight: winHeight

    visible: true
    title: qsTr("Layouts")

    Item{
        id: root
        anchors.fill: parent
        property int spacing:2
        property int headHeight:win.height/12
        property int searchBarHeight:win.height/20
        property int bottomHeight:win.height/12
        property color backColor:"floral white"

        Rectangle{
            // прямоугольник для фона
            anchors.fill:parent
            color: root.backColor

            ColumnLayout{
                // компоновщик столбца на всё окно
                anchors.fill:parent
                spacing: root.spacing


                RowLayout {
                    // компоновщик строки для шапки
                    id:header
                    spacing: root.spacing
                    property color headerColor:"lightpink"
                    Rectangle {
                        id:back
                        visible:false
                        Layout.alignment: Qt.AlignCenter
                        Layout.preferredWidth: root.headHeight
                        Layout.preferredHeight: root.headHeight
                        color: header.headerColor
                        Rectangle{
                            // дополнительный прямоугольник,
                            // чтобы выровнять кнопку с отступом от края слева
                            color:header.headerColor
                            height: root.headHeight/1.5
                            width: root.headHeight/1.5
                            anchors.centerIn: parent
                            anchors.verticalCenter: parent.verticalCenter
                            Text{
                                anchors.centerIn: parent
                                text: "<-"}
                        }
                    }
                    Rectangle {
                        Layout.alignment: Qt.AlignCenter
                        Layout.fillWidth: true
                        Layout.preferredHeight: root.headHeight
                        color: header.headerColor
                        Text{
                            id:header_text
                            anchors.centerIn: parent
                            text: "Page"}
                    }
                    Rectangle {
                        Layout.alignment: Qt.AlignCenter
                        Layout.preferredWidth: root.headHeight
                        Layout.preferredHeight: root.headHeight
                        color: header.headerColor
                        Rectangle{
                            // круг для аватарки
                            radius: width*0.5
                            color:"white"
                            height: root.headHeight/1.5
                            width: root.headHeight/1.5
                            anchors.centerIn: parent
                            anchors.verticalCenter: parent.verticalCenter
                        }
                    }
                }
                Rectangle {
                    // контейнер для поиска
                    id:searchBar
                    color: "moccasin"
                    Layout.fillWidth: true
                    Layout.preferredHeight: root.searchBarHeight
                    visible:false
                    Rectangle {
                        radius: height*0.5
                        width: root.searchBarHeight*8
                        height: root.searchBarHeight/1.5
                        color: "white"
                        anchors.centerIn: parent
                        Text{
                            anchors.centerIn: parent
                            text: "Search"}
                    }

                }


                Rectangle{
                    // контейнер для контента
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    color: root.backColor
                    //Text{
                    //anchors.centerIn: parent
                    //text: "Content"}

                    Rectangle{
                        id:content
                        anchors.centerIn: parent
                        color: root.backColor
                        width: parent.width-60
                        height: parent.height

                        Rectangle{
                            id:content_1
                            anchors.top: parent.top
                            anchors.margins: 10
                            color: header.headerColor
                            width: parent.width
                            height: 100
                            visible:true
                        }
                        Rectangle{
                            id:content_2
                            anchors.top: content_1.bottom
                            anchors.margins: 10
                            color: header.headerColor
                            width: parent.width
                            height: 100
                            visible:true
                        }
                        Rectangle{
                            id:content_3
                            anchors.top: content_2.bottom
                            anchors.margins: 10
                            color: header.headerColor
                            width: parent.width
                            height: 100
                            visible:true
                        }



                        states:[
                            State {
                                name: "first"
                                PropertyChanges {target:content_1; color:header.headerColor;}
                                PropertyChanges {target:content_2; color:root.backColor}
                                PropertyChanges {target:content_3; color:root.backColor}
                                PropertyChanges {target:btn_1; color:footer.btnColor_Select}
                                PropertyChanges {target:btn_2; color:footer.btnColor}
                                PropertyChanges {target:btn_3; color:footer.btnColor}
                                PropertyChanges {target:back; visible:false}
                            },
                            State {
                                name: "second"
                                PropertyChanges {target:content_1; color:footer.btnColor}
                                PropertyChanges {target:content_2; color:footer.btnColor}
                                PropertyChanges {target:content_3; color:footer.btnColor}
                                PropertyChanges {target:btn_1; color:footer.btnColor}
                                PropertyChanges {target:btn_2; color:footer.btnColor_Select}
                                PropertyChanges {target:btn_3; color:footer.btnColor}
                                PropertyChanges {target:back; visible:true}
                            },
                            State {
                                name: "third"
                                PropertyChanges {target:content_1; color:footer.btnColor_Select}
                                PropertyChanges {target:content_2; color:footer.btnColor_Select}
                                PropertyChanges {target:content_3; color:root.backColor}
                                PropertyChanges {target:btn_1; color:footer.btnColor}
                                PropertyChanges {target:btn_2; color:footer.btnColor}
                                PropertyChanges {target:btn_3; color:footer.btnColor_Select}
                                PropertyChanges {target:back; visible:true}
                            } ]

                        transitions:[
                            Transition {
                                ColorAnimation  {
                                    target: content_1
                                    properties: "color"
                                    duration: 500
                                }
                                ColorAnimation  {
                                    target: content_2
                                    properties: "color"
                                    duration: 500
                                }
                                ColorAnimation  {
                                    target: content_3
                                    properties: "color"
                                    duration: 500
                                }
                                ColorAnimation  {
                                    target: btn_1
                                    properties: "color"
                                    duration: 500
                                }
                                ColorAnimation  {
                                    target: btn_2
                                    properties: "color"
                                    duration: 500
                                }
                                ColorAnimation  {
                                    target: btn_3
                                    properties: "color"
                                    duration: 500
                                }
                            }
                        ]

                    }
                }

                RowLayout {
                    // компоновщик строки для нижнего меню
                    id: footer
                    spacing: root.spacing

                    property color btnColor:"moccasin"
                    property color btnColor_Select:"#F0AF40"

                    property int centerBtnHeight:root.bottomHeight
                    property int centerBtnWidth:root.width/4
                    property int sideBtnHeight:root.bottomHeight/1.5

                    Rectangle{
                        id:btn_1
                        Layout.fillWidth: true
                        Layout.preferredHeight: footer.sideBtnHeight
                        Layout.alignment: Qt.AlignBottom
                        color: footer.btnColor
                        Text{
                            anchors.centerIn: parent
                            text: "1"}

                        MouseArea {
                            anchors.fill:parent
                            onClicked: content.state = "first"
                        }
                    }
                    Rectangle{
                        id:btn_2
                        Layout.fillWidth: true
                        Layout.preferredHeight: footer.sideBtnHeight
                        Layout.alignment: Qt.AlignBottom
                        color: footer.btnColor
                        Text{
                            anchors.centerIn: parent
                            text: "2"}

                        MouseArea {
                            anchors.fill:parent
                            onClicked: content.state = "second"}
                    }
                    Rectangle{
                        id:btn_3
                        Layout.fillWidth: true
                        Layout.preferredHeight: footer.sideBtnHeight
                        Layout.alignment: Qt.AlignBottom
                        color: footer.btnColor
                        Text{
                            anchors.centerIn: parent
                            text: "3"}
                        MouseArea{
                            anchors.fill:parent
                            onClicked: content.state = "third"
                        }
                    }

                }
            }
        }
    }
}
