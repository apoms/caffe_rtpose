#!/usr/bin/env python
import numpy as np
import os
import sys
import argparse
import glob
import time
import subprocess

RTPOSE_PROGRAM_PATH = './build/examples/rtpose/rtpose.bin'

def run_rtpose(video_path, start_frame, end_frame, num_gpus):
    print('Running rtpose: {}, range: {}-{}, gpus: {}'.format(
        video_path,
        start_frame,
        end_frame,
        num_gpus))
    current_env = os.environ.copy()
    start = time.time()
    p = subprocess.Popen([
        RTPOSE_PROGRAM_PATH,
        '--video', video_path,
        '--start_frame', start_frame,
        '--end_frame', end_frame,
        '--no_frame_drops',
        '--no_display',
    ], env=current_env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    so, se = p.communicate()
    rc = p.returncode
    elapsed = time.time() - start
    return elapsed

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("video_paths_file")
    parser.add_argument("start_frame")
    parser.add_argument("end_frame")
    args = parser.parse_args()

    with open(args.video_paths_file, 'r') as f:
        paths = f.read().splitlines()

    for path in paths:
        run_rtpose(path, args.start_frame, args.end_frame, 1)


if __name__ == '__main__':
    main(sys.argv)
