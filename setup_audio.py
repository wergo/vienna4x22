#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
Setup audio files for the Vienna4x22 dataset.
"""
import os
import glob
from shutil import copyfile
import argparse

# Download audio files from here!
# TODO: download files automatically
AUDIO_URL = (
    "http://repo.mdw.ac.at/projects/IWK/the_vienna_4x22_piano_corpus/data/audio.zip"
)

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

MIDI_DIR = os.path.join(CURRENT_DIR, "midi")
MATCH_DIR = os.path.join(CURRENT_DIR, "match")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        "Setup Audio recordings for the Vienna 4x22 dataset"
    )

    parser.add_argument(
        "--audio-dir",
        "-a",
        default=None,
        help="Path to the audio files",
    )

    args = parser.parse_args()

    if args.audio_dir is None:
        # download_file
        raise ValueError("Path to the audio files is required!")

    target_dir = os.path.join(CURRENT_DIR, "audio")

    if not os.path.join(target_dir):
        os.mkdir(target_dir)

    audiofiles = glob.glob(os.path.join(args.audio_dir, "*", "*.wav"))

    audiofiles.sort()

    for i, audio_fn in enumerate(audiofiles):

        piece = os.path.basename(audio_fn).replace(".wav", "")

        match_fn = os.path.join(MATCH_DIR, f"{piece}.match")
        target_audio_fn = os.path.join(target_dir, os.path.basename(audio_fn))
        # Ignore files for which there is no corresponding
        # match file (i.e., average, special takes...)
        # Only copy file if it does not exist already
        if os.path.exists(match_fn) and not os.path.exists(target_audio_fn):
            print(f"copying {audio_fn} to {target_audio_fn}...")
            copyfile(
                src=audio_fn,
                dst=target_audio_fn,
            )
        else:
            print(f"No corresponding match file for {audio_fn}!")
