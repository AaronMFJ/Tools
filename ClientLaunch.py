import sys

# Global variable that holds the path to the LaunchRNR.txt file.
# This makes it easy to update the path when needed.
# For Python3+, use input instead of raw_input

LAUNCH_RNR_TEXT_FILE = "JoinMultiPlayerGameMULTI.bat"

idName = str(raw_input("Login: "))
idPass = str(raw_input("Password: "))

try:
    idCount = int(input("How many iterations: "))
except ValueError:
    # If the value is not a number then stop here.
    print("'ERROR: How many iterations' needs a numeric value.")
    sys.exit(1)

idCommand = str(raw_input("Launch commands: "))

# List of commands to run.
commandLines = []
standardCommand = '@cd "ShooterGame\Binaries\Win64" \n'
startCommand = '@start RNR-Win64-Test.exe -log -serverbranch=dev -quickmatch=dev '

# Build a list of commands to be run.
# Use the player count as the max range for this loop.
for userCount in range(1, idCount):
    # Build the command line.  Example: " -DebugAutoLogin=john.doe9:my-password -forced_team=DEV_NO_WAIT"
    cmdLine = startCommand + "-DebugAutoLogin=" + idName + str(userCount) + ":" + idPass + " " + idCommand + '\n'
    commandLines.append(cmdLine)

# Write out the file.
with open(LAUNCH_RNR_TEXT_FILE, 'w') as f:
    f.writelines(standardCommand)
    f.writelines(commandLines)

