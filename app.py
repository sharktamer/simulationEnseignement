#########################
# Auteur : Mathieu Morissette
#########################
from flask import Flask
from fonction import inverserListe

# Script utilisant la fonction InverserListe dans une page web
app = Flask(__name__)

@app.route("/")
def hello_world():
    prenoms = ["Alexandre", "Benoit", "Camille", "Diane", "Etienne", "Fiona", "Gabriel", "Helene"]
    pageWeb = "<p>" + "Départ : " + str(prenoms) + "</p>" 
    pageWeb += inverserListe(prenoms)
    return pageWeb


####################
# Questions avancées
####################
# 1. Que se passera-t-il si on passe une liste impaire à la fonction?
# 2. Quelle est la complexité algorithmique de notre fonction InverserListe()?
# 3. Comment pourrions-nous modifier la fonction pour que notre liste d'origine ne soit pas modifié?
# 4. Que se passe-t-il en mémoire lorsqu'on permute les valeurs dans cette liste?
#