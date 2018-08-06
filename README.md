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

## Pick a backend

### 1. Keras_Yolo3

- Backend: Keras + Tensorflow
- Platform:
	- Mac OS X 
	- Ubuntu Linux
	- Remark:
		- Running on Raspbian hits Bus Error in TensorFlow. I didn't debug it.
- AI Model: `yolov3-tiny`
- AI Hardware:
	- Pure CPU
	- GPU (haven't tested)
- [Setup keras_yolo3 backend](doc/keras_yolo3.md)

### 2. YoloV2NCS

- Backend: Intel Movidius SDK
- Platform:
	- Ubuntu Linux
	- Raspbian (Raspberry Pi 3)
    - Remark:
        - Movidius NCS SDK doesn't support Mac OS.
- AI Model: `yolov2-tiny-voc`
- AI Hardware:
	- Intel Movidius NCS USB stick.
- [Setup YoloV2NCS backend](doc/yolov2ncs.md)

### 3. Darknet

**Unfinished**

## Run it

Attach a camera.

```console
# Use Keras backend
$ python3 run.py -b 0 

# Use YoloV2NCS
$ python3 run.py -b 1 
```

You should see live yolo result like below:
![Example](doc/example.jpg)

Press ESC key to exit.

## Troubleshooting

Check camera is working.
```console
$ python3 test_camera.py
```

If camera is not working, check device number (Linux only)
```console
$ ls -l /dev/video*
```

You can use `-c [camera_index]` in `run.py` and `test_camera.py`.

Using USB camera + Movidius NCS on Raspberry Pi 3 together may have power issue
(RPi3 only gets 12W). Consider adding a powered USB 3.0 hub.
