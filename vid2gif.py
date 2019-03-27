#!/usr/bin/env python3

import argparse
import tempfile
import ffmpeg
import os
import shutil


def vid2gif(src, dst, resize=1.0, set_size=-1.0, start_time=-1.0, stop_time=-1.0, fps=-1):
    # Checking if --resize and --set-size are not used in the same time
    if args.resize and args.set_size:
        print("Error: resize and set_size can't be used in the same time")
        exit

    # Creating temp folder to work into it
    palette_dir = tempfile.mkdtemp()
    current_dir = os.getcwd()
    palette_file = os.path.join(current_dir, palette_dir, "palette.png")
    print(palette_file)

    # TODO
    # stream = ffmpeg.input(src)
    # stream = ffmpeg.concat()
    # stream = ffmpeg.output(palette_file)

    # Removing temp folder
    shutil.rmtree(os.path.join(current_dir, palette_dir))


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

    vid2gif(args.src, args.dst, args.resize, args.set_size,
            args.start_time, args.stop_time, args.fps)
