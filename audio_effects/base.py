import numpy as np

class AudioEffect:
    def apply(self, signal: np.ndarray) -> np.ndarray:
        raise NotImplementedError("Must implement apply method")