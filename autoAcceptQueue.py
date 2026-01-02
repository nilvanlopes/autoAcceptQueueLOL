# %%
# Import Required Libraries
import pyautogui
import time
import os
import sys

# %%
# Function: Return the path where is located this script or exe
def exe_dir():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

# %%
# Function: Find Image on Screen
def find_image(filename, confidence=0.9):
    """
    Locate an image on the screen using computer vision.
    
    Parameters:
    -----------
    filename : str
        Path to the image file to search for
    confidence : float, optional
        Confidence level (0.0 to 1.0) required for a match. Default is 0.9
        
    Returns:
    --------
    tuple or None
        Returns (x, y) coordinates if image is found, None otherwise
    """
    try:
        img = os.path.join(exe_dir(), "popup.png")
        position = pyautogui.locateOnScreen(img, confidence=confidence)
        return position
    except Exception as e:
        print(f"Error finding image: {e}")
        return None

# %%
# Function: Main Monitoring Loop
def main():
    """
    Main function that continuously monitors the screen for the target image.
    Plays an alarm sound when the image is detected.
    """
    filename = 'popup.png'  # Change to your image path
    confidence = 0.9  # Adjust confidence as needed

    while True:
        position = find_image(filename, confidence)
        if position:
            print("Image found!")
            pyautogui.moveTo(position)
            pyautogui.click(position)
            break  # Exit loop when image is found
        else:
            print("Image not found. Waiting...")
            time.sleep(1)  # Wait 1 second before trying again

# %%
# Execute Main Function
if __name__ == "__main__":
    main()


