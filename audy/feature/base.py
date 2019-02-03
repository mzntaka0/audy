# -*- coding: utf-8 -*-
"""
"""
import argparse
import os
import sys

import scipy.signal
import librosa
import numpy as np


windows = {'hamming': scipy.signal.hamming, 'hann': scipy.signal.hann, 'blackman': scipy.signal.blackman,
           'bartlett': scipy.signal.bartlett}


def stft(audio, sr, window_size, window_stride, normalize=False):
    n_fft = int(sr * window_size)
    win_length = n_fft
    hop_length = int(sr * window_stride)
    stft = librosa.stft(audio,
                        n_fft=n_fft,
                        hop_length=hop_length,
                        win_length=win_length,
                        window=window
                        )
    spect, phase = librosa.magphase(stft)
    spect = np.log1p(spect)
    spect = torch.FloatTensor(spect)
    if normalize:
        mean = spect.mean()
        std = spect.std()
        spect.add_(-mean)
        spect.div_(std)
    return spect
