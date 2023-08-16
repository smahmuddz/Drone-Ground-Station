const dgram = require('dgram');
const server = dgram.createSocket('udp4');

const droneIp = '192.168.10.1';
const dronePort = 8889;

// Initialize UDP server to receive Tello responses
server.on('listening', () => {
    const address = server.address();
    console.log(`UDP Server listening on ${address.address}:${address.port}`);
});

server.on('message', (message, remote) => {
    console.log(`Received response from ${remote.address}:${remote.port}: ${message}`);
    // Process the response
    // Implement logic to parse and handle the response data
});

server.bind(dronePort, '0.0.0.0'); // Bind to all available network interfaces

// Function to send commands to the Tello drone
function sendCommand(command) {
    const commandBuffer = Buffer.from(command);
    const client = dgram.createSocket('udp4');
    client.send(commandBuffer, 0, commandBuffer.length, dronePort, droneIp, err => {
        if (err) {
            console.error('Error sending command:', err);
        }
        client.close();
    });
}

function backward() {
    sendCommand('backward 20');
}

function forward() {
    sendCommand('forward 20');
}

function moveLeft() {
    sendCommand('left 20');
}

function moveRight() {
    sendCommand('right 20');
}

function ascend() {
    sendCommand('up 20');
}

function descend() {
    sendCommand('down 20');
}

function hold() {
    sendCommand('stop'); // Stop all movement
}

function stop() {
    sendCommand('emergency'); // Emergency stop
}
