import random

from gameobjects.character import Character
from randomizers.baserandomizer import Randomizer
from options import Options
from typing import List


class CharacterStats(Randomizer):

    def __init__(self, rng: random.Random, options: Options, characters: List[Character]):
        super().__init__(rng, options)
        self._characters = characters

    @property
    def priority(self):
        return 52

    @property
    def is_active(self):
        return self._Options.is_code_active("random_zerker")

    def __randomize(self):
        zerker = self._rng.choice(range(13))
        self._characters[zerker].berserk = True
