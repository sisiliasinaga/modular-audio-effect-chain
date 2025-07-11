import numpy as np
from audio_effects.factory import create_effect

# simulate sine wave
t = np.linspace(0, 2*np.pi, 44100)
signal = 0.8 * np.sin(440 * t)

# effect chain of compressor -> hall reverb
effect_chain = create_effect("reverb_hall", create_effect("compressor"))

# apply effects
processed = effect_chain.apply(signal)

print("Original max amplitude:", np.max(np.abs(signal)))
print("Processed max amplitude:", np.max(np.abs(processed)))
