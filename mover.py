import pyautogui
import time

print("Mouse mover started. Press Ctrl+C to stop.")

try:
    while True:
        # Get current mouse position
        x, y = pyautogui.position()

        # Move slightly and back
        pyautogui.moveTo(x + 10, y + 10, duration=0.5)
        pyautogui.click()
        pyautogui.moveTo(x, y, duration=0.5)

        print(f"Moved and clicked at {time.strftime('%H:%M:%S')}")

        # Wait 1 minute
        time.sleep(60)

except KeyboardInterrupt:
    print("\nStopped.")
