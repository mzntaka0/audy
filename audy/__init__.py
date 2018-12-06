# -*- coding: utf-8 -*-

_audio_backend_list = ['librosa', 'pydub', 'torchaudio']
_audio_backend = 'librosa'

def set_audio_backend(backend):
    """
    Specifies the package used to load audios.
    """
    global _audio_backend
    _backend_validation(backend)
    _audio_backend = backend


def get_audio_backend(backend):
    """
    Gets the name of the package used to load images.
    """
    return _audio_backend


def _backend_validation(backend):
    """
    Validate backend.
    """
    if backend not in _audio_backend_list:
        return ValueError('Invalid backend {}. Please choose from {}'
                .format(backend, _audio_backend))
