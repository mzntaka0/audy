# -*- coding: utf-8 -*-
"""
"""

import librosa

__all__ = [
    'load'
    ]


def load(audio_path, sr=16000, mono=False):
    audio, sr = librosa.load(audio_path, sr=sr, mono=mono)
    return audio, sr
