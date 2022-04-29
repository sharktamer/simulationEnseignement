#########################
# Auteur : Mathieu Morissette
#########################
# Objectif de l'algorithme : Inverser la première moitié de la liste avec la deuxième moitié de la liste.
######################### 
# Exemple :
# ["1", "2", "3", "4"] ---> ["3", "4", "1", "2"]
#########################

# Fonction d'inversion de la liste
def inverserListe(liste):
    bufferHTML=""
    
    # On prend la taille de la liste et on effectue une division entière [//] par 2. **important pour ne pas avoir une position en décimale
    positionMilieu = len(liste)//2
    # Pour chaque élément de la première moitié de la liste (de la position 0 à celle du milieu)
    for i in range(positionMilieu):
        # On effectue une permutation de l'élément à la position du curseur i avec celui à la position du curseur i+positionMilieu
        liste[i], liste[i+positionMilieu] = liste[i+positionMilieu], liste[i]
        
        bufferHTML += remplirBufferHTML(i, liste)
    # La liste passée dans la fonction est directement modifié, donc pas besoin de la retourner
    return bufferHTML



# Fonction pour formatter du texte d'affichage des itérations de la fonction
def remplirBufferHTML(iteration, liste):
    element1 = liste[iteration]
    element2 = liste[iteration + len(liste)//2]
    stringFormatte = "<p>Itération " + str(iteration+1) + " : " + str(liste) + " (élément " + str(iteration+1) + " permuté avec l'élément " + str(iteration+1 + len(liste)//2) + ")<p>"
    stringFormatte = stringFormatte.replace(element1, "<mark><strong>"+element1+"</strong></mark>")
    stringFormatte = stringFormatte.replace(element2, "<mark><strong>"+element2+"</strong></mark>")
    return stringFormatte