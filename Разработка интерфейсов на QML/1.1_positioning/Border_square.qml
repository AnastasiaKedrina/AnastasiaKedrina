import QtQuick 2.15

Item {
    property alias comSize:border_rect.width

    Rectangle{
        id:border_rect
        color: "red"
        height:border_rect.width
    }
}
