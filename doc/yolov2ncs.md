# Setup YoloV2NCS

## Requirements

- [Intel Movidius NCS USB stick](https://developer.movidius.com/buy)
- The SDK only supports Linux.

## Steps

1. Install [NCS SDK](https://github.com/movidius/ncsdk)

> Remember to use `-b ncsdk2` in `git clone` so you won't get old v1 SDK.

2. Install OpenCV

Because we're using Python3, but Ubuntu doesn't have OpenCV apt package for Python3, you can use `pip3 install opencv-python` or the 

3. Build YoloV2NCS

```console
$ cd yolo3-camera/vendor/YoloV2NCS
$ make -j4
```

4. Convert Caffe model to Movidius NCS model

```console
$ mvNCCompile ./models/caffemodels/yoloV2Tiny20.prototxt -w ./models/caffemodels/yoloV2Tiny20.caffemodel -s 12
```

5. Verify if it works for single image

```console
$ python3 ./detectionExample/Main.py --image ./data/dog.jpg
```
