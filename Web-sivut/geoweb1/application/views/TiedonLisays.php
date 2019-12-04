<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket - Raspberry Pi</title>
        <meta charset="UTF-8">
    </head>
    <body>
        ## Test your websocket connection!
        <h3>Just type and press enter ;)</h3>
        <div id="container"></div>
        <input type="text" placeholder="Write your message to the WebSocket!" id="message" />
        <script>
            (function () {
                var url = 'ws://10.100.4.196:9002';
                var mySocket = new WebSocket(url);
                var container = document.getElementById('container');

                var key = document.onkeypress = function (event) {
                    event = event || window.event;

                    if (event.which == 13) {
                        var message = document.getElementById('message');

                        container.innerHTML += '<div><span>Me :</span><span>' + message.value + '</span></div>';
                        console.log('me: ' + message.value);
                        mySocket.send(message.value);
                        message.value = '';
                    }

                    return event.which;
                };

                mySocket.onopen = function () {
                    console.log('opened !');
                    container.innerHTML += '<h2>Connection established : ' + url + '</h2>';
                };

                mySocket.onmessage = function (e) {
                    console.log('server: ' + e.data);
                    container.innerHTML += '<div><span>Server: </span><span>' + e.data + '</span></div>';
                };

                mySocket.onclose = function () {
                    console.log('closed !');
                    container.innerHTML += '<h2>Connection closed</h2>';
                };
            }());
        </script>
    </body>
</html>