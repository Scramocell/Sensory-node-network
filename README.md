# Sensory-node-network

This was part of my Engineering Education Scheme project which involved creating a node network of mobile nodes each with the capability of recording water depth data and sending it along the node to a base station.

This is the final version of the project as it stands. The node.py is the python file that is flashed onto every node, each node has to have a specific tag that has to be hard coded in. The program is designed to be run on a microbit using micropython and requries no additional libraries.

the log2graph.py and log2excel.py are run on the base computer. The base computer must be running teraterm, with the connection set to serial and 115200 baudrate, clicking the 'log' button located in 'file' you must rename the log file to 'teraterm.txt'. Then the two programs will work. The 'excel' script requires 'xlwt' which can be 'pip' installed and the 'graph' script requires 'matplotlib' which can also be 'pip' installed.

The sensor used was the JSN-SR04T with the 'trig' going to pin 0, on the microbit, the 'echo' to pin 1 and 'GND' to 'GND'. The sensors requires an external 5v supply. In my experience the sensor is very poor, but we had a tight budget more expensive options are out there with the same pin layout: 'GND', 'trig', 'echo' and high volts.

following these instruction you should be able to setup a network of any number of nodes relaying data to a base station which stores and displays the incoming data
