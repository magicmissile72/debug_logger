from datetime import datetime
import time
# Grab the 'current' time
# value = datetime.now()

# Check for arguments, but only one...
from sys import argv
import sys
import platform

# Functions used
# ---------------------------------------------------------------
def check_args():
    if len(argv) == 1:
        exit("This script requires at least one argument")
    elif len(argv) > 2:
        exit("This script requires at most one argument")
    else:
        script_name, arg1 = argv
        return script_name
# ---------------------------------------------------------------
def fix_log_name(script_name):
    temp1 = script_name.replace(".\\", "")
    temp2 = temp1.replace(".py", "", )
    logname = temp2 + "_debug.log"
    return logname
# ---------------------------------------------------------------
def get_time():
    current_time = datetime.now()
    format_time = current_time.strftime("%Y-%m-%d %H:%M:%S %f : ")
    return format_time
# ---------------------------------------------------------------
def write_debug(reason):
    ct = get_time()
    log.write(ct + reason + "\n")
    return
# ---------------------------------------------------------------



# ---------------------------------------------------------------
# Main program
# ---------------------------------------------------------------
#
# Setup
script_name = check_args()
logname = fix_log_name(script_name)
# Open debug log
log = open(logname, 'w')
log.truncate()
# get system info
os = platform.platform()
ver = str(sys.version)
info = str(sys.version_info)
log.write(os + "\n")
log.write(ver + "\n")
log.write(info + "\n")
log.write(("-" * 80) + "\n")
# Finished with the setup
# ---------------------------------------------------------------
print()
print("This program writes to a log")
print()
for x in range(0,10):
    print (f"x is equal to {x}")
    y = (f"line {x} output inside the loop where 'x' equals {x}")
    write_debug(y)
    time.sleep(1)
print("Finished...")

# Close the log file
log.write(("-" * 80) + "\n")
log.write("Closing the log file...")
log.close()
# ---------------------------------------------------------------
# EOF