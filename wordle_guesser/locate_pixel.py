import pyautogui
import time

print("Move your mouse to the desired position. The coordinates will be displayed in 5 seconds...")

# Wait a few seconds to allow you to move the mouse to the desired position
time.sleep(5)

# Get the current mouse position
x, y = pyautogui.position()

# Print the coordinates
print(f"The current mouse position is: ({x}, {y})")
