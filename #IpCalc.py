#IpCalc

import re
Ip= input("veuillez entrer une adresse IP sous forme XXX. XXX. XXX. XXX /XX:")

totoctet=re.split(r"[./]",Ip)
totoctet=[int(octet)for octet in totoctet]

print("L'adresse IP est : {}.{}.{}.{} /{}".format(*totoctet))    


def validate_ip(Ip):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}\/\d{1,2}$')

binaireIp=[]
def classe():
    if totoctet [0] <=223 and totoctet[0] >= 192:
        print("le masque de sous réseau est : Classe C")
    elif totoctet [0] <=191 and totoctet[0] >= 128:
        print("le masque de sous réseau est : Classe B")
    elif totoctet [0] <=127 and totoctet[0] >= 0:
        print("le masque de sous réseau est : Classe A")
    else:
        print("Classe non reconnu")


def netmask():
    prefixe = totoctet[4]
    mask = (1 << 32) - (1 << (32 - prefixe))
    netmask = [str((mask >> i) & 0xFF) for i in [24, 16, 8, 0]]
    binaire_netmask = ".".join(format(int(octet), '08b') for octet in netmask)
    print(f"Netmask: {'.'.join(netmask)} / {prefixe} ({binaire_netmask})")


def nbrhote():
    h=32-totoctet[4]
    hotesUtili= 2**h-2
    print("Le nombre d'Hotes utilisables est de :",hotesUtili)
#on utilise      for octet in totoctet :          pour parcourir la liste totoctet de manièrer individuelle, car sinon le octet>0 ne fonctionne pas

for octet in totoctet:
    binaire = format(octet, '08b') #permet de générer un nombre binaire en octet au format 8bytes
    binaireIp.append(binaire.zfill(8))



print("l'adresse IP en binaire est :",".".join(binaireIp))


netmask()
classe()
nbrhote()
 