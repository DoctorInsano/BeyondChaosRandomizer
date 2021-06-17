from abc import ABC, abstractmethod
from typing import List

from gameobjects.gameobject import GameObject


class Loader(ABC):

    def __init__(self, rom_file_name):
        self.rom_file_name = rom_file_name

    @abstractmethod
    def get(self, force_reload=False) -> List[GameObject]:
        """
        Returns a list game object associated with this loader
        (e.g. a character loader will return a list of characters).

        Keyword arguments:
        force_reload -- throw away the current cached game objects and reload from scratch.
        """
        raise NotImplementedError
