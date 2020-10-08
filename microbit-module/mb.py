from serial import SerialException
import serial
import microbit_db as db

class MicroBit:
    """
    Handler class for microbit over USB
    """
    def __init__(self, port):
        self.connection = serial.Serial()
        self.connection.baudrate = 9600
        self.connection.port = port
        # Current data:
        self.devName = str()
        self.temp = None
        self.light = None
        self.active = False
        # Min/Max data
        self.minTemp = None
        self.maxTemp = None
        self.minLight = None
        self.maxLight = None
        self.lowTemp = None
        self.highTemp = None
        self.tempWarning = False
        self.lowLight = None
        self.highLight = None
        self.lightWarning = False
        self.mail = None
    def testConnection(self):
        """
        Tests the connection over given port
        """
        try:
            self.connection.open()
            if self.active is False:
                self.active = True
                db.dbSetStatus(self, 'Active')
        except SerialException:
            # print("> Test Failed: Could not access the given port {}".format(self.connection.port))
            if self.active is True:
                self.active = False
                db.dbSetStatus(self, 'Not active')
            return False
        self.connection.close()
        self.active = True
        return True

    def readValues(self):
        """
        Opens a connection to the Micro:bit and reads one line, splits it into 
        a list of three elements \n
        Returns: string:'device name', int:'temperature', int:'light'
        """
        try:
            with self.connection as s:
                raw = s.readline().decode().split(";")
                data = list()
                try:
                    data.append(raw[0])
                    data.append(int(raw[1]))
                    data.append(int(raw[2].split('#')[0]))
                except IndexError:
                    print("Error: Corrupted input.")
                    self.active = False
                    db.dbSetStatus(self, 'Not active')
                    return False
                except KeyboardInterrupt:
                    print("Manually disconnected")
                    self.active = False
                    db.dbSetStatus(self, 'Not active')
                    return False
                if self.active is False:
                    self.active = True
                    db.dbSetStatus(self, "Active")
                self.devName = data[0]
                if self.temp != data[1] or self.light != data[2]:
                    self.temp = data[1]
                    self.light = data[2]
                    db.dbUpdate(self, None, 'microbit')
                return True
        except SerialException:
            if self.active is True:
                self.active = False
                db.dbSetStatus(self, 'Not active')
            return 'Could not connect to port: {}'.format(self.connection.port)
        except UnicodeDecodeError:
            print("Error: Corrupted input.")
            self.active = False
            db.dbSetStatus(self, 'Not active')
            return False
        except ValueError:
            print("Error: Corrupted input.")
            self.active = False
            db.dbSetStatus(self, 'Not active')
            return False

    def clear(self):
        self.minLight = None
        self.maxLight = None
        self.minTemp = None
        self.maxLight = None

    def __repr__(self):
        return "Device name: {}\nTemperature: {}\nLight: {}".format(
            self.devName, self.temp, self.light
            )
