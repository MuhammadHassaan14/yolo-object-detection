# Real-Time Object Detection with YOLOv8

## Features

- Real-time object detection using webcam
- Static image detection mode
- Annotated outputs with bounding boxes and class labels
- Easy to use and lightweight (uses YOLOv8n - nano version)


## Folder Structure

project-folder/
│
├── main.py # Main Python script
├── image.jpg # Sample image for testing
├── README.md # This file
└── ...

## Installation

### 1. Clone the repository
git clone https://github.com/MuhammadHassaan14/yolo-object-detection.git
cd yolo-object-detection
2. Create virtual environment (optional but recommended)
go to cmd
write:
.\venv\Scripts\activate       #for Windows
source venv/bin/activate     #for macOS/Linux
3. Install dependencies
pip install ultralytics opencv-python
How to Use

Option 1: Real-Time Detection (Webcam)
python main.py
When prompted in terminal, type:
Choose mode: 
1. Real-time (webcam) 
2. Image detection
> 1
Press e to quit the webcam window (you can change the key by selecting the letter on line 34, if cv2.waitKey(1) & 0xFF == ord('e'):)

Option 2: Static Image Detection
Make sure image.jpg exists in the same folder, or replace it with your own.
python main.py
Then choose:
> 2
The result will be displayed in a window and saved as output.jpg.

