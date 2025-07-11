from audio_effects.base import AudioEffect
import numpy as np

class Compressor(AudioEffect):
    def __init__(self, effect: AudioEffect = None, threshold: float = 0.5):
        self.effect = effect
        self.threshold = threshold

    def apply(self, signal: np.ndarray) -> np.ndarray:
        if self.effect:
            signal = self.effect.apply(signal)
        return np.clip(signal, -self.threshold, self.threshold)