from mitarbeiter import Mitarbeiter
from vorgesetzter import Vorgesetzter


def main():
    walterWinkelmann: Mitarbeiter = Mitarbeiter("Walter Winkelmann")
    waltraudWichtig: Vorgesetzter = Vorgesetzter("Waltraud Wichtig")
    hermannWichtiger: Vorgesetzter = Vorgesetzter("Hermann Wichtiger")
    williWinzig = Mitarbeiter("Willi Winzig")

    walterWinkelmann.setzeVorgesetzten(waltraudWichtig)
    waltraudWichtig.setzeVorgesetzten(hermannWichtiger)

    print(walterWinkelmann.darfBestellen(15))
    print(walterWinkelmann.darfBestellen(20))
    print(walterWinkelmann.darfBestellen(21))
    print(hermannWichtiger.darfBestellen(15))
    print(hermannWichtiger.darfBestellen(25))

    walterWinkelmann.setzeBestellLimit(30)
    print(walterWinkelmann.bekommeBestelllimit())
    print(walterWinkelmann.darfBestellen(21))
    print(hermannWichtiger.darfBestellen(25))

    waltraudWichtig.setzeBestellLimit(10)
    print(waltraudWichtig.bekommeBestelllimit())
    print(waltraudWichtig.darfBestellen(10))
    print(waltraudWichtig.darfBestellen(11))

    waltraudWichtig.setzeBestellLimit(5000)
    print(waltraudWichtig.darfBestellen(2000))
    print(waltraudWichtig.darfBestellen(7000))

    waltraudWichtig.gibInfo()
    walterWinkelmann.gibHierarchie(walterWinkelmann)
    hermannWichtiger.gibInfo()
    hermannWichtiger.gibHierarchie(hermannWichtiger)
    walterWinkelmann.gibInfo()
    walterWinkelmann.gibHierarchie(walterWinkelmann)

    waltraudWichtig.setzeVorgesetzten(None)
    walterWinkelmann.gibHierarchie(walterWinkelmann)
    williWinzig.gibInfo()
    williWinzig.gibHierarchie(williWinzig)


if __name__ == "__main__":
    main()
