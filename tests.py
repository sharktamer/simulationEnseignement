import unittest
from fonction import inverserListe


class TestInversionListe(unittest.TestCase):

    # Test qui valide que la fonction retourne la liste attendue
    def test_resultat_attendu(self):
        prenomsDebut = ["Alexandre", "Benoit", "Camille", "Diane", "Etienne", "Fiona", "Gabriel", "Helene"]
        prenomsFin = ["Etienne", "Fiona", "Gabriel", "Helene", "Alexandre", "Benoit", "Camille", "Diane"]
        inverserListe(prenomsDebut)
        self.assertEqual(prenomsDebut, prenomsFin)

    # Test qui valide que l'inverse de l'inverse nous redonne bien la liste de départ
    def test_inverse_inverse_liste(self):
        prenomsDebut = ["Alexandre", "Benoit", "Camille", "Diane", "Etienne", "Fiona", "Gabriel", "Helene"]
        prenomsDebutCopie = prenomsDebut.copy()
        inverserListe(prenomsDebut)
        inverserListe(prenomsDebut)
        self.assertEqual(prenomsDebut, prenomsDebutCopie)

    # Test assez superflus qui valide que la liste a la même longueur au départ qu'à la fin [Le premier test couvre ce cas indirectement, mais pour donner des exemples]
    def test_meme_longueur_liste(self):
        prenoms = ["Alexandre", "Benoit", "Camille", "Diane", "Etienne", "Fiona", "Gabriel", "Helene"]
        tailleDebut = len(prenoms)
        inverserListe(prenoms)
        self.assertEqual(tailleDebut, len(prenoms))

if __name__ == '__main__':
    unittest.main()