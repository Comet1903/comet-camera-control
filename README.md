# Comet Camera Control - CCC
Control you cursor via a Python skript

## How to use / Usage
### Usage
There is no reason why you should use this to control your cursor.

### How to use
Face your camera/webcam to a white sheet of paper. Face a black or dark object between the camera and the paper. For best results use a white pen with black tapt on the top.

## Setup
### Download and Install
```bash
git clone https://github.com/Comet1903/comet-camera-control
cd comet-camera-control
pip3 install -r requirements.txt
```
### Config
Depending on how much cameras are connected to your PC, you have to change the id of the camera. The easiest way to find your camera id is by trying them out. Start at 0 and end when you got the rigt camera
```python
vc = cv2.VideoCapture(0) # Replace 0 with you camera id
```
### Run it
```bash
python3 ccc.py
```
