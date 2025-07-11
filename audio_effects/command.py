from typing import Callable, List
import numpy as np
from audio_effects.base import AudioEffect

class Command:
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError
    
class AddEffectCommand(Command):
    def __init__(self, effect_stack: List[AudioEffect], create_fn: Callable[[AudioEffect], AudioEffect]):
        self.effect_stack = effect_stack
        self.create_fn = create_fn
        self.added_effect = None

    def execute(self):
        self.added_effect = self.create_fn()
        if self.effect_stack:
            self.added_effect.effect = self.effect_stack[-1]
        self.effect_stack.append(self.added_effect)

    def undo(self):
        if self.effect_stack:
            self.effect_stack.pop()