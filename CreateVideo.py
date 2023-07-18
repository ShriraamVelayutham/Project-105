import os
import cv2
path = "PRO-C105-Project-Images-main"
images = []
for i in os.listdir(path):
 name, ext = os.path.splitext(i)
if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
    file_name = path+"/"+i
    print(file_name)
    images.append(file_name)
count = len(images)
frame = cv2.imread(images(0))
height,width,channels = frame.shape
size = (width, height)
print(size)
out = cv2.VideoWriter('project avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(0, count-1):
 var = cv2.imread(images[i])
print("Done")