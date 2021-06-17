from numpy.random import Generator

from gameobjects.character import Character
from randomizers.baserandomizer import Randomizer
from options import Options


class UmaroRisk(Randomizer):
    def __init__(self, rng: Generator, options: Options, characters: list[Character]):
        super().__init__(options)
        self._metronome = self._Options.is_code_active('metronome')
        self._collateral_damage = self._Options.is_code_active("collateraldamage")
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
        vanilla_umaro_id = 12
        highest_character_id = 13
        candidates = [
            c for c in self._characters
            if c.id <= highest_character_id and c.id != vanilla_umaro_id
            and magic_command not in c.battle_commands
            and lore_command not in c.battle_commands
            and xmagic_command not in c.battle_commands
        ]
        if not candidates:
            candidates = [c for c in self._characters if c.id <= 13 and c.id != 12]
        umaro_risk = self._rng.choice(candidates)
        if 0xFF in umaro_risk.battle_commands:
            battle_commands = [0]
            if not self._collateral_damage:
                extended_commands = list(self._rng.permutation([3, 5, 6, 7, 8, 9, 0xA, 0xB,
                                                                0xC, 0xD, 0xE, 0xF, 0x10,
                                                                0x12, 0x13, 0x16, 0x18, 0x1A,
                                                                0x1B, 0x1C, 0x1D])[:2])
                battle_commands.extend(extended_commands)
            battle_commands.append(1)
            umaro_risk.battle_commands = battle_commands

        """
            umaro = [c for c in characters if c.id == 13][0]
            umaro.battle_commands = list(umaro_risk.battle_commands)
            if random.choice([True, False, False]):
                umaro_risk.battle_commands = [0x00, 0xFF, 0xFF, 0xFF]
            else:
                cands = [0x00, 0x05, 0x06, 0x07, 0x09, 0x0A, 0x0B, 0x10,
                         0x12, 0x13, 0x16, 0x18]
                cands = [i for i in cands if i not in changed_commands]
                base_command = random.choice(cands)
                commands = list(commands.values())
                base_command = [c for c in commands if c.id == base_command][0]
                base_command.allow_while_berserk(fout)
                umaro_risk.battle_commands = [base_command.id, 0xFF, 0xFF, 0xFF]

            umaro.beserk = False
            umaro_risk.beserk = True

            if Options_.is_code_active('metronome'):
                umaro_risk.battle_commands = [0x1D, 0xFF, 0xFF, 0xFF]

            umaro_risk.write_battle_commands(fout)
            umaro.write_battle_commands(fout)

            umaro_exchange_sub = Substitution()
            umaro_exchange_sub.bytestring = [0xC9, umaro_risk.id]
            umaro_exchange_sub.set_location(0x21617)
            umaro_exchange_sub.write(fout)
            umaro_exchange_sub.set_location(0x20926)
            umaro_exchange_sub.write(fout)

            spells = get_ranked_spells(sourcefile)
            spells = [x for x in spells if x.target_enemy_default]
            spells = [x for x in spells if x.valid]
            spells = [x for x in spells if x.rank() < 1000]
            spell_ids = [s.spellid for s in spells]
            index = spell_ids.index(0x54)  # storm
            index += random.randint(0, 10)
            while random.choice([True, False]):
                index += random.randint(-10, 10)
            index = max(0, min(index, len(spell_ids) - 1))
            spell_id = spell_ids[index]
            storm_sub = Substitution()
            storm_sub.bytestring = bytes([0xA9, spell_id])
            storm_sub.set_location(0x21710)
            storm_sub.write(fout)

            return umaro_risk
        """
        pass

    @property
    def is_active(self):
        return False
        # return self._Options.random_zerker
