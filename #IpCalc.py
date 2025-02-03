# IpCalc.py

import re
import sys


def classe(totoctet: list[int]) -> None:
    if totoctet[0] <= 223 and totoctet[0] >= 192:
        print("le masque de sous réseau est : Classe C")
    elif totoctet[0] <= 191 and totoctet[0] >= 128:
        print("le masque de sous réseau est : Classe B")
    elif totoctet[0] <= 127 and totoctet[0] >= 0:
        print("le masque de sous réseau est : Classe A")
    else:
        print("Classe non reconnu")


def netmask(totoctet: list[int]) -> None:
    prefixe = totoctet[4]
    mask = (1 << 32) - (1 << (32 - prefixe))
    netmask = [str((mask >> i) & 0xFF) for i in [24, 16, 8, 0]]
    binaire_netmask = ".".join(format(int(octet), "08b") for octet in netmask)
    print(f"Netmask: {'.'.join(netmask)} / {prefixe} ({binaire_netmask})")


def nbrhote(totoctet: list[int]) -> None:
    h = 32 - totoctet[4]
    hotesUtili = 2**h - 2
    print("Le nombre d'Hotes utilisables est de :", hotesUtili)


def main() -> int:
    """The main function"""

    ipv4: str = input("Veuillez entrer une adresse IP sous forme XXX.XXX.XXX.XXX/XX:")

    totoctet_str: list[str] = re.split(r"[./]", ipv4)
    totoctet: list[int] = [int(octet) for octet in totoctet_str]
    print("L'adresse IP est : {}.{}.{}.{}/{}".format(*totoctet))

    binaireIp = []

    for octet in totoctet:
        binaire = format(
            octet, "08b"
        )  # permet de générer un nombre binaire en octet au format 8bytes
        binaireIp.append(binaire.zfill(8))

    print("l'adresse IP en binaire est :", ".".join(binaireIp))

    netmask(totoctet)
    classe(totoctet)
    nbrhote(totoctet)

    return 0


if __name__ == "__main__":
    sys.exit(main())
