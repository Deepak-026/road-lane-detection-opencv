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
Install dependencies and run the example runner. The runner accepts a webcam (default) or a video file.

```bash
pip install -r requirements.txt
python run.py --source 0                # run webcam
python run.py --source path/to/video.mp4 --output outputs/result.mp4
```

Alternatively open the demo notebook at `notebook/lane-detection-cv.ipynb`.
