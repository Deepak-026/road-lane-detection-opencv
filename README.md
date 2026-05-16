# 🚗 Road Lane Detection using OpenCV

## 📌 Overview
This project implements a **real-time road lane detection system** using classical
computer vision techniques with OpenCV. The system is designed to identify lane
boundaries accurately under varying lighting conditions, shadows, and road noise,
making it suitable for autonomous driving research and Advanced Driver Assistance Systems (ADAS).

The pipeline processes live webcam feeds or prerecorded driving footage with
**low-latency inference** and modular vision components.

---

## ✨ Features
- Real-time lane detection on video streams
- Robust edge detection and noise suppression
- Dynamic Region of Interest (ROI) masking
- Lane curvature visualization
- Stable lane tracking using temporal averaging
- Supports webcam and prerecorded video input
- Optimized for low computational overhead
- Modular and scalable pipeline design

---

## 🧠 Computer Vision Pipeline

### 1️⃣ Image Preprocessing
- RGB → Grayscale conversion
- Gaussian Blur for noise reduction
- Contrast enhancement for low-light robustness

### 2️⃣ Edge Detection
- Canny Edge Detection to extract lane boundaries
- Adaptive threshold tuning for varying environments

### 3️⃣ Region of Interest (ROI) Masking
- Removes irrelevant regions such as sky, vehicles, and roadside objects
- Focuses computation on the drivable lane area only

### 4️⃣ Hough Line Transform
- Detects lane candidate lines efficiently
- Handles discontinuous lane markings

### 5️⃣ Lane Estimation & Visualization
- Slope-based lane classification
- Lane averaging and smoothing across frames
- Overlay visualization on original video feed

---

## ⚡ Performance Highlights
- Processes video in **real-time (30+ FPS)** on standard hardware
- Low-latency inference optimized using NumPy vectorization
- Robust against:
  - Shadows
  - Road texture noise
  - Illumination changes
  - Partial lane occlusions

---

## 📊 Results
The system successfully detects:
- Straight lanes
- Curved roads
- Dashed lane markings
- Multi-lane highways

Temporal smoothing ensures stable lane tracking across continuous video frames.

---

# 💻 Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)

---

## 📂 Project Structure

```bash
├── run.py
├── requirements.txt
├── notebook/
│   └── lane-detection-cv.ipynb
├── outputs/
├── src/
│   ├── preprocessing.py
│   ├── edge_detection.py
│   ├── roi.py
│   ├── lane_detection.py
│   └── visualization.py
```

---

## ▶️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

### Run using Webcam

```bash
python run.py --source 0
```

### Run using Video File

```bash
python run.py --source path/to/video.mp4 --output outputs/result.mp4
```

---

## 📓 Jupyter Notebook Demo

Open the interactive notebook:

```bash
notebook/lane-detection-cv.ipynb
```

---

## 🚀 Future Improvements
- Deep Learning-based lane segmentation
- Perspective Transform (Bird’s Eye View)
- Lane Departure Warning System
- ROS integration for autonomous robotics
- GPU acceleration using CUDA/OpenCV

---

## 📸 Demo Preview
_Add screenshots or GIFs here for better visualization._

---

## 🤝 Contributions
Pull requests and improvements are welcome. Feel free to fork the repository and experiment with advanced computer vision techniques.

---

## 📜 License
This project is open-source and available under the MIT License.
