# Road Lane Detection using OpenCV

## Overview
This project implements a real-time road lane detection system using classical
computer vision techniques in OpenCV. The system processes video streams to
detect lane boundaries under varying lighting and noise conditions.

## Features
- Real-time lane detection on video streams
- Robust edge detection and noise handling
- Modular vision pipeline design
- Optimized for low-latency inference

## Computer Vision Pipeline
1. Image preprocessing (grayscale, smoothing)
2. Canny edge detection
3. Region of Interest (ROI) masking
4. Hough Line Transform
5. Lane line averaging and visualization

## Tech Stack
- Python
- OpenCV
- NumPy
- Matplotlib

## How to Run
```bash
pip install -r requirements.txt
python notebook/Lane_Detection.ipynb  
