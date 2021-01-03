import cv2
import os

#def num_to_char(num):

## opening the video
vidcap = cv2.VideoCapture('sample2.mp4')
fps_org = vidcap.get(cv2.CAP_PROP_FPS)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps_org))
## reading the first frame
success,image = vidcap.read()
count = 0
# loop to read each frame
while success:
  id=count+100000000000
  cv2.imwrite("frames/%d.jpg" % id, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  #print('Read a new frame: ', success)
  count += 1


print("frames read finished")
## after reading all frames generating noise
#exit()

## rewrite the video
image_folder = 'frames'
video_name = 'reassembled.mp4'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'),frameSize= (width,height),fps=fps_org)

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()


## delete recorded frames as jpg images
filelist = [ f for f in os.listdir(image_folder) if f.endswith(".jpg") ]
for f in filelist:
    os.remove(os.path.join(image_folder, f))