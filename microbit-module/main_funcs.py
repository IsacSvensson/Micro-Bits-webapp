from mb import MicroBit
import microbit_db as db
from mailmodule import mail

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

def checkIntervals(mbObj):
    mb = db.getMicroBit(mbObj.devName)
    mbObj.lowTemp = mb[8] if mb[8] else 0
    mbObj.highTemp = mb[10] if mb[10] else 100
    mbObj.lowLight = mb[9] if mb[9] else 0
    mbObj.highLight = mb[11] if mb[11] else 256
    mbObj.mail = mb[12]

    msg = None

    print("{},{},{},{},{}".format(mbObj.devName, mbObj.temp, mbObj.lowTemp, mbObj.highTemp, mbObj.tempWarning))
    if ((mbObj.temp < mbObj.highTemp) and (mbObj.temp > mbObj.lowTemp)):
        mbObj.tempWarning = False
        print('temp normal')
    elif not mbObj.tempWarning and (mbObj.temp < mbObj.lowTemp):
        if mbObj.mail:
            mbObj.tempWarning, msg = mail.sendWarning("temperature", "lower", mbObj.devName, mbObj.mail)
            msg = "".join(["Sent mail: ", msg])
        else:
            mbObj.tempWarning = True
            msg = "System Warning: Temperature is lower than allowed interval"
    elif not mbObj.tempWarning and (mbObj.temp > mbObj.highTemp):
        if mbObj.mail:
            mbObj.tempWarning, msg = mail.sendWarning("temperature", "higher", mbObj.devName, mbObj.mail)
            msg = "".join(["Sent mail: ", msg])
        else:
            mbObj.tempWarning = True
            msg = "System Warning: Temperature is higher than allowed interval"

    if (mbObj.light < mbObj.highLight) and (mbObj.light > mbObj.lowLight):
        mbObj.lightWarning = False
        print("light normal")
    elif not mbObj.lightWarning and (mbObj.light < mbObj.lowLight):
        if mbObj.mail:
            mbObj.lightWarning, msg = mail.sendWarning("light level", "lower", mbObj.devName, mbObj.mail)
            msg = "".join(["Sent mail: ", msg])
        else:
            mbObj.lightWarning = True
            msg = "System Warning: light level is lower than allowed interval"
    elif not mbObj.lightWarning and (mbObj.light > mbObj.highLight):
        if mbObj.mail:
            mbObj.lightWarning, msg = mail.sendWarning("light level", "higher", mbObj.devName, mbObj.mail)
            msg = "".join(["Sent mail: ", msg])
        else:
            mbObj.lightWarning = True
            msg = "System Warning: light level is higher than allowed interval"
    if msg:
        print(db.dbInsert('event', mbObj, msg))