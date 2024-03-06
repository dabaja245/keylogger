


Overview
This Python script implements a simple keylogger using the pynput library. A keylogger is a program that records keystrokes made by a user, typically covertly, to monitor user activity.

Functionality
Key Logging: The script captures keys pressed by the user and logs them into a file named log.txt.
Stopping Mechanism: It allows the user to stop the keylogging process by pressing the escape key (Esc).
Components
Dependencies: The script uses the pynput library, which provides functions for monitoring and controlling input devices like keyboards.
Variables:
key_list: A list used to store the keys pressed by the user.
Functions:
key_pressed(key): This function is called whenever a key is pressed. It appends the pressed key to the key_list and calls the log_keys() function.
key_released(key): This function is called whenever a key is released. If the pressed key is the escape key, it stops the keylogging process.
log_keys(list_of_keys): This function logs the keys stored in list_of_keys into the log.txt file. It iterates through each key, converts it to a string, removes any single quotes, prints it, and writes it to the log file. Finally, it clears the list_of_keys after logging.
Main Logic:
The script sets up a listener using keyboard.Listener from the pynput library. It starts the listener with listener.join(), which waits for the listener to stop.
Usage
Installation: Make sure you have Python installed on your system. Install the pynput library using pip install pynput.
Execution: Run the script using python keylog.py or python3 keylog.py depending on your Python installation.
Termination: Press the escape key (Esc) to stop the keylogging process.
Note
This script is provided for educational purposes only. Ensure that you have permission to monitor keyboard inputs before using it in any environment.
