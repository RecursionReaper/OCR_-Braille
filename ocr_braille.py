import cv2
import pytesseract
import numpy as np
from datetime import datetime
import os

# Configuration
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
DEBUG_MODE = True  # Set to True for debug images

# Braille Dictionary (English Letters)
braille_dict = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓',
    'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏',
    'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵', ' ': ' ', '.': '⠲', ',': '⠂', '?': '⠦', '!': '⠖', '-': '⠤'
}

def text_to_braille(text):
    """Converts detected text to Braille."""
    text = text.lower()
    return ''.join(braille_dict.get(char, char) for char in text)

def create_debug_folder():
    """Creates a debug folder for storing intermediate images."""
    if DEBUG_MODE:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        debug_path = os.path.join("debug_images", timestamp)
        os.makedirs(debug_path, exist_ok=True)
        return debug_path
    return None

def preprocess_image(image, debug_path=None):
    """Optimized image preprocessing for extracting bold text from a white page."""
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding to separate text from background
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Remove small noise (opening operation)
    kernel = np.ones((5, 5), np.uint8)
    denoised = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)

    # Enlarge text to improve OCR accuracy
    enlarged = cv2.resize(denoised, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    # Save debug images
    if debug_path:
        cv2.imwrite(f"{debug_path}/gray.jpg", gray)
        cv2.imwrite(f"{debug_path}/binary.jpg", binary)
        cv2.imwrite(f"{debug_path}/denoised.jpg", denoised)
        cv2.imwrite(f"{debug_path}/enlarged.jpg", enlarged)

    return enlarged

def capture_text():
    """Captures text from a webcam and applies OCR."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera access denied. Check permissions.")
        return

    print("\n=== INSTRUCTIONS ===")
    print("1. Hold text 20-30cm from the camera")
    print("2. Ensure even lighting (avoid shadows)")
    print("3. Press 's' to capture | 'q' to quit\n")

    debug_path = create_debug_folder()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Camera error")
            break

        cv2.imshow("Text Capture (Press 's')", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            # Save original image
            cv2.imwrite("original_capture.jpg", frame)

            # Preprocess image
            processed = preprocess_image(frame, debug_path)

            # Apply OCR with optimized settings
            text = pytesseract.image_to_string(
                processed,
                config='--psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
            ).strip()

            if DEBUG_MODE:
                print("\n=== DEBUG INFO ===")
                print(f"Image dimensions: {frame.shape}")
                print(f"Mean brightness: {np.mean(processed):.1f}")
                print(f"Extracted Text: {text}")

            if len(text) > 1:
                braille_text = text_to_braille(text)
                print("\n=== RESULTS ===")
                print(f"Detected Text: {text}")
                print(f"Braille Equivalent: {braille_text}")
            else:
                print("\nERROR: Text not detected clearly. Try:")
                print("- Increasing text size")
                print("- Improving lighting conditions")
                print("- Holding the camera steady")

            break
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_text()
