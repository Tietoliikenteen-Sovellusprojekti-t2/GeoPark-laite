var file = '/dev/ttyS0';

var GPS = require('gps');
var SerialPort = require('serialport');
var port = new SerialPort.SerialPort(file, {
  baudrate: 9600,
  parser: SerialPort.parsers.readline('\r\n')
});

var gps = new GPS;

gps.on('data', function(data) {
  console.log(data);
});

port.on('data', function(data) {
  gps.update(data);
});