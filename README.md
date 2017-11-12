# NoisePy ~ a random noise generator ####

__NoisePy__ generates a random noise image, based on given dimension  and 
black ratio

this is still in **development**, for better usage options, arguments, direct file save and more will follow

__Requirements__:

+ Python3
+ pip3

__Dependencies__ (will be installed during installation):
+ numpy
+ scipy

__Installation__:
```commandline
sudo -H pip3 install -e git+https://github.com/lymbycfyk/noisepy.git
```

or

```commandline
sudo -H pip3 install noisepy
```

__Usage__:
```commandline
$ python3 -m noisepy
image width(pixel): 800
image height(pixel): 600
black ratio(0.X): 0.66
```
or
```commandline
$ python3 -m noisepy -c 800 -r 600 -b 0.66
```

![example](https://imgur.com/t6xUDyL "example image")

__Help__:
```commandline
$ python3 -m noisepy -h
  Usage: python3 -m noisepy [options] arg1 arg2 arg3

  Options:
    --version             show program's version number and exit
    -h, --help            show this help message and exit
    -r HEIGHT, --rows=HEIGHT
                          set height of image
    -c WIDTH, --columns=WIDTH
                          set width of image
    -b RATIO, --black=RATIO
                          set black ration
```
