import QtQuick 2.15
import QtQuick.Layouts 1.3
import QtQuick.Window 2.15

Window {
    id:win;
    property int winWidth:480
    property int winHeight:800
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
                        height: parent.height-100

                        Rectangle{
                            id:content_block_1
                            anchors.top: parent.top
                            anchors.margins: 10
                            color: header.headerColor
                            width: parent.width
                            height: 100
                            visible:true
                        }
                        Rectangle{
                            id:content_block_2
                            anchors.top: content_block_1.bottom
                            anchors.margins: 10
                            color: header.headerColor
                            width: parent.width
                            height: 100
                            visible:true
                        }
                        Rectangle{
                            id:content_block_3
                            anchors.top: content_block_2.bottom
                            anchors.margins: 10
                            color: header.headerColor
                            width: parent.width
                            height: 100
                            visible:true
                        }
                        Rectangle{
                            id:content_block_4
                            anchors.top: content_block_3.bottom
                            anchors.margins: 10
                            color: header.headerColor
                            width: parent.width
                            height: 100
                            visible:false
                        }
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
                            id:mouse_1
                            hoverEnabled: true
                            anchors.fill: btn_1
                            onPressed: {
                                btn_1.color=footer.btnColor_Select
                                btn_2.color=footer.btnColor
                                btn_3.color=footer.btnColor
                                btn_4.color=footer.btnColor
                                btn_5.color=footer.btnColor
                                searchBar.visible=false
                                header_text.text="Page 1"
                                content_block_1.color=header.headerColor
                                content_block_2.visible=false
                                content_block_3.visible=false
                                content_block_4.visible=false
                            }
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
                            id:mouse_2
                            hoverEnabled: true
                            anchors.fill: btn_2
                            onPressed: {
                                btn_1.color=footer.btnColor
                                btn_2.color=footer.btnColor_Select
                                btn_3.color=footer.btnColor
                                btn_4.color=footer.btnColor
                                btn_5.color=footer.btnColor
                                searchBar.visible=false
                                header_text.text="Page 2"
                                content_block_1.color=footer.btnColor_Select
                                content_block_2.color=footer.btnColor_Select
                                content_block_3.color=footer.btnColor_Select
                                content_block_2.visible=true
                                content_block_3.visible=true
                                content_block_4.visible=false
                            }
                        }
                    }
                    Rectangle{
                        id:btn_3
                        Layout.preferredWidth: footer.centerBtnWidth
                        Layout.preferredHeight: footer.centerBtnHeight
                        Layout.alignment: Qt.AlignBottom
                        color: footer.btnColor
                        Text{
                            anchors.centerIn: parent
                            text: "3"}
                        MouseArea {
                            id:mouse_3
                            hoverEnabled: true
                            anchors.fill: btn_3
                            onPressed: {
                                btn_1.color=footer.btnColor
                                btn_2.color=footer.btnColor
                                btn_3.color=footer.btnColor_Select
                                btn_4.color=footer.btnColor
                                btn_5.color=footer.btnColor
                                searchBar.visible=true
                                header_text.text="Page 3"
                                content_block_1.color=header.headerColor
                                content_block_2.color=header.headerColor
                                content_block_3.color=header.headerColor
                                content_block_4.color=header.headerColor
                                content_block_2.visible=true
                                content_block_3.visible=true
                                content_block_4.visible=true
                            }
                        }
                    }
                    Rectangle{
                        id:btn_4
                        Layout.fillWidth: true
                        Layout.preferredHeight: footer.sideBtnHeight
                        Layout.alignment: Qt.AlignBottom
                        color: footer.btnColor
                        Text{
                            anchors.centerIn: parent
                            text: "4"}
                        MouseArea {
                            id:mouse_4
                            hoverEnabled: true
                            anchors.fill: btn_4
                            onPressed: {
                                btn_1.color=footer.btnColor
                                btn_2.color=footer.btnColor
                                btn_3.color=footer.btnColor
                                btn_4.color=footer.btnColor_Select
                                btn_5.color=footer.btnColor
                                searchBar.visible=false
                                header_text.text="Page 4"
                                content_block_1.color=footer.btnColor
                                content_block_2.color=footer.btnColor
                                content_block_2.visible=true
                                content_block_3.visible=false
                                content_block_4.visible=false
                            }
                        }
                    }
                    Rectangle{
                        id:btn_5
                        Layout.fillWidth: true
                        Layout.preferredHeight: footer.sideBtnHeight
                        Layout.alignment: Qt.AlignBottom
                        color: footer.btnColor
                        Text{
                            anchors.centerIn: parent
                            text: "5"}
                        MouseArea {
                            id:mouse_5
                            hoverEnabled: true
                            anchors.fill: btn_5
                            onPressed: {
                                btn_1.color=footer.btnColor
                                btn_2.color=footer.btnColor
                                btn_3.color=footer.btnColor
                                btn_4.color=footer.btnColor
                                btn_5.color=footer.btnColor_Select
                                searchBar.visible=false
                                header_text.text="Page 5"
                                content_block_1.color=header.headerColor
                                content_block_2.color=header.headerColor
                                content_block_3.color=header.headerColor
                                content_block_2.visible=true
                                content_block_3.visible=true
                                content_block_4.visible=false
                            }
                        }
                    }
                }
            }
        }
    }
}
