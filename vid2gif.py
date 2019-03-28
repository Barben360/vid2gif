#!/usr/bin/env python3

import argparse
import ffmpeg
import os
import shutil


def vid2gif(src, dst, scale="", start_time=-1.0, stop_time=-1.0, fps=-1):

    # ffmpeg -y -i in.mp4 -t 30 -filter_complex "fps=10,scale=-1:-1:flags=lanczos[x];[0:v]palettegen[y];[x][y]paletteuse" out.gif
    stream = ffmpeg.input(src)
    if fps >= 1:
        stream = ffmpeg.filter(stream, 'fps', fps)
    if scale.size() > 0:
        stream = ffmpeg.filter(stream, 'scale', scale)
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create a small and clean GIF from a video')

    parser.add_argument('src', metavar='SRC', help='source video file')
    parser.add_argument('dst', metavar='DST', help='destination GIF file')
    parser.add_argument('--resize', dest='resize', type=float, nargs=1, default=-1.0,
                        help='resize output (e.g: --resize 0.7 decreases video size by 30%)')
    parser.add_argument('--set-size', dest='set_size', nargs=1,
                        help='set output size (e.g: --set-size 500:400 sets height to 500px and width to 400px, and --set-size 500:-1 sets height to 500px and keeps aspect ratio)')
    parser.add_argument('--start-time', dest='start_time',
                        type=float, default=-1.0, help='set start time in seconds')
    parser.add_argument('--stop-time', dest='stop_time',
                        type=float, default=-1.0, help='set stop time in seconds')
    parser.add_argument('--fps', dest='fps', type=int, default=-1,
                        help='set framerate in frames per second')

    args = parser.parse_args()

    if resize > 0 and set_size > 0:
        print("Error: resize and set_size can't be used in the same time")
        exit
    scale = ""
    if resize > 0:
        scale=""
    elif set_size > 0:
        

    vid2gif(args.src, args.dst, ,
            args.start_time, args.stop_time, args.fps)
