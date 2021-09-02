#!/usr/bin/env bash

import os
import time


container = ["73de35312a4c", "3092695b0d94"]
test = 0
restoreData = 'docker exec -it ' + container[test] + ' adb shell svc data enable'
restartChrome = 'docker exec -it ' + container[test] + ' adb shell pm clear com.android.chrome'

for i in container:
    os.popen(restoreData)
    os.popen(restartChrome)
    print(restoreData)
    test += 1


