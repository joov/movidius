# yolo3-camera
Simple camera preview processed with Yolo3 

Based on [keras-yolo3 project](https://github.com/qqwweee/keras-yolo3/).

## Requirements

- Tensorflow
- Keras
- OpenCV / Numpy

> It's recommended to use `pip` to install the above packages.

## Setup

### Get the code

```console
$ git clone --recursive https://github.com/ctchuang/yolo3-camera.git
```

Do not forget `--resursive` option.

### Prepare Yolo3 model

Prepare `vendor/keras-yolo3/model_data/yolo.h5`.

```console
$ cd yolo3-camera/vendor/keras-yolo3/

$ wget https://pjreddie.com/media/files/yolov3-tiny.weights
$ python convert.py yolov3-tiny.cfg yolov3-tiny.weights model_data/yolo.h5

$ cd -
```

> Remember to visit [the original YOLO project](https://pjreddie.com/darknet/yolo/).

### Run it

```console
$ python run.py [-h]
```

You should see live yolo result like below:
![Example](doc/example.jpg)
