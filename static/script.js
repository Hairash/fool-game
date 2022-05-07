const socket = new WebSocket(`ws://${window.location.host}/ws/url/`);

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    console.log(data);
    switch (data.type) {
        case 'message':
            document.querySelector('#counter').innerText = data.data;
            break;
        case 'players':
            document.querySelector('#players_counter').innerText = data.data;
            break;
        case 'private_message':
            document.querySelector('#private_counter').innerText = data.data;
            break;
    }

}

document.querySelector('#send_button').onclick = function(e) {
    socket.send(JSON.stringify({
        'type': 'message',
        'data': document.querySelector('#counter').innerText,
    }));
};

document.querySelector('#private_send_button').onclick = function(e) {
    socket.send(JSON.stringify({
        'type': 'private_message',
        'data': 1,
    }));
};
