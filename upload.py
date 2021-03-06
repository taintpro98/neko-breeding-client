import requests
import os
import glob

from constants import savePath, uploadUrl

nekoImagesCount = 0
nekoImages = list()

def upload(filepath):
    try:
        with open(filepath, 'rb') as fh:
            print('uploading {}'.format(filepath))
            files = {'neko': fh}
            print("The file content: ", files)
            res = requests.post(uploadUrl, files=files)
            print("response", res)
            res.close()
    except:
        upload(filepath)

while True:
    # nekoImages = [fn for fn in sorted(Path(pathSave).iterdir(), key=os.path.getmtime) if fn.as_posix().endswith("png")]
    nekoImages = list(filter(os.path.isfile, glob.glob(os.path.join(savePath, "*.png"))))
    nekoImages.sort(key=lambda x: os.path.getmtime(x))
    if nekoImagesCount < len(nekoImages):
        upload(nekoImages[-1])
        nekoImagesCount += 1