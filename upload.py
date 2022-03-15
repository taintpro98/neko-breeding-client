import requests
import os
import os
from pathlib import Path

workDir = os.path.join("C:"+ os.sep, 'Users', 'bruno', 'Documents', 'bruno', 'neko-breeding-client')
pathSave = os.path.join(workDir, "save")
nekoImagesCount = 0
nekoImages = list()

URL = "http://localhost:5000"

# while True:
#     print("waiting...")
#     nekoImages = sorted(Path(pathSave).iterdir(), key=os.path.getmtime)
#     if nekoImagesCount < len(nekoImages):
#         print('uploading {}'.format(nekoImages[-1]))
#         files = {'neko': open(nekoImages[-1], 'rb')}
#         requests.post(URL + "/upload", files=files)
#     nekoImagesCount += 1
print("upload")