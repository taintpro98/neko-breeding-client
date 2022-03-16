import os 

URL = "http://localhost:5000/"
uploadUrl = URL + "upload"

pluginPath = os.path.join("C:"+ os.sep, 'Users', 'bruno', 'AppData', 'Roaming', 'Maxon', 'Maxon Cinema 4D R25_1FE0824E', 'plugins', 'SendPythonCode', 'send_python_code.py')
renderPath = os.path.join("C:"+ os.sep, 'Users', 'bruno', 'Documents', 'bruno', 'neko-breeding-client', 'render-follow-api.py')

workDir = os.path.join("C:"+ os.sep, 'Users', 'bruno', 'Documents', 'bruno', 'neko-breeding-client')
savePath = os.path.join(workDir, "save")