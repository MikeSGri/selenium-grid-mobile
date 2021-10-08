# selenium-grid-mobile

# upgrading appium chrome driver
 1. head over to https://sites.google.com/a/chromium.org/chromedriver/downloads and locate the chrome version of your device
 2. in line 93 update the chrome version copying full text
 3. create a new image with new update

# restarting device in order to continues testing 
1. adb shell pm clear com.android.chrome
