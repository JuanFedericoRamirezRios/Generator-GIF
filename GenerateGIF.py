"""
 * Python 3.11

 * GPL-3.0 license
"""
path = "./"
extension = ".png"
sort = True
out="outGif.gif"
duration = 100
loops = 0

from PIL import Image
import os
import typing
import argparse as ar

def ObtainFrames(path = path, extension = extension, sort = sort) -> typing.List[typing.Any] | None:
    if not os.path.exists(path):
        print("Error:", path, "not exist.")
        return None

    fileNames = [fileName for fileName in os.listdir(path) if fileName.endswith(extension)]
    if sort: fileNames.sort()
    # print(fileNames)
    return [Image.open(os.path.join(path, fileName)) for fileName in fileNames]
def SaveGIF(frames, outFilePath=out, duration = duration, loops = loops) -> None:
    """
    loops: If loops = 0 -> indefinitely
    duration: in ms.
    """
    frames[0].save(outFilePath, save_all=True, append_images=frames[1:], optimize=True, duration=duration, loop=loops) # optimize=True: optimize the size of file.

if __name__ == "__main__":
    args = ar.ArgumentParser(description="Convert images to .gif")
    args.add_argument("-p", "--path", type=str, help="Path of input images. By default: ./")
    args.add_argument("-e", "--extension", type=str, help="Extesion of input images. By default: .png")
    args.add_argument("-s", "--sort", type=str, help="Sort input images: y|n. By default: y")
    args.add_argument("-o", "--out", type=str, help="Out file. By default: outGif.gif")
    args.add_argument("-d", "--duration", type=int, help="Duration in ms of each frame. By default: 100")
    args.add_argument("-l", "--loops", type=int, help="Loops. By default: 0 (indefinitely)")

    args = args.parse_args()

    if args.path: path = args.path # if arg.path != None
    if args.extension: extension = args.extension
    if args.sort:
        if args.sort == "n":
            sort = False
    if args.out: out = args.out
    if args.duration: duration = args.duration
    if args.loops: loops = args.loops

    frames = ObtainFrames(path, extension, sort)
    if frames == None: exit()
    if len(frames) < 2:
        print("Error: one or no images")
        exit()

    SaveGIF(frames, out, duration, loops)

