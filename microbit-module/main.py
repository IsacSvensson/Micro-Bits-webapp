import os
from pathlib import Path
import json
from time import sleep
from datetime import date
from main_funcs import checkChanges, listenForNewMB, checkKnown, checkIntervals
import microbit_db as db
from mb import MicroBit

if __name__ == "__main__":
    # List of all possible COM-ports
    with open(os.path.join(Path(__file__).parent.absolute(), 'config.json')) as json_file:
        data = json.load(json_file)
    ports = data['ports']

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
            if mb.active:
                checkIntervals(mb)
        sleep(1)
        prevDate = newDate
