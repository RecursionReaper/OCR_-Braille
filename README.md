# OCR_-Braille
Develop a system that captures text input using a camera, converts it into Braille, and represents the Braille characters using servo motors, allowing visually impaired individuals to feel the text.

# 📜 Bold Text to Braille Converter

This project captures bold text from a webcam, processes it using OpenCV for optimal OCR accuracy, extracts the text with Tesseract OCR, and converts it to Braille using a predefined dictionary.

## 🚀 Features
- ✅ **Optimized Preprocessing** → Uses **Otsu's thresholding** and **morphological operations** for better text detection on white backgrounds.
- ✅ **Noise Reduction** → Removes small artifacts and enhances contrast.
- ✅ **OCR Tuning** → Uses `--psm 6` for paragraph-level recognition and limits detected characters to English letters.
- ✅ **Braille Conversion** → Converts extracted text into Braille symbols.
- ✅ **Debug Mode** → Saves intermediate images (`grayscale`, `binary`, `denoised`, `enlarged`) for troubleshooting.

---

## 🛠 Installation
### **1️⃣ Prerequisites**
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Tesseract OCR
- Webcam (built-in or external)

### **2️⃣ Install Dependencies**
```sh
pip install opencv-python numpy pytesseract
```

### **3️⃣ Install Tesseract OCR**
#### **Mac (Homebrew)**
```sh
brew install tesseract
```
#### **Ubuntu**
```sh
sudo apt update && sudo apt install tesseract-ocr -y
```
#### **Windows**
1. Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract)
2. Add Tesseract to system PATH.

---

## 📌 Usage
### **Run the script**
```sh
python main.py
```

### **Controls**
- **Press 's'** → Capture text
- **Press 'q'** → Quit the program

### **Instructions for Best Results**
- 📌 Hold the text **20-30 cm away** from the camera.  
- 📌 Ensure **even lighting** (avoid shadows).  
- 📌 Use **bold text (size 48+)** on a **plain white background**.  

---

## 🖼 Image Processing Pipeline
1️⃣ **Convert to Grayscale** → Converts image to **black & white**.  
2️⃣ **Thresholding (Otsu's)** → Segments text from background.  
3️⃣ **Morphological Operations** → Removes noise and enhances text edges.  
4️⃣ **Upscaling** → Enlarges the image for better OCR accuracy.  
5️⃣ **OCR Extraction** → Detects text using **Tesseract** with `--psm 6`.  
6️⃣ **Braille Conversion** → Converts extracted text to Braille characters.  

---

## 🏗 Debugging & Logs
📂 If `DEBUG_MODE = True`, the script saves intermediate images in `debug_images/` for analysis.

---

## 📜 Example Output
```
=== RESULTS ===
Detected Text: FIELD PROJECT
Braille Equivalent: ⠋⠊⠑⠇⠙ ⠏⠗⠕⠚⠑⠉⠞
```

---

## 🛠 Future Improvements
- 🔹 Improve OCR accuracy for various fonts and sizes.  
- 🔹 Implement a GUI-based interface.  
- 🔹 Support multi-line Braille translation.  

---

## 🤝 Contributing
1. Fork the repository
2. Create a new branch (`feature-xyz`)
3. Commit changes (`git commit -m "Added new feature"`)
4. Push to the branch (`git push origin feature-xyz`)
5. Open a Pull Request 🚀

---

## 📜 License
This project is licensed under the **MIT License**.




<img width="1284" alt="image" src="https://github.com/user-attachments/assets/6c76770b-e3a7-4f39-90a0-c1b81c35a233" />
