#################################################
### Script will convert all .FLAC files in a  ###
###   given directory to .MP3 and deposit     ###
###   them into a separate directory.         ###
### Author:   Brian Meyer                     ###
### Language: Python                          ###
### Tool:     ffmpeg                          ###
### Creation Date: 2025-09-15                 ###
### List of post-release updates:             ###
###    -                                      ###
###    -                                      ###
#################################################


#!/usr/bin/env python3
import os
import subprocess

# Paths
SRC = "/mnt/user/media/media_files/_FLAC"
DST = "/mnt/user/media/media_files/flac_to_mp3"

# ffmpeg binary
FFMPEG = "/usr/local/bin/ffmpeg/ffmpeg"

# Walk through source tree
for root, dirs, files in os.walk(SRC):
    for file in files:
        if file.lower().endswith(".flac"):
            infile = os.path.join(root, file)
            relpath = os.path.relpath(infile, SRC)  # relative path
            outfile = os.path.join(DST, os.path.splitext(relpath)[0] + ".mp3")

            outdir = os.path.dirname(outfile)
            os.makedirs(outdir, exist_ok=True)

            if not os.path.exists(outfile):
                print(f"Converting: {infile} -> {outfile}")
                subprocess.run([
                    FFMPEG, "-i", infile,
                    "-ab", "320k",
                    "-map_metadata", "0",
                    "-id3v2_version", "3",
                    outfile
                ], check=True)
            else:
                print(f"Skipping (already exists): {outfile}")
