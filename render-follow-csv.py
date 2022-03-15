import c4d
import time
import os
import csv
import json
from os import walk

# Set the condition for removal
# Choose a line or add a new one yourself:
Condition = lambda o: o[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] == 1 and o.GetBit(c4d.BIT_ACTIVE) == True

nameObject = ['body','ear','nose','eye','eyebrow','medal','necklaces','top','front face','side face','arms','accessories','back','background']
workDir = os.path.join("C:"+ os.sep, 'Users', 'bruno', 'Documents', 'bruno', 'demo')
pathSave = os.path.join(workDir, "save")
pathFile = os.path.join(workDir, "test.csv")
pathC4dFile = os.path.join(workDir, 'ELE_NIKU_08_500_test.c4d')
tail = ".png"

filenames = []
listObject = {}

# print("pathC4dFile", pathC4dFile)
# doc = c4d.documents.LoadDocument(pathC4dFile, c4d.SCENEFILTER_OBJECTS | c4d.SCENEFILTER_MATERIALS | c4d.SCENEFILTER_MERGESCENE, thread=None)
# file = c4d.documents.LoadDocument(pathC4dFile, 
#     c4d.SCENEFILTER_OBJECTS 
#     | c4d.SCENEFILTER_MATERIALS 
#     | c4d.SCENEFILTER_MERGESCENE
#     | c4d.SCENEFILTER_SAVE_BINARYCACHE
# )
# c4d.documents.InsertBaseDocument(file)
# doc = c4d.documents.GetActiveDocument()

def FindAllAndFill(name, listResult):
    print(name)
    d = doc.SearchObject(name)
    result = d.GetDown()

    while result is not None:
        result[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1
        listResult.append(result)
        newResult = result.GetNext()
        result = newResult

    for f in listResult:
        print(f)

def TurnObjectOn(nameObject, id, isOn):
    listObj = listObject[nameObject]
    for obj in listObj:
        if obj.GetName() == id:
            obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = isOn


def ReadCSVFile():
    file = open(pathFile)
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    name = []
    for row in csvreader:
        rows.append(row)
        name.append(row[0])
    InitFolder(name)
    index = 0

    for row in rows:
        ReadJson(row[1],name[index])
        index = index + 1

    file.close()

def ReadJson(jsonData,name):
    y = json.loads(jsonData)
    for data in y:
        TurnObjectOn(str(data) ,str(y[data]),0)

    logOut = str(name)
    print(name)

    fullPath = os.path.join(pathSave, logOut + tail)
    print("fullPath", fullPath)
    rd = doc.GetActiveRenderData()
    rd[c4d.RDATA_PATH]= fullPath
    c4d.CallCommand(12099)
    print("start")
    while c4d.CheckIsRunning ( c4d.CHECKISRUNNING_EXTERNALRENDERING )==True:
        print('rendering')
        time.sleep(2)
    print("done")
    # for data in y:
    #     print("Turn On Object")
    #     TurnObjectOn(str(data) ,str(y[data]),1)


def InitFolder(newFileName):
    print("Remove old file:")
    count = 0
    filenames = os.listdir(pathSave)

    for name in newFileName:
        nameCheck = name + tail
        if nameCheck in filenames:
            count = count + 1
            print("Remove: " + name)
            os.remove(os.path.join(pathSave, nameCheck))

    print("Finish remove, remove " + str(count) + " file(s)" )

def main():
    print ('--------------------Start run----------------')

    for d in nameObject:
        listObject[d] = []
        FindAllAndFill(d,listObject[d])

    ReadCSVFile()

    c4d.CallCommand(12098)
    doc.EndUndo()
    c4d.CallCommand(100004728)
    c4d.EventAdd()

if __name__=='__main__':
    main()