# yolo3-camera

Very simple camera preview processed with yolov3-tiny

## Credits

- [The original YOLO project](https://pjreddie.com/darknet/yolo/).
- [keras-yolo3 project](https://github.com/qqwweee/keras-yolo3/).
- [YoloV2NCS project](https://github.com/duangenquan/YoloV2NCS)

## Get the code

```console
$ git clone --recursive https://github.com/ctchuang/yolo3-camera.git
```

> Do not forget `--resursive` option.

## Decide the backend

### 1. Keras_Yolo3

Work on Mac OS X and Linux with CPU-only.

- [Setup keras_yolo3 backend](doc/keras_yolo3.md)

### 2. YoloV2NCS

Work on Linux with Intel Movidius NCS hardware.

- [Setup YoloV2NCS backend](doc/yolov2ncs.md)

## Run it

```console
# Use Keras backend
$ python3 run.py -b 0 

# Use YoloV2NCS
$ python3 run.py -b 1 
```

You should see live yolo result like below:
![Example](doc/example.jpg)

Press ESC key to exit.