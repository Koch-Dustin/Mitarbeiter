from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vorgesetzter import Vorgesetzter


class Mitarbeiter:

    bestelllimit = 20
    vorgesetzter: Vorgesetzter = None

    def __init__(self, name: str):
        self.name: str = name

    @classmethod
    def setzeBestellLimit(cls, limit: int):
        cls.bestelllimit = limit

    def setzeVorgesetzten(self, vorgesetzter: Vorgesetzter):
        self.vorgesetzter: Vorgesetzter = vorgesetzter

    def darfBestellen(self, kosten: int):
        if kosten <= self.bestelllimit:
            return True
        if kosten > self.bestelllimit:
            return False

    def bekommeBestelllimit(self):
        return self.bestelllimit

    def bekommeVorgesetzten(self):
        if self.vorgesetzter == None:
            print("Dieser Mitarbeiter hat noch keinen Vogesetzten!")
            return None
        else:
            return self.vorgesetzter

    def gibInfo(self):
        if self.vorgesetzter is not None:
            print(
                f"Ich bin {self.__class__.__name__}, Name {self.name}. Mein Vorgesetzter ist {self.vorgesetzter.name}. Mein Bestelllimit ist {self.bestelllimit} EUR."
            )
            return

        if self.vorgesetzter == None and self.__class__.__name__ == "Mitarbeiter":
            print(
                f"Ich bin freier Mitarbeiter, Name {self.name}. Mein Bestelllimit ist {self.bestelllimit}"
            )
            return

        print(
            f"Ich bin {self.__class__.__name__}, Name {self.name}. Mein Bestellimit ist {self.bestelllimit} EUR."
        )

    def gibVorgesetzten(self):
        if self.vorgesetzter is not None:
            return self.vorgesetzter
        else:
            return

    def gibHierarchie(self, mitarbeiter: Mitarbeiter):
        if (
            mitarbeiter.vorgesetzter == None
            and mitarbeiter.__class__.__name__ == "Mitarbeiter"
        ):
            print(f"Freier Mitarbeiter {self.name}")
        else:
            hierachie = []
            chef = mitarbeiter.gibVorgesetzten()

            while True:
                try:
                    chefdata = f"{chef.__class__.__name__} {chef.name}"
                    hierachie.insert(0, chefdata)
                    chef = chef.gibVorgesetzten()
                except AttributeError:
                    break

            for element in hierachie:
                print(element)
            print(f"{self.__class__.__name__} {self.name}")
