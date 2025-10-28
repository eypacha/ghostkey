# audio.py - utilidades para síntesis y reproducción de sonidos

import numpy as np
import simpleaudio as sa

def play_tone(frequency=440, duration=0.2, volume=0.5, sample_rate=44100):
    """
    Reproduce un tono senoidal de la frecuencia y duración especificadas.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(frequency * 2 * np.pi * t) * volume
    audio = (tone * 32767).astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    play_obj.wait_done()  # Espera a que termine el sonido
