---?color=linear-gradient(to right, #c02425, #f0cb35)
@title[Introduction]

@snap[west headline text-white span-70]
Movidius<br>*Neural Network stick*
@snapend

@snap[south-west byline  text-white]
USB-Stick auf Basis von Intel's Myriad-X-Chip
@snapend

---
@title[Inhalt]

### Inhalt

---?image=https://software.intel.com/sites/default/files/managed/e8/20/NCS-banner-MovStick-500w-300h.png

1. Was tut der Movidius-Stick
1. Funktionsweise
1. Einrichten auf dem RPI
1. Coding-Beispiel
1. Ausblick
<br><br>

---
@title[Machine Learning]

# Zwei Phasen des Machine Learning

![Neural Network](http://uc-r.github.io/public/images/analytics/deep_learning/deep_nn.png)

## Phase 1: Training

- Ermittlung von Gewichten des NN
- Basis: Markierter Datensatz von Testdaten

[Beispiel: COCO Dataset](http://cocodataset.org/#explore)

## Phase 2: Running

- Einspielen von Echtdaten
- Ablesen von Ergebnissen

---
@title[Movidius - Eigenschaften]

# Eigenschaften des Movidius-Sticks

1. Hilft nur in Phase 2 (Running)
1. Beschränkt auf Video-Anwendungen
1. Geringer Fußabdruck (klein, 1W Verbrauch, universell einsetzbar)
1. Beschränkte Ressourcen im Stick

---
@title[Beispiele]

# Anwendungsbeispiele

[AppZoo](https://github.com/movidius/ncappzoo) enthält Beispielprojekte

- [Apps](https://github.com/movidius/ncappzoo/blob/master/apps/README.md)
- [Caffee](https://github.com/movidius/ncappzoo/blob/master/caffe/README.md)
- [tensorflow](https://github.com/movidius/ncappzoo/blob/master/tensorflow/README.md)

---
@title[Installation]

# Installation auf RPI

- Basis: Raspbian Desktop (z.B. über [Noobs](https://www.raspberrypi.org/downloads/noobs/) installiert)
- Installation [Movidius-SDK](https://software.intel.com/en-us/neural-compute-stick/get-started)
- Installation python-dependencies (`opencv`, `picamera[array]`) mit `pip3`
- Clone von diesem Projekt mit `--recurse`-Option
- cd to `yolo3-camera/vendor/YoloV2NCS`
- `make -j4`
- Compile Model `mvNCCompile ./models/caffemodels/yoloV2Tiny20.prototxt -w ./models/caffemodels/yoloV2Tiny20.caffemodel -s 12`

@title[Code]

# Code

## Outer Loop

---?gist=https://gist.github.com/joov/9c4592e380065bc415ed3bda329f78f3&lang=python&title=Outer Loop
@[3-5]
@15-22]

## Open Device

---?gist=https://gist.github.com/joov/f33fb754236063044bab3d91d218e39c&lang=python&title=Open Device
@[2-4]

---
@title[Run]

# Run

start `run.sh` in root of project

---
@title[Ausblick]

# Ausblick

## Kamera

- [Aviglion-Kamera](http://news.avigilon.com/News-Releases/News-Release-Details/2018/Avigilon-to-Provide-First-Look-of-AI-Powered-H5-Camera-Line-at-GSX-2018/default.aspx) mit AI-Chip
- [FLIR-Kamera](https://www.invision-news.de/fachartikel/inferenz-an-der-edge/)
## Andere Prozessoren

- [Intel Nervana](https://ai.intel.com/intel-nervana-neural-network-processor-architecture-update/)
- [GPUs und andere Produkte](https://en.wikipedia.org/wiki/AI_accelerator#Stand_alone_products)