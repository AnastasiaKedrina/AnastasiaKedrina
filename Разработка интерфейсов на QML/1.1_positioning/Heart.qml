import QtQuick 2.15

Item{
    property int rect_size: win.width/22

    id: heart_container
    width:rect_size*7
    height:rect_size*6

    Fill_square{
        property int rect_size: heart_container.width/7
        id:heart_fill_1
        x:rect_size*1
        y:rect_size*1
        comSize:rect_size*2
    }
    Fill_square{
        property int rect_size: heart_container.width/7
        id:heart_fill_2
        x:rect_size*2
        y:rect_size*2
        comSize:rect_size*3
    }
    Fill_square{
        property int rect_size: heart_container.width/7
        id:heart_fill_3
        x:rect_size*4
        y:rect_size*1
        comSize:rect_size*2
    }

    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_1
        x:rect_size*1
        y:rect_size*0
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_2
        x:rect_size*2
        y:rect_size*0
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_3
        x:rect_size*0
        y:rect_size*1
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_4
        x:rect_size*0
        y:rect_size*2
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_5
        x:rect_size*1
        y:rect_size*3
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_6
        x:rect_size*2
        y:rect_size*4
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_7
        x:rect_size*3
        y:rect_size*5
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_8
        x:rect_size*3
        y:rect_size*1
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_9
        x:rect_size*4
        y:rect_size*0
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_10
        x:rect_size*5
        y:rect_size*0
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_11
        x:rect_size*6
        y:rect_size*1
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_12
        x:rect_size*6
        y:rect_size*2
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_13
        x:rect_size*5
        y:rect_size*3
        comSize:rect_size*1
    }
    Border_square{
        property int rect_size: heart_container.width/7
        id:heart_border_14
        x:rect_size*4
        y:rect_size*4
        comSize:rect_size*1
    }

}
