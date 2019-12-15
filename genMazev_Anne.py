import classes
import matrice_initiale2 as mazeGen



        

#################################################################################################################################
# Déclaration des variables liées au labyrinthe
### \/ VARIABLES MODIFIABLES. POUR MODIFIER LA TAILLE DU LABYRINTHE, MODIFIER LES VALEURS DE CES DEUX VARIABLES \/ ###
ligne = 7
colonne = 7
### /\ VARIABLES MODIFIABLES. POUR MODIFIER LA TAILLE DU LABYRINTHE, MODIFIER LES VALEURS DE CES DEUX VARIABLES /\ ###

ligneFin = ((ligne - 1)//2)
colFin = ((colonne - 1)//2)

#################################################################################################################################
# Génération du labyrinthe
### Étape 1 - Génération d'un labyrinthe vide aux dimensions finales
maze=[]
for i in range (0,ligneFin):
    maze.append([classes.Salle()])
    for j in range(0,colFin):
        maze[i].append(classes.Salle())


### Étape 2 - Génération d'un labyrinthe "surdimensionné"
laby = mazeGen.labyrinthe_aleatoire(ligne,colonne)

### Étape 3 - Convertir le labyrinthe surdimensionné (tableau de booléens) en labyrinthe interprétable (tableau de Salles)
doors = mazeGen.passages(laby[0])


for i in range (ligneFin):
    for j in range(colFin):
        maze[i][j].setPorteN(doors[i][j]["nord"])
        maze[i][j].setPorteE(doors[i][j]["est"])
        maze[i][j].setPorteS(doors[i][j]["sud"])
        maze[i][j].setPorteO(doors[i][j]["ouest"])


#####################################
#Génération mécanismes

####Constantes modifiables liées aux mécanismes###
nb_meca=4

#Mecan est la liste des mécanismes utiles (à compléter+ construire les objets seau, pelle etc)
mecan=[]
mecan.append(Mecanism("feu",seau,pelle,True,"Eteint le feu", "On trouve une pelle"))
mecan.append(Mecanism("tas de sable",pelle,blason,True,"Pelleter le sable","Blason sous le sable"))
mecan.append(Mecanism("armure",blason, clef, True, "Accrocher le blason sur l'armure","Accès à une clef"))
mecan.append(Mecanism("serrure",clef,liberté, True, "Mettre la clef dans la serrure","Sortie du donjon"))
            

####Placement des mécanismes dans le labyrinthe
choix=mazeGen.mecanisme(laby,nb_meca)

####Liste des abscisses et liste des ordonnées des salles avec mécanismes dans le labyrinthe final
meca_x=[]
meca_y=[]
for i in range(0,len(choix)):
    meca_x=meca_x.append((laby[1][i]-1)/2)
    meca_y=meca_y.append((laby[2][i]-1)/2)

####Intégration des mécanismes utiles dans les salles concernées
    ###Ajout d'un mécanisme utile dans la liste des mécanismes de la salle

for k in range(0,len(choix)):
    maze[meca_x[k]][meca_y[k]].mecas.append(mecan[k])

)


    

####

