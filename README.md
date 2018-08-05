# yolo3-camera
Simple camera preview processed with Yolo3 

Work on Mac OS X and Linux.

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

### 1. Keras-based (doesn't require special hardware)

- [Setup keras_yolo3](doc/keras_yolo3.md)

### 2. Intel Movidius NCS hardware

- [Setup YoloV2NCS](doc/yolov2ncs.md)

## Run it

```console
$ python3 run.py [-h]
```

You should see live yolo result like below:
![Example](doc/example.jpg)

Press ESC key to exit.