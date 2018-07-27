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
$ wget https://pjreddie.com/media/files/yolov3.weights
$ python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
```

### Run it

```console
$ python run.py [-h]
```

You can see live yolo result like
![Example](doc/example.jpg
)
