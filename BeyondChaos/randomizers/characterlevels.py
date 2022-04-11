import random

from gameobjects.character import Character
from randomizers.baserandomizer import Randomizer
from options import Options
from typing import List


class TerraLevel(Randomizer):
    def __init__(self, rng: random.Random, options: Options, characters: List[Character]):
        super().__init__(rng, options)
        self._characters = characters

    @property
    def priority(self):
        return 51

    @property
    def is_active(self):
        return self._Options.random_character_stats and not self._Options.is_code_active('worringtriad')

    def __randomize(self):
        level_map = {
            0: [70, 20, 5, 5],  # avg. level + 0
            1: [18, 70, 10, 2],  # avg. level + 2
            2: [9, 20, 70, 1],  # avg. level + 5
            3: [20, 9, 1, 70]  # avg. level - 3
        }
        for character in self._characters:
            # Don't randomize Terra's level like everyone else's because it gets added
            # for every loop through the title screen, apparently.
            if character.id == 1:
                terra_level = self._rng.choice([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8])
                character.initial_level_override = terra_level
            else:
                level_roll = self._rng.randint(0, 99)
                level_chance_array = level_map[character.level_modifier]
                new_level_modifier = 0
                while level_roll >= 0:
                    level_roll -= level_chance_array[new_level_modifier]
                    new_level_modifier += 1
                character.level_modifier_mutated = new_level_modifier - 1
