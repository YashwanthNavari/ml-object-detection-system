<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=200&section=header&text=ML%20Object%20Detection%20System&fontSize=50&fontAlignY=38&animation=twinkling&desc=Real-Time%20YOLOv8%20Object%20Detection&descAlignY=60&descAlign=62" />

  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=24&pause=1000&color=00F0FF&center=true&vCenter=true&width=600&lines=Real-Time+YOLOv8+Object+Detection;Computer+Vision+%26+Deep+Learning;COCO-128+Dataset+Training" alt="Typing SVG" />
  </a>
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/YOLOv8-FF1493?style=for-the-badge&logo=yolo&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/Roboflow-0A2885?style=for-the-badge&logo=roboflow&logoColor=white" />
</div>

---

## 🌌 Introduction

The **ML Object Detection System** is an advanced computer vision project leveraging the cutting-edge **YOLOv8** (You Only Look Once) architecture for real-time, high-accuracy object detection. Integrated with OpenCV, this model performs rapid inference on live video feeds, correctly identifying and localizing multiple object classes simultaneously.

Trained on the **COCO-128** baseline dataset, the system demonstrates robust performance and real-world applicability in dynamic environments.

---

## ✨ Key Features

| Feature | Description |
| :--- | :--- |
| ⚡ **Real-Time Inference** | Connects to a standard webcam for instant, sub-millisecond object detection overlay. |
| 🧠 **State-of-the-Art CNN** | Utilizes the YOLOv8 Nano (`yolov8n.pt`) deep learning model for optimal speed-to-accuracy balance. |
| 📊 **Custom Training Pipeline** | Includes `train.py` for fine-tuning the model over custom epochs (default 10 epochs on `imagesz=640`). |
| 🔄 **Automated Data Retrieval** | Integrated `Roboflow` API pipeline (`download_data.py`) to easily pull massive datasets (e.g., COCO-2017). |

---

## 🛠️ Project Architecture

```mermaid
graph TD;
    A[Raw Data / Roboflow API] --> B(Data Ingestion);
    B --> C{YOLOv8 Training Pipeline};
    C -->|Output| D[best.pt Weights];
    D --> E[Real-time OpenCV Inference];
    F[Webcam/Video Feed] --> E;
    E --> G((Live Object Detections));
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YashwanthNavari/ml-object-detection-system.git
cd ml-object-detection-system
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Install the required libraries:
```bash
pip install ultralytics opencv-python roboflow
```

### 3. Run Real-Time Detection
With your webcam connected, launch the primary inference script:
```bash
python detect.py
```
> **Controls**: Press the `q` key inside the detection window to exit the stream securely.

### 4. Custom Model Training
To train the model from scratch on the configured datasets:
```bash
python train.py
```

---

## 💻 Tech Stack

<details>
<summary>Click to view robust technologies utilized</summary>

- **Language:** Python
- **Core Framework:** Ultralytics (YOLOv8)
- **Computer Vision:** OpenCV (`cv2`)
- **Dataset Management:** Roboflow API
- **Model Representation:** PyTorch (`.pt` weights)

</details>

---

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" />
</div>
