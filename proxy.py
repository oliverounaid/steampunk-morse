from serial import Serial
import socketio
​
serial_port_name = 'COM6'
URL = "http://localhost:8000"
URL = "https://kak-socketio-server.herokuapp.com"
​
sio = socketio.Client()
​
serial_port = Serial(port=serial_port_name, baudrate=9600, timeout=2)
​
@sio.event
def connect():
    print('connection established')
​
@sio.on('send-data')
def on_message(data):
    print(data)
    if 'python' in data:
        if data['python'] == 'on':
            serial_port.write(b'5')
        elif  data['python'] == 'off':
            serial_port.write(b'6')
        # print(serial_port.readline())
​
@sio.event
def disconnect():
    print('disconnected from server')
    
sio.connect(URL)
​
while True:
    value = serial_port.readline().decode('utf-8').strip().split()
    
    if value:
        print('Value:', value[0], value[1])
        sio.emit('send-data', {value[0]: value[1]})
​
​
    
  
​
​
​
​
Coll