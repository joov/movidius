---
@title[Introduction]

## Movidius Neural Network Stick

### USB-Stick auf Basis von Intel's Myriad-X-Chip

---
@title[Inhalt]

---?image=https://software.intel.com/sites/default/files/managed/e8/20/NCS-banner-MovStick-500w-300h.png

### Inhalt

1. Was tut der Movidius-Stick
1. Funktionsweise
1. Einrichten auf dem RPI
1. Coding-Beispiel
1. Ausblick


---
@title[Machine Learning]

### Zwei Phasen des Machine Learning

![Neural Network](http://uc-r.github.io/public/images/analytics/deep_learning/deep_nn.png)

+++

#### Phase 1: Training

- Ermittlung von Gewichten des NN
- Basis: Markierter Datensatz von Testdaten

Beispiel: [COCO Dataset](http://cocodataset.org/#explore)

#### Phase 2: Running

- Einspielen von Echtdaten
- Ablesen von Ergebnissen

---
@title[Movidius - Eigenschaften]

### Eigenschaften des Movidius-Sticks

1. Hilft nur in Phase 2 (Running)
1. Beschränkt auf Video-Anwendungen
1. Geringer Fußabdruck (klein, ca. 1W, USB)
1. Beschränkte Ressourcen im Stick

---
@title[Beispiele]

### Anwendungsbeispiele

[AppZoo](https://github.com/movidius/ncappzoo) enthält Beispielprojekte

- [Apps](https://github.com/movidius/ncappzoo/blob/master/apps/README.md)
- [Caffee](https://github.com/movidius/ncappzoo/blob/master/caffe/README.md)
- [tensorflow](https://github.com/movidius/ncappzoo/blob/master/tensorflow/README.md)

---
@title[Installation]

### Installation auf RPI

- Basis: Raspbian Desktop (z.B. über [Noobs](https://www.raspberrypi.org/downloads/noobs/) installiert)
- Installation [Movidius-SDK](https://software.intel.com/en-us/neural-compute-stick/get-started)
- Installation python-dependencies (`opencv`, `picamera[array]`) mit `pip3`

---
@title[Installation-2]

- Clone von diesem Projekt mit `--recurse`-Option
- cd to `./vendor/YoloV2NCS`
- `make -j4`
- Compile Model `mvNCCompile ./models/caffemodels/yoloV2Tiny20.prototxt -w ./models/caffemodels/yoloV2Tiny20.caffemodel -s 12`

@title[Code]

---?gist=https://gist.github.com/joov/9c4592e380065bc415ed3bda329f78f3&lang=python&title=Outer Loop
@[3-5]
@[15-22]

#### Outer Loop

---?gist=https://gist.github.com/joov/f33fb754236063044bab3d91d218e39c&lang=python&title=Open Device
@[2-4]

#### Open Device

---
@title[Run]

### Run

start `run.sh` in root of project

---
@title[Ausblick]

### Ausblick

#### Kamera

- [Aviglion-Kamera](http://news.avigilon.com/News-Releases/News-Release-Details/2018/Avigilon-to-Provide-First-Look-of-AI-Powered-H5-Camera-Line-at-GSX-2018/default.aspx)
- [FLIR-Kamera](https://groupgets.com/manufacturers/flir/products/boson)

#### Andere Prozessoren

- [Intel Nervana](https://ai.intel.com/nervana-nnp/)
- [Andere Produkte](https://en.wikipedia.org/wiki/AI_accelerator#Stand_alone_products)
  - GPUs
  - Handy-Prozessoren
  - DSPs
  - *etc.*
