# YOLOv5 requirements
# Usage: pip install -r requirements.txt

gitpython
ipython  # interactive notebook
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.1.1
Pillow>=7.1.2
psutil
PyYAML>=5.3.1
requests>=2.23.0
scipy>=1.4.1
thop>=0.1.1  # FLOPs computation
torch>=1.7.0  # see https://pytorch.org/get-started/locally (recommended)
torchvision>=0.8.1
tqdm>=4.64.0
tensorboard>=2.4.1
pandas>=1.1.4
seaborn>=0.11.0

I am also creating a way you can install torch online.
You have to go on the following website 

https://pytorch.org/get-started/previous-versions/
and select torch 1.10.0
if you are using a cuda device that has gpu you install cuda 10.2 version
other wise install cpu only version

This is a read me file which will help you run the code on images and also validate our acuuracy levels for method 2 

1. For detection you have do the following

python detect.py --weights best.pt --source "path to the image"

2. For evalualtion you have do the following

python val.py --weights best.pt --data coco128.yaml --img 640
for changing of dataset for testing you can change the location in coco128.yaml file located in the data folder.

The following are the requirements for the code to run

We have stored the following in the runs file
1. train folder: contains all path creted during the training 
2. detect folder which shows the results on the test images 
3. val folder which shows evaluation of the test images in which we got a map of .9820 for method 2.