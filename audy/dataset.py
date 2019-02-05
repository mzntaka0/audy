# -*- coding: utf-8 -*-
"""
"""
from pathlib import Path

from torch.utils.data import Dataset
import torchaudio

from audy.exceptions import NotDesiredSampleRateError, AudioFileNotFoundError

__all__ = [
    'AudioDataset'
    ]


# TODO: Need to deal with not only source data but target data.
class AudioDataset(Dataset):
    """
    Audio dataset as training input

    Args:
        - audio_dir (str): The path for audios directory
        - transforms (list): list of transforms  # TODO: alternate to Compose
        - ext (str): expected extension of audio file
        - desirted_sr (str): desired sample rate of audio
    """
    _accepted_ext = [
        'wav',
        ]

    def __init__(self, audio_dir: str, transforms: list = list(),
                 ext: 'str' = 'wav', desired_sr: int = 16000):
        super().__init__()
        self.audio_Dir = Path(audio_dir)
        self._audios = list(self.audio_Dir.glob('*.{}'.format(ext)))
        if not self._audios:
            raise AudioFileNotFoundError(
                "Any Audio File has not been found. Please select directory containing audios as audio_dir.")
        self._ext = ext
        self.transforms = transforms
        self.sample_rate = desired_sr

    def __len__(self):
        return len(self._audios)

    def __getitem__(self, idx: int):
        audio_Path = self._audios[idx]
        audio, sample_rate = torchaudio.load(str(audio_Path))  # ([L x C], sample_rate)
        self._sr_validation(sample_rate)

        for transform in self.transforms:
            audio = transform(audio, sample_rate)
        return audio

    def _sr_validation(self, sample_rate):
        if not sample_rate == self.sample_rate:
            raise NotDesiredSampleRateError


if __name__ == '__main__':
    import audy
    audio_dir = '../tests/assets/'
    audio_dataset = audy.AudioDataset(audio_dir, ext='str')
    audio_dataset[0]
