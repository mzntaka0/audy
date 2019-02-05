# -*- coding: utf-8 -*-
"""
"""
import argparse
import os
import sys
import glob

import librosa


class Mixer(object):

    def __init__(self, root, loader, extensions, transform=None, target_transform=None):
        self.root = root
        self.audio_list = glob.glob(os.path.join(root, *))

    def load(self, audio_path):
        pass

    @staticmethod
    def get_args():
        pass

    
