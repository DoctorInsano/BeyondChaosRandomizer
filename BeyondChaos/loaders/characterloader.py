from typing import List

from gameobjects.character import Character
from loaders.baseloader import Loader
from utils import CHAR_TABLE


class CharacterLoader(Loader):
    def __init__(self, rom_file_name):
        self.character_list = []
        self.rom_file_name = rom_file_name
        return

    def get(self, force_reload=False) -> List[Character]:
        if self.character_list and not force_reload:
            return self.character_list
        self._load_characters()
        return self.character_list

    def _load_characters(self):
        self.character_list = []
        rom = open(self.rom_file_name, "rb")
        character_byte_block_length = 22
        i = 0
        for line in open(CHAR_TABLE):
            line = line.strip()
            if line[0] == '#':
                continue
            while '  ' in line:
                line = line.replace('  ', ' ')
            character_address_and_name = line.split(",")
            character_address = int(character_address_and_name[0], 16)
            rom.seek(character_address)
            character_data = rom.read(character_byte_block_length)
            character = Character(i, character_address, character_address_and_name[1], character_data)
            self.character_list.append(character)
            i += 1
