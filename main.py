import numpy as np
from audio_effects.factory import create_effect
from audio_effects.command import AddEffectCommand

# simulate sine wave
t = np.linspace(0, 2*np.pi, 44100)
signal = 0.8 * np.sin(440 * t)

# set up command stack
effect_stack = []
undo_stack = []
redo_stack = []

# effect chain of compressor -> hall reverb
# decorator pattern: adds behavior to reverb algo dynamically by taking in AudioEffect instance and chaining effects
add_compressor = AddEffectCommand(effect_stack, lambda: create_effect("compressor"))
add_reverb = AddEffectCommand(effect_stack, lambda: create_effect("reverb_hall"))

for cmd in [add_compressor, add_reverb]:
    cmd.execute()
    undo_stack.append(cmd)
    redo_stack.clear()

# apply final effect chain
def apply_chain():
    if effect_stack:
        final_effect = effect_stack[-1]
        processed = final_effect.apply(signal)
        print("Processed max amplitude:", np.max(np.abs(processed)))
    else:
        print("No effects applied")

apply_chain()

# undo last effect
last = undo_stack.pop()
last.undo()
redo_stack.append(last)
apply_chain()

# redo last effect
last = redo_stack.pop()
last.execute()
undo_stack.append(last)
apply_chain()