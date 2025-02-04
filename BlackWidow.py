# Import necessary libraries
import sys  # To interact with system-specific parameters and functions
import time  # To handle time-related tasks, like sleep delays

# Print a welcome message with the developer's name
print("\nWelcome Branch - Developer: Konner Hunt")

# Print the InfoTechCenter system version
print("\nWelcome to InfoTechCenter v1.0\n")

# Initialize variables
x = 0  # Counter for the booting process
ellipsis = 0  # Counter for the number of dots in the booting message

# Loop to simulate the system booting process
while x != 20:
    x += 1  # Increment the counter to simulate boot steps
    # Construct the booting message with dynamic dots for a loading effect
    message = ("Infotech Center System Booting" + "." * ellipsis)
    ellipsis += 1  # Increase the number of dots in the message
    sys.stdout.write("\r" + message)  # Write the message to stdout with carriage return for overwrite
    time.sleep(.5)  # Pause for 0.5 seconds between each step to simulate progress

    # Reset the ellipsis counter after reaching 4 dots
    if ellipsis == 4:
        ellipsis = 0

    # When the loop reaches 20 iterations, print the system's status
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted\n")
