from time import sleep
from datetime import date
from main_funcs import *

if __name__ == "__main__":
    # List of all possible COM-ports
    ports = ["COM3", "COM4"]
    microBits = list()
    for port in ports:
        # Creates a class instance for each port in list
        microBits.append(MicroBit(port))

    knownMBs = listenForNewMB(microBits, checkKnown())

    raw = db.getHistory()
    prevDate = None
    if raw:
        prevDate = raw[0][1]
    newDate = None
    
    while True:
        knownMBs = listenForNewMB(microBits, knownMBs)
        # Loop through the list and print values if active.
        for mb in microBits:
            # Checks if it's a new day
            newDate = date.today().strftime("%Y-%m-%d")
            if prevDate != newDate:
                mb.clear()
                if mb.active:
                    db.dbInsert("history", mb)

            # If device is connected
            if (mb.testConnection()):
                mb.readValues()
                checkChanges(mb, newDate)
            elif not knownMBs: 
                pass
            else:
                if mb.devName in knownMBs and mb.active:
                    db.dbSetStatus(mb, "Not active")
        sleep(1)
        prevDate = newDate
