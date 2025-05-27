import os 
import eel

from engine.feautures import playAssistantsound
playAssistantsound()
eel.init('www')
os.system('start chrome.exe --app="http://localhost:800/index.html"')

eel.start('index.html',mode='chrome',host='localhost',block=True)
