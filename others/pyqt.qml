import QtQuick 2.15
import QtQuick.Controls 2.15
ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "Initial calc"
    Text {
        anchors.centerIn: parent
        text: "Logan"
        font.pixelSize: 24
    }
    Text {
        anchors.centerIn: parent
        text: "Logan"
        font.pixelSize: 20
    }
    ComboBox {
    width: 200
    model: [ "Banana", "Apple", "Coconut" ]
    }
   
}

