from mb import MicroBit
import microbit_db as db

def checkChanges(mb, date):
    """
    Input: MicroBit-instance, Date-string (YYYY-MM-DD)\n
    If the MB-object got no min/max-info history is set, if there is no history,
    a new entry is made in db.\n
    If there is history changes are updated to the entry.
    """
    setHistory(mb)
    new = False
    changes = False
    if mb.minTemp is None:
        new = True
        print("Minimum temperature of the day changed from {} to {}".format(mb.minTemp, mb.temp))
        mb.minTemp = mb.temp
        changes = True
    elif mb.temp < mb.minTemp:
        print("Minimum temperature of the day changed from {} to {}".format(mb.minTemp, mb.temp))
        mb.minTemp = mb.temp
        changes = True
    if mb.maxTemp is None:
        new = True
        print("Maximum temperature of the day changed from {} to {}".format(mb.maxTemp, mb.temp))
        mb.maxTemp = mb.temp
        changes = True
    elif mb.temp > mb.maxTemp:
        print("Maximum temperature of the day changed from {} to {}".format(mb.maxTemp, mb.temp))
        mb.maxTemp = mb.temp
        changes = True
    if mb.minLight is None:
        new = True
        print("Minimum light of the day changed from {} to {}".format(mb.minLight, mb.light))
        mb.minLight = mb.light
        changes = True
    elif mb.temp < mb.minLight:
        print("Minimum light of the day changed from {} to {}".format(mb.minLight, mb.light))
        mb.minLight = mb.light
        changes = True
    if mb.maxLight is None:
        new = True
        print("Maximum light of the day changed from {} to {}".format(mb.maxLight, mb.light))
        mb.maxLight = mb.light
        changes = True
    elif mb.light > mb.maxLight:
        print("Maximum light of the day changed from {} to {}".format(mb.maxLight, mb.light))
        mb.maxLight = mb.light
        changes = True
    if new:
        db.dbInsert('history', mb)
    if changes:
        db.dbUpdate(mb, date)
    

def checkKnown():
    """
    Returns a list of previously connected units from db. 
    """
    knownMBs = db.getMicroBits()
    toRet = list()
    if knownMBs:
        for mb in knownMBs:
            toRet.append(mb[0])
        return toRet
    return None

def setHistory(mb):
    """
    Input: MicroBit-object\n
    Checks if there is a previous db-entry for this date and this Micro:bit.
    If there is old data is imported to object. 
    """
    if mb.minTemp is None:
        data = db.getHistory()
        if data:
            for history in data:
                if mb.devName in history:
                    mb.minTemp = history[3]
                    mb.maxTemp = history[4]
                    mb.minLight = history[5]
                    mb.maxLight = history[6]

def listenForNewMB(microBits, knownMBs):
    """
    Input: List of MicroBit-objects, List of previously connected device (Strings).\n
    Matches connected Microbits to the known microbits. If new, adds the new 
    microbit to db. 
    """
    for mb in microBits:
        if (mb.testConnection()):
                mb.readValues()
                if not knownMBs:
                    db.dbInsert("microbit", mb)
                    knownMBs = [mb.devName]
                    setHistory(mb)
                elif mb.devName not in knownMBs:
                    db.dbInsert("microbit", mb)
                    knownMBs.append(mb.devName)
                    setHistory(mb)
    return knownMBs