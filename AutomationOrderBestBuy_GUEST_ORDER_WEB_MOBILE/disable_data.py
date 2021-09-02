import time
from subprocess import Popen
import pytest
import os
import re
from colorama import init, Fore, Back, Style


processes = []
for counter in range(4):
    chrome_cmd = 'docker exec -it 93948d769d64 adb shell svc data disable'
    processes.append(Popen(chrome_cmd, shell=True))
sleep 3
adb shell svc data disable
sleep 3
adb shell svc data enable
    #edge_cmd = 'export Browser=MicrosoftEdge && python3 -m pytest mike_test.py -s'
    #processes.append(Popen(edge_cmd, shell=True))

    firefox_cmd = 'export Browser=firefox && python3 -m pytest test_guest_order.py'
    processes.append(Popen(firefox_cmd, shell=True))
    time.sleep(1)

for counter in range(4):
    processes[counter].wait()