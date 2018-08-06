# Setup Darknet

## Steps

```console
$ cd yolo3-camera/vendor/darknet

$ make -j4

$ wget https://pjreddie.com/media/files/yolov3-tiny.weights

# Test
$ ./darknet detect cfg/yolov3-tiny.cfg yolov3-tiny.weights data/person.jpg

```