from audio_effects.compressor import Compressor
from audio_effects.reverb import Reverb, HallReverb, RoomReverb
from audio_effects.base import AudioEffect

def create_effect(effect_name: str, prev_effect: AudioEffect = None) -> AudioEffect:
    if effect_name == "compressor":
        return Compressor(prev_effect, threshold=0.3)
    elif effect_name == "reverb_hall":
        return Reverb(prev_effect, HallReverb())
    elif effect_name == "reverb_room":
        return Reverb(prev_effect, RoomReverb())
    else:
        raise ValueError(f"Invalid effect name: {effect_name}")