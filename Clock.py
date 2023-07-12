from datetime import datetime
import time
import os

# Platform names
macos = ("macos", "macOS", "MACos")
windows = ("windows", "WINDOWS", "Windows")
linux = ("linux", "Linux", "LINUX")

# Opening files
platform_open = open("platform", "a+")  # Open in append mode
platform_read = open("platform", "r")

# Read the platform from the file
platform_from_file = platform_read.read().strip()

# Check if the platform from the file is valid
if platform_from_file in windows:
    while True:
        now_windows = datetime.now()
        current_time_windows = now_windows.strftime("%H:%M:%S")
        os.system("cls")
        print(current_time_windows + " 24 Hour Format")
        time.sleep(1)

elif platform_from_file in linux or platform_from_file in macos:
    while True:
        now_other = datetime.now()
        current_time_other = now_other.strftime("%H:%M:%S")
        os.system("clear")
        print(current_time_other + " 24 Hour Format")
        time.sleep(1)

else:
    # Prompt the user for the platform if not found in the file
    platform_input = input("What platform are you on (Windows/macOS/Linux): ")
    
    if platform_input in windows:
        platform_open.seek(0)  # Move the file pointer to the beginning
        platform_open.truncate()  # Clear the file contents
        platform_open.write(platform_input)  # Write the platform to the file

        while True:
            now_windows = datetime.now()
            current_time_windows = now_windows.strftime("%H:%M:%S")
            os.system("cls")
            print(current_time_windows + " 24 Hour Format")
            time.sleep(1)

    elif platform_input in linux or platform_input in macos:
        platform_open.seek(0)
        platform_open.truncate()
        platform_open.write(platform_input)

        while True:
            now_other = datetime.now()
            current_time_other = now_other.strftime("%H:%M:%S")
            os.system("clear")
            print(current_time_other + " 24 Hour Format")
            time.sleep(1)

    else:
        print("Invalid platform")

platform_open.close()
platform_read.close()
