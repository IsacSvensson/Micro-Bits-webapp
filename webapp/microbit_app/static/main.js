// Create WebSocket connection.
const socket = new WebSocket('ws://localhost:8080');

// Connection opened
socket.addEventListener('open', function (event) {
    console.log('Connected to the WS Server!')
});

// Connection closed
socket.addEventListener('close', function (event) {
    console.log('Disconnected from the WS Server!')
});

// Listen for messages
socket.addEventListener('message', function (event) {
    var dataArr = event.data.split(";");
    
    var status = document.getElementById(dataArr[0]+"-status");
    var temp = document.getElementById(dataArr[0]+"-temp");
    var light = document.getElementById(dataArr[0]+"-light");

    temp.innerText = dataArr[2];
    light.innerText = dataArr[3];

    status.innerText = dataArr[1];
    if (dataArr[1] == "Not active"){
        temp.innerText = "-";
        light.innerText = "-";
    }
    else{
        temp.style.display = "inline-block";
        light.style.display = "inline-block";
    }
});
// Send a msg to the websocket
const sendMsg = () => {
    var room = document.getElementById('this-room').title;
    socket.send(room);
}

loadCanvas = (w, h, dots) => {
    var canvas = document.getElementById("canvas1");
    canvas.width  = w * 100;
    canvas.height = h * 100;
    ctx = canvas.getContext('2d');

    dots.forEach(element => {
        ctx.fillStyle = element[0];
        ctx.beginPath();
        ctx.ellipse(element[1] * 100, element[2] * 100, 3, 3, Math.PI/4, 0, 2*Math.PI);
        ctx.fill();
    setInterval(sendMsg, 1000)
    });
    
}