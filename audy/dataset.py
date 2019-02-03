# -*- coding: utf-8 -*-
"""
"""
import os
import sys
from pathlib import Path

from torch.utils.data import Dataset
import torchaudio


class AudioDataset(Dataset):
    """
    Audio dataset as training input

    Args:
        - audio_dir (str): The path for audios directory
        - transforms (list): list of transforms
    """
    _accepted_ext = [
        'wav',
        ]

    def __init__(self, audio_dir: str, transforms: list = None, ext: 'str' = 'wav'):
        self.audio_Dir = Path(audio_dir)
        self._audios = self.audio_Dir.glob('*.{}'.format(ext))
        self.transforms = transforms

    def __len__(self):
        return len(self._audios)

    def __getitem__(self, idx):
        audio_Path = self._audios(idx)
        audio, sample_rate = torchaudio.load(str(audio_Path))  # ([L x C], sample_rate)

        if transforms:
            for transform in transforms:
                pass






if __name__ == '__main__':
    audio_dir = 'data'
    audio_dataset = AudioDataset(audio_dir)
