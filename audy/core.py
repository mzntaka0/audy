# -*- coding: utf-8 -*-
"""
"""

import librosa
from pathlib import Path

__all__ = [
    'load'
    ]


def load(audio_path, sr=16000, mono=False):
    audio, sr = librosa.load(audio_path, sr=sr, mono=mono)
    return audio, sr


def load_dir(audio_dir, sr=16000, mono=False, ext='wav'):
    audio_Dir = Path(audio_dir)
    audios = audio_Dir.glob('*.{}'.format(ext))
