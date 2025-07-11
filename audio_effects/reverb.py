from audio_effects.base import AudioEffect
import numpy as np

class ReverbAlgorithm:
    def process(self, signal: np.ndarray) -> np.ndarray:
        raise NotImplementedError

class HallReverb(ReverbAlgorithm):
    def process(self, signal):
        return signal + 0.2 * np.roll(signal, 1000)

class RoomReverb(ReverbAlgorithm):
    def process(self, signal):
        return signal + 0.1 * np.roll(signal, 500)

class Reverb(AudioEffect):
    def __init__(self, effect: AudioEffect = None, algorithm: ReverbAlgorithm = HallReverb()):
        self.effect = effect
        self.algorithm = algorithm

    def apply(self, signal: np.ndarray) -> np.ndarray:
        if self.effect:
            signal = self.effect.apply(signal)
        return self.algorithm.process(signal)