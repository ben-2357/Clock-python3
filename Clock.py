from datetime import datetime
import time
import os
macos = ("macos", "macOS", "MACos")
windows = ("windows", "WINDOWS", "Windows")
linux = ("linux", "Linux", "LINUX")
platform = input("What platform are you on (Windows/macOS/Linux): ")
if platform in windows:
    while True:
        now_windows = datetime.now()
        current_time_windows = now_windows.strftime("%H:%M:%S")
        os.system("cls")
        print(current_time_windows)
        time.sleep(1)
#other includes macOS and Linux
elif platform in linux or platform in macos:
    while True:
        now_other = datetime.now()
        current_time_other = now_other.strftime("%H:%M:%S")
        os.system("clear")
        print(current_time_other)
        time.sleep(1)
else:
    print("Invalid platform")