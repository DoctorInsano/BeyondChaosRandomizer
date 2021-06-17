from typing import List

from numpy.random import Generator

from gameobjects.character import Character
from options import Options
from randomizers.baserandomizer import Randomizer


class UmaroRisk(Randomizer):
    def __init__(self, rng: Generator, options: Options, characters: List[Character]):
        super().__init__(options)
        self._characters = characters
        self._rng = rng

    @property
    def priority(self):
        return 40

    def randomize(self):
        if not self.is_active:
            return
        magic_command = 2
        lore_command = 0xC
        xmagic_command = 0x17
        vanilla_gogo_id = 12
        highest_character_id = 13
        candidates = [
            c for c in self._characters
            if c.id <= highest_character_id and c.id != vanilla_gogo_id
               and magic_command not in c.battle_commands
               and lore_command not in c.battle_commands
               and xmagic_command not in c.battle_commands
        ]
        if not candidates:
            candidates = [c for c in self._characters if c.id <= 13 and c.id != vanilla_gogo_id]
        umaro_risk: Character = self._rng.choice(candidates)
        real_umaro = [c for c in self._characters if c.id == 13][0]
        real_umaro.battle_commands = list(umaro_risk.battle_commands)
        real_umaro.berserk = False
        umaro_risk.berserk = True
        pass

    @property
    def is_active(self):
        return False
        # return self._Options.random_zerker
