
import re
import hashlib

def extraire_nom_telephone(fichier_bin):
    with open(fichier_bin, "rb") as f:
        data = f.read()
    strings = re.findall(rb"[ -~]{4,}", data)
    ascii_strings = [s.decode("utf-8", errors="ignore") for s in strings]
    candidats = list(set(s for s in ascii_strings if "GT-" in s or len(s) >= 6))
    return candidats

def calculer_sha1(mac_address, nom_appareil):
    concat = mac_address + nom_appareil
    sha1 = hashlib.sha1(concat.encode()).hexdigest()
    return sha1

if __name__ == "__main__":
    # Exemple : fichier de trame binaire Bluetooth
    fichier = "ch18.bin"

    # Étape 1 : extraire le nom de l'appareil
    noms_possibles = extraire_nom_telephone(fichier)
    print("[+] Noms de téléphone extraits :", noms_possibles)

    # Étape 2 : adresse MAC connue (issue de Wireshark ou challenge)
    adresse_mac = "0C:B3:19:B9:4F:C6"

    # Étape 3 : pour chaque nom, calculer le hash et l'afficher
    for nom in noms_possibles:
        flag = calculer_sha1(adresse_mac, nom)
        print(f"SHA1({adresse_mac + nom}) = {flag}")
