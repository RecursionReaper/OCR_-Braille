# 📜 Bold Text to Braille Converter

This project captures bold text from a webcam, processes it using OpenCV for optimal OCR accuracy, extracts the text with Tesseract OCR, and converts it to Braille using a predefined dictionary. The future goal is to integrate a **micro servo motor system** to emboss the Braille output onto a tactile surface, making the text physically readable.

## 🚀 Features
- ✅ **Optimized Preprocessing** → Uses **Otsu's thresholding** and **morphological operations** for better text detection on white backgrounds.
- ✅ **Noise Reduction** → Removes small artifacts and enhances contrast.
- ✅ **OCR Tuning** → Uses `--psm 6` for paragraph-level recognition and limits detected characters to English letters.
- ✅ **Braille Conversion** → Converts extracted text into Braille symbols.
- ✅ **Debug Mode** → Saves intermediate images (`grayscale`, `binary`, `denoised`, `enlarged`) for troubleshooting.
- ✅ **Future Physical Braille Output** → Planned integration with a **servo-based embossing system**.

---

## 📌 How It Works
### **1️⃣ Image Processing Pipeline**
1️⃣ **Convert to Grayscale** → Converts image to **black & white**.  
2️⃣ **Thresholding (Otsu's)** → Segments text from background.  
3️⃣ **Morphological Operations** → Removes noise and enhances text edges.  
4️⃣ **Upscaling** → Enlarges the image for better OCR accuracy.  
5️⃣ **OCR Extraction** → Detects text using **Tesseract** with `--psm 6`.  
6️⃣ **Braille Conversion** → Converts extracted text to Braille characters.  

### **2️⃣ Text Capture Instructions**
- 📌 Hold the text **20-30 cm away** from the camera.  
- 📌 Ensure **even lighting** (avoid shadows).  
- 📌 Use **bold text (size 48+)** on a **plain white background**.  
- 📌 Press **'s'** to capture and convert text.  
- 📌 Press **'q'** to exit the program.  

---

## 📜 Applications
This project is useful in various accessibility and assistive technologies, including:
- 🔹 **Education for the Visually Impaired** → Helps convert printed or digital text into tactile Braille.
- 🔹 **Instant Braille Translation** → Captures and converts text in real-time using a webcam.
- 🔹 **Smart Reading Devices** → Can be integrated into reading devices for the blind.
- 🔹 **Automated Braille Printers** → Future goal is to control a micro servo motor system that embosses the detected Braille onto a tactile surface.

---

## 🏗 Future Developments
- 🔹 **Micro Servo-Based Braille Output** → Utilize a servo array to emboss Braille on paper or a refreshable tactile display.
- 🔹 **Support for More Languages** → Enhance Tesseract OCR for multilingual recognition.
- 🔹 **Advanced AI-based OCR** → Train a deep learning model for better text recognition accuracy.
- 🔹 **GUI-based Interface** → Make the application more user-friendly.
- 🔹 **Handwritten Text Support** → Enhance processing to work with handwritten documents.

---

## 🖼 Debugging & Logs
📂 If `DEBUG_MODE = True`, the script saves intermediate images in `debug_images/` for analysis.

---

## 📜 Example Output
```
=== RESULTS ===
Detected Text: FIELD PROJECT
Braille Equivalent: ⠋⠊⠑⠇⠙ ⠏⠗⠕⠚⠑⠉⠞

<img width="1284" alt="image" src="https://github.com/user-attachments/assets/8ebdefc3-5b29-481a-b316-cfba707f355a" />


```

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

