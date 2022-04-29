#########################
# Auteur : Mathieu Morissette
#########################
from flask import Flask
from fonction import inverserListe

# Script utilisant la fonction InverserListe dans une page web
app = Flask(__name__)

@app.route("/")
def hello_world():
    prenoms = ["Fred", "Adam", "Simon", "Louis", "Marc", "Denis", "Roger", "Luc"]
    pageWeb = "<p>" + "Départ : " + str(prenoms) + "</p>" 
    pageWeb += inverserListe(prenoms)
    return pageWeb
