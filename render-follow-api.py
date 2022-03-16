import c4d
import time
import requests
import os
import json
from os import walk
from constants import savePath, nameObject, tail, URL

listObject = {}

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

def render(name, jsonData):
    y = json.loads(jsonData)
    for data in y:
        TurnObjectOn(str(data) ,str(y[data]),0)
    logOut = str(name)
    print(name)
    fullPath = os.path.join(savePath, logOut + tail)
    print("fullPath", fullPath)
    rd = doc.GetActiveRenderData()
    rd[c4d.RDATA_PATH]= fullPath
    c4d.CallCommand(12099)
    while c4d.CheckIsRunning ( c4d.CHECKISRUNNING_EXTERNALRENDERING )==True:
        print('rendering')
        time.sleep(2)

def main():
    print ('--------------------Start rendering----------------')

    for d in nameObject:
        listObject[d] = []
        FindAllAndFill(d,listObject[d])
    idx = 0
    while True:
        r = requests.get(url = URL)
        data = r.json()
        print(data)
        render(data['name'] + str(idx), data['data'])
        idx += 1
        
    c4d.CallCommand(12098)
    doc.EndUndo()
    c4d.CallCommand(100004728)
    c4d.EventAdd()
    
if __name__=='__main__':
    main()
