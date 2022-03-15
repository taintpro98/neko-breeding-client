import os

pluginPath = os.path.join("C:"+ os.sep, 'Users', 'bruno', 'AppData', 'Roaming', 'Maxon', 'Maxon Cinema 4D R25_1FE0824E', 'plugins', 'SendPythonCode', 'send_python_code.py')
renderPath = os.path.join("C:"+ os.sep, 'Users', 'bruno', 'Documents', 'bruno', 'demo', 'render-follow-api.py')
c4dCommand = 'python -u "{}" --file "{}"'.format(pluginPath, renderPath)
os.system(c4dCommand) 