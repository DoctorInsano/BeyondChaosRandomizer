from numpy.random import Generator

from gameobjects.character import Character
from randomizers.baserandomizer import Randomizer
from options import Options


class ShuffleCharacterCommands(Randomizer):
    def __init__(self, rng: Generator, options: Options, characters: list[Character]):
        super().__init__(options)
        self._characters = characters
        self._rng = rng

    @property
    def is_active(self):
        return self._Options.shuffle_commands

    @property
    def priority(self):
        return 30

    def randomize(self):
        pass
