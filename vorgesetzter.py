from mitarbeiter import Mitarbeiter


class Vorgesetzter(Mitarbeiter):
    def __init__(self, name: str):
        super().__init__(name)

    def setzeBestelllimit(self, limit: int):
        self.bestelllimit = limit
