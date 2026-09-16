from abc import ABC, abstractmethod

class Menu(ABC):

    @abstractmethod
    def draw_text(self):
        pass

    def draw_menu(self):
        pass