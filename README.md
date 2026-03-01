# Generate GIF files from every image in a folder.

## Usage
GenerateGIF.exe [-h] [-p PATH] [-e EXTENSION] [-s SORT] [-o OUT] [-d DURATION] [-l LOOPS]

### Options:
- -h, --help &emsp; show this help message and exit
- -p PATH, --path PATH &emsp; Path of input images. By default: ./
- -e EXTENSION, --extension EXTENSION &emsp; Extesion of input images. By default: .png
- -s SORT, --sort SORT &emsp; Sort input images: y|n. By default: y
- -o OUT, --out OUT &emsp; Out file. By default: outGif.gif
- -d DURATION, --duration DURATION &emsp; Duration in ms of each frame. By default: 100
- -l LOOPS, --loops LOOPS &emsp; Loops. By default: 0 (indefinitely)

### Examples:
Run GenerateGIF.exe in the folder of images ExamplePNGs to generate OutGif.gif with indefinitely loop:

![Default example](ExamplePNGs/outGif.gif)

Images in the local folder ExamplePNGs, the extension of images is .png, no sort (sort by default) the output is ExampleGIF.gif, delay of each frame 50 ms and 2 loops:
- ./GenerateGIF -p ./ExamplePNGs -e .png -s n -o ExampleGIF.gif -d 50 -l 2

![Custom example](ExampleGIF.gif)

** The example of animation was made in Blender based on https://www.youtube.com/watch?v=OhzcCsR_EO0 **



