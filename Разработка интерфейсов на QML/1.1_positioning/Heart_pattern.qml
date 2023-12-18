import QtQuick 2.15

Item {
    property alias marginTop: hearts_container.marginTop
    property alias marginLeft: hearts_container.marginLeft

    Item{
        id:hearts_container
        property int marginTop
        property int marginLeft

        Heart{
            id:heart_1
            x:0
            y:0
        }
        Heart{
            id:heart_2
            anchors.top: heart_1.bottom
            anchors.left: heart_1.left
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
        Heart{
            id:heart_3
            anchors.top: heart_2.bottom
            anchors.left: heart_2.left
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
        Heart{
            id:heart_4
            anchors.top: heart_3.bottom
            anchors.left: heart_3.left
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
        Heart{
            id:heart_5
            anchors.top: heart_4.bottom
            anchors.left: heart_4.left
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
        Heart{
            id:heart_6
            anchors.top: heart_1.top
            anchors.left: heart_1.right
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
        Heart{
            id:heart_7
            anchors.top: heart_6.bottom
            anchors.left: heart_6.left
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
        Heart{
            id:heart_8
            anchors.top: heart_7.bottom
            anchors.left: heart_7.left
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
        Heart{
            id:heart_9
            anchors.top: heart_8.bottom
            anchors.left: heart_8.left
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
        Heart{
            id:heart_10
            anchors.bottom: heart_6.top
            anchors.left: heart_6.right
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
        Heart{
            id:heart_11
            anchors.top: heart_10.bottom
            anchors.left: heart_10.left
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
        Heart{
            id:heart_12
            anchors.top: heart_11.bottom
            anchors.left: heart_11.left
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
        Heart{
            id:heart_13
            anchors.top: heart_12.bottom
            anchors.left: heart_12.left
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
        Heart{
            id:heart_14
            anchors.top: heart_13.bottom
            anchors.left: heart_13.left
            anchors.topMargin:hearts_container.marginTop
            anchors.leftMargin:hearts_container.marginLeft
        }
    }
}

