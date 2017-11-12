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

    sudo -H pip3 install -e git+https://github.com/lymbycfyk/noisepy.git

__Usage__:

    $ python3 -m noisepy
    image width(pixel): 800
    image height(pixel): 600
    black ratio(0.X): 0.66

or

    $ python3 -m noisepy -c 800 -r 600 -b 0.66

![alt text][example_image]

__Help__:

    $ python3 -m nopisepy -h
    Usage: python3 -m nopisepy [options] arg1 arg2 arg3

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -r HEIGHT, --rows=HEIGHT
                            set height of image
      -c WIDTH, --columns=WIDTH
                            set width of image
      -b RATIO, --black=RATIO
                            set black ration


[example_image]: https://github.com/lymbycfyk/noisepy/blob/master/exmpl.png "noise example"
