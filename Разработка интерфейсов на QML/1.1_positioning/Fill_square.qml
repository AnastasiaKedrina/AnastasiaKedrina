import QtQuick 2.15

Item {
    property alias comSize:fill_rect.width

    Rectangle{
        id:fill_rect
        color: "white"
        height:fill_rect.width
    }
}
