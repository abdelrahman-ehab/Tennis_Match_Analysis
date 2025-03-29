# Tennis_Match_Analysis

A computer vision project to analyze tennis matches in real-time, tracking players, detecting the ball, and calculating gameplay metrics using **YOLOv8**, **YOLOv5 (custom-trained)**, and **OpenCV**. Includes a live court map and an analytics dashboard for speed analysis.

## 🚀 Features
- **Player Detection**: Real-time player tracking using **YOLOv8x**.
- **Ball Detection**: Custom-trained YOLOv5 model with **interpolation** for accurate fast-moving ball detection.
- **Court Mapping**: Pixel-based court detection to map player and ball positions.
- **Live Analytics Dashboard**: 
  - Ball speed (km/h) and player speed (km/h) per frame.
  - Real-time trajectory visualization.
- **Tools**: Perspective transformation, frame interpolation, and coordinate mapping.

## 🛠 Technologies Used
- **YOLOv8x** (pre-trained) for player detection.
- **YOLOv5** (custom-trained on tennis ball dataset) for ball detection.
- **OpenCV** for video processing, court detection, and visualization.
- **NumPy** & **Pandas** for data handling.
- **Matplotlib** for analytics visualization.
