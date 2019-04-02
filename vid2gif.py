#!/usr/bin/env python3

import argparse
import ffmpeg
import os
import shutil
import sys


def vid2gif(src, dst, output_width="-1", output_height="-1", start_time=-1.0, stop_time=-1.0, fps=-1):

    # ffmpeg -y -i in.mp4 -t 30 -filter_complex "fps=10,scale=-1:-1:flags=lanczos,split[x][y];[x]palettegen[z];[y][z]paletteuse" out.gif
    in_stream = ffmpeg.input(src, ss=start_time, t=(stop_time-start_time))
    scale_input = in_stream
    if fps >= 1:
        stream = ffmpeg.filter(in_stream['v'], 'fps', fps)
        scale_input = stream

    stream = ffmpeg.filter(scale_input, 'scale', output_width, output_height, 'lanczos')
    
    palette = ffmpeg.filter(in_stream['v'], 'palettegen')
    stream = ffmpeg.filter(stream, palette, 'paletteuse')
    stream = stream.overwrite_output(dst, format='gif')
    print(ffmpeg.compile(stream))
    ffmpeg.run(stream,overwrite_output=True)
    ffmpeg.run(palette)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Create a small and clean GIF from a video')

    parser.add_argument('src', metavar='SRC', help='source video file')
    parser.add_argument('dst', metavar='DST', help='destination GIF file')
    parser.add_argument('--resize', dest='resize', type=float, default=-1.0,
                        help='resize output (e.g: --resize 0.7 decreases video size by 30%)')
    parser.add_argument('--set-size', dest='set_size',
                        help='set output size (e.g: --set-size 500:400 sets height to 500px and width to 400px, and --set-size 500:-1 sets height to 500px and keeps aspect ratio)')
    parser.add_argument('--start-time', dest='start_time',
                        type=float, default=-1.0, help='set start time in seconds')
    parser.add_argument('--stop-time', dest='stop_time',
                        type=float, default=-1.0, help='set stop time in seconds')
    parser.add_argument('--fps', dest='fps', type=int, default=-1,
                        help='set framerate in frames per second')

    args = parser.parse_args()

    if args.resize > 0 and args.set_size:
        print("Error: resize and set_size can't be used in the same time")
        sys.exit(1)
    output_width = "-1"
    output_height = "-1"
    if args.resize and args.resize > 0.0:
        output_width = "iw*" + str(args.resize)
    elif args.set_size and len(args.set_size) > 0:
        if args.set_size.count(':') != 1:
            print("Error: --set-size format must be width:height")
            sys.exit(1)
        size_list = args.set_size.split(':')
        if len(size_list) != 2:
            print("Error: --set-size format must be width:height")
            sys.exit(1)
        output_width = size_list[0]
        output_height = size_list[1]

    vid2gif(args.src, args.dst, output_width, output_height,
            args.start_time, args.stop_time, args.fps)
