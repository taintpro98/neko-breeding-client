import os
import time
from constants import pluginPath, renderPath

c4dCommand = 'python -u "{}" --file "{}"'.format(pluginPath, renderPath)
os.system(c4dCommand)