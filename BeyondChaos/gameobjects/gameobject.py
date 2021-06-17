from abc import ABC, abstractmethod


class GameObject(ABC):

    def __init__(self, address: int):
        self.address = address

    @abstractmethod
    def get_bytes(self):
        """
        Returns a dictionary of address -> value for direct substitution into the ROM.
        """
        raise NotImplementedError
