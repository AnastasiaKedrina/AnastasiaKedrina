## Layouts
- В шапку можно добавить кнопку "назад" и аватарку пользователя
- Под шапкой может располагаться поисковая строка
- Кнопок меню может быть больше 3х
- Из кнопок меню можно выделить одну основную и выделить её

![2023-11-08_21-50-24](https://github.com/AnastasiaKedrina/QML/assets/113825953/34f763db-0856-4a0f-94e0-23032be02aff)

### Файл **main.qml**
```
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
                            anchors.right: parent.right
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
                            anchors.centerIn: parent
                            text: "Header"}
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
                            anchors.left: parent.left // якорь слева, чтобы справа был отступ
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
                    Text{
                        anchors.centerIn: parent
                        text: "Content"}
                }


                RowLayout {
                    // компоновщик строки для нижнего меню
                    id: footer
                    spacing: root.spacing

                    property color sideBtnColor:"moccasin"
                    property color centerBtnColor:header.headerColor
                    property int centerBtnHeight:root.bottomHeight
                    property int centerBtnWidth:root.width/4
                    property int sideBtnHeight:root.bottomHeight/1.5

                    Rectangle{
                        Layout.fillWidth: true
                        Layout.preferredHeight: footer.sideBtnHeight
                        Layout.alignment: Qt.AlignBottom
                        color: footer.sideBtnColor
                        Text{
                            anchors.centerIn: parent
                            text: "1"}
                    }
                    Rectangle{
                        Layout.fillWidth: true
                        Layout.preferredHeight: footer.sideBtnHeight
                        Layout.alignment: Qt.AlignBottom
                        color: footer.sideBtnColor
                        Text{
                            anchors.centerIn: parent
                            text: "2"}
                    }
                    Rectangle{
                        Layout.preferredWidth: footer.centerBtnWidth
                        Layout.preferredHeight: footer.centerBtnHeight
                        Layout.alignment: Qt.AlignBottom
                        color: footer.centerBtnColor
                        Text{
                            anchors.centerIn: parent
                            text: "3"}
                    }
                    Rectangle{
                        Layout.fillWidth: true
                        Layout.preferredHeight: footer.sideBtnHeight
                        Layout.alignment: Qt.AlignBottom
                        color: footer.sideBtnColor
                        Text{
                            anchors.centerIn: parent
                            text: "4"}
                    }
                    Rectangle{
                        Layout.fillWidth: true
                        Layout.preferredHeight: footer.sideBtnHeight
                        Layout.alignment: Qt.AlignBottom
                        color: footer.sideBtnColor
                        Text{
                            anchors.centerIn: parent
                            text: "5"}
                    }
                }
            }
        }
    }
}


```
