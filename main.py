# Le code est à améliorer en
# limitant le plus possible les variables globales et
# en jouant avec les fonctions, les returns, ...

import turtle
import random
import pygame
import vlc

# Ligne suivante à modifier en fonction du chemin d'accès de l'utilisateur
# Ne pas oublier de télécharger les différentes musiques à récupérer dans le GitHub
lien = r"C:\Users\cleme\PycharmProjects\indulgencepape"
p = vlc.MediaPlayer(lien + "\music.mp3")
p.play()
# On met en place la musique générale, et on sauvegarde d'avance des variables pour les musiques
# dans le cas de victoires et de défaites.
d = vlc.MediaPlayer(lien + "\defeat.mp3")
v = vlc.MediaPlayer(lien + "\victory.mp3")



#winsound.PlaySound(r'C:\Users\cleme\PycharmProjects\indulgencepape\music.mp3',winsound.SND_ASYNC)

# Initialisation globale des différentes variables dont on aura besoin dans l'ensemble du code

jeutermine = 1
turtle.tracer(False)
screen = turtle.Screen()
cpt = 0
turtle.speed(0)
bonus = 1
turtle.title("Le commerce des indulgences vu par Luther")
donatello = turtle.Turtle()
leonardo = turtle.Turtle()
lespeches = 0
papamobile = turtle.Turtle()
tauxdepeche = 5
interventionpontificale = 0
interventiondiabolique = 0
michelangelo = turtle.Turtle()
raphael = turtle.Turtle()
don = 0
donatello.goto(-160, 210)
raphael.goto(-180, -170)
michelangelo.goto(-135, -135)
leonardo.goto(-160,-90)

def statistiques():
    # une partie de l'interface graphique
    turtle.goto(-290, 220)
    turtle.write("Nombre de pardons :", font=("Gothic", 10, "normal"))
    turtle.penup()
    turtle.goto(-50, 200)
    turtle.left(180 + 90)
    turtle.pendown()
    turtle.forward(400)
    turtle.left((180 + 90))
    turtle.forward(250)
    turtle.penup()
    #turtle.goto(-290, 180)
    #turtle.write("Achats d'indulgences :", font=("Gothic", 10, "normal"))
    turtle.goto(-290, 160)
    turtle.write("Achat d'une indulgence", font=("Gothic", 10, "normal"))
    turtle.goto(-290, 120)
    turtle.write("(Pour 50 pardons un \n en plus par jour)", font=("Gothic", 10, "normal"))
    turtle.goto(-290, 100)
    turtle.write("Faire un don à l'Eglise", font=("Gothic", 10, "normal"))
    turtle.goto(-290, 80)
    turtle.write("(Pour 50 indulgences, 1 don)", font=("Gothic", 10, "normal"))
    turtle.goto(-290, 60)
    turtle.write("Demander une faveur pontificale : ", font=("Gothic", 10, "normal"))
    turtle.goto(-290, 20)
    turtle.write("(Pour 20 indulgences \n 100 péchés supprimés)", font=("Gothic", 10, "normal"))
    turtle.goto(-290,0)
    turtle.write("Retraite spirituelle", font=("Gothic", 10, "normal"))
    turtle.goto(-290,-40)
    turtle.write("(Pour 100 pardons, \n 1 péché en moins par jour)", font=("Gothic", 10, "normal"))
    turtle.goto(-290,-80)
    turtle.write("Nombre de péchés :", font=("Gothic", 10,"normal"))
    turtle.goto(-290,-120)
    turtle.write("Nombre d'indulgences :", font=("Gothic", 10, "normal"))
    turtle.goto(-290,-160)
    turtle.write("Nombre de dons :",font=("Gothic",10,"normal"))


def croix():
    # la représentation de la croix
    turtle.left(180)
    x = 90
    turtle.goto(x, 250)
    while x != 181:
        turtle.pendown()
        turtle.forward(500)
        turtle.penup()
        x = x + 1
        turtle.goto(x, 250)
    turtle.penup()
    turtle.left(90)
    x = 125
    turtle.goto(-20, x)
    while x != 49:
        turtle.pendown()
        turtle.forward(310)
        turtle.penup()
        x = x - 1
        turtle.goto(-20, x)
    turtle.penup()


def dessinercadre():
    # le reste de l'interface graphique et le cadre
    turtle.penup()
    turtle.goto(300,-250)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(-300,-250)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.goto(300,-250)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()
    turtle.goto(300,250)
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()
    turtle.goto(-300,200)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    croix()
    statistiques()
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.goto(-50,-50)
    turtle.penup()
    turtle.goto(-300, 180)
    turtle.pendown()
    turtle.goto(-50,180)
    turtle.penup()
    turtle.goto(-300,120)
    turtle.pendown()
    turtle.goto(-50,120)
    turtle.penup()
    turtle.goto(-300,75)
    turtle.pendown()
    turtle.goto(-50,75)
    turtle.penup()
    turtle.goto(-300,15)
    turtle.pendown()
    turtle.goto(-50,15)
    turtle.penup()
    turtle.goto(-300,-90)
    turtle.pendown()
    turtle.goto(-50,-90)
    turtle.penup()
    turtle.goto(-300,-135)
    turtle.pendown()
    turtle.goto(-50,-135)
    turtle.penup()

def jeu() :
    # lejeu
    screen.onclick(cliquer)
    turtle.mainloop()


def cliquer(x, y):
    #le fonctionnement global, l'algorithme réel de notre programme
    global jeutermine
    global cpt
    global bonus
    global tauxdepeche
    global don
    findujeu = 0
    papamobile.clear()
    turtle.goto(x,y)
    global interventionpontificale
    global interventiondiabolique
    if jeutermine == 1:
        if interventionpontificale <= 50 and interventionpontificale > 0:
            interventionpontificale = interventionpontificale - 1
            papamobile.goto(-45,165)
            if interventionpontificale !=0:
                papamobile.write("Bravo, le pape est \nvenu vous rendre \nvisite, vous gagnez\n 50 indulgences \npour 50 jours !",
                             font=("Gothic",10,"normal"))
            michelangelo.clear()
            michelangelo.write(bonus-1,font=("Gothic",25,"normal"))
            #print(interventionpontificale)
            if interventionpontificale == 0:
                bonus = bonus - 50
        if interventiondiabolique <=50 and interventiondiabolique >0:
            interventiondiabolique = interventiondiabolique - 1
            papamobile.goto(-45, -20)
            if interventiondiabolique !=0:
                papamobile.write("Vous avez fait\n une très grosse\n bêtise :(, \nvous êtes \nmaintenant puni !",
                             font=("Gothic",10,"normal"))
            if interventiondiabolique == 0:
                tauxdepeche = tauxdepeche - 50
        #screen.ontimer(afficher_infos, 1)
        #cpt = turtle.ontimer(compterlescliquer(cpt))
        if x > -20 and x < 250 and y > -250 and y < 250 :
            cpt = compterlescliquer(cpt)
            ok = papeoudiable()
            if ok == 1 and interventionpontificale == 0:
                interventionpontificale = 50
                papamobile.goto(-45,165)
                papamobile.write("Bravo, le pape est \nvenu vous rendre \nvisite, vous gagnez\n 50 indulgences \npour 50 jours !", font=("Gothic", 10, "normal"))
                bonus = bonus + 50
            if ok == 2 and interventiondiabolique == 0:
                interventiondiabolique = 50
                papamobile.goto(-45, -20)
                papamobile.write("Vous avez fait\n une très grosse\n bêtise :(, \nvous êtes \nmaintenant puni !",
                                 font=("Gothic", 10, "normal"))
                """
                e = random.randint(0,2)
                if e == 2:
                    papamobile.goto(200,-40)
                    papamobile.write("Heureusement, vous êtes de la famille du pape, ouf",
                                     font=("Gothic", 10, "normal"))
                else :
                    """
                tauxdepeche = tauxdepeche + 50
        """        
        if interventionpontificale >0 and x > -20 and x < 250 and y > -250 and y < 250:
            cpt = compterlescliquer(cpt)
            interventionpontificale = interventionpontificale - 1
            if interventionpontificale ==0 :
                bonus = bonus - 50
        if interventiondiabolique > 0 and x > -20 and x < 250 and y > -250 and y < 250:
            cpt = compterlescliquer(cpt)
            interventiondiabolique = interventiondiabolique - 1
            if interventiondiabolique ==0:
                tauxdepeche = tauxdepeche + 50
                """
        if cpt >= 50 and x > -290 and x < -75 and y < 175 and y > 120:
            bonususine()
            cpt = cpt-(50+bonus-1)
            donatello.write(cpt, font=("Gothic", 25, "normal"))

        if bonus >= 50 and x > -290 and x < -100 and y > 70 and y < 100 :
            dondeterre()
            raphael.clear()
            raphael.write(don,font=("Gothic",25,"normal"))
            michelangelo.clear()
            michelangelo.write(bonus-1,font=("Gothic",25,"normal"))
        if bonus >= 20 and x > -290 and x < -100 and y < 70 and y > 25 :
            faveur()
            leonardo.clear()
            leonardo.write(lespeches, font=("Gothic", 25, "normal"))
            michelangelo.clear()
            michelangelo.write(bonus-1,font=("Gothic",25,"normal"))
        if cpt >= 100 and x > -290 and x < -100 and y < 10 and y > -45 :
            retraitespirtuelle()
            donatello.clear()
            donatello.write(cpt,font=("Gothic",25,"normal"))

        print(x,y)
        peche()
        #print(bonus)
        findujeu = victoire()
        if findujeu == 1:
            messagevictoire(findujeu)
        findujeu = defaite()
        if findujeu == 2:
            messagevictoire(findujeu)

# chacune de ces fonctions a un effet sur les différentes statistiques de l'utilisateur en fonction de son choix

def dondeterre():
    global don
    global bonus
    don = don + 1
    bonus = bonus - 50

def compterlescliquer(notrecompteur):
    global cpt
    global bonus
    #faire des if pour vérifier les cas oui c'est ko
    cpt = notrecompteur + bonus
    afficher_infos()
    return cpt

def afficher_infos():
    global bonus
    global cpt
    turtle.penup()
    """
    turtle.color("white")
    turtle.goto(-160,210)
    test = 0
    #donatello
    while test != 5:
        turtle.write((nombredepardons-bonus),font=("Gothic",25,"normal"))
        test = test + 1
    """
    #turtle.color("black")
    donatello.clear()
    donatello.write(cpt,font=("Gothic",25,"normal"))
    #mettre un max à 999 ?

def bonususine():
    global cpt
    global bonus
    global tauxdepeche
    """
    test = 0
    while test != 5:
        turtle.color("white")
        turtle.write((cpt), font=("Gothic", 25, "normal"))
        test = test + 1
    """
    bonus = bonus + 1
    donatello.clear()
    #turtle.color("black")
    #print("Votre nombre d'indulgences est à", (bonus-1))
    abus = random.randint(0,11)
    """
    screen.ontimer(test, 1), test de faire fonctionner un timer abandonné pour des pardons ou indulgences par seconde
    """
    if abus == 5:
        tauxdepeche = tauxdepeche+1
    michelangelo.clear()
    michelangelo.write(bonus-1,font=("Gothic",25,"normal"))

def peche() :
    global lespeches
    global tauxdepeche
    if tauxdepeche >0:
        peche = random.randint(0,tauxdepeche)
        lespeches = lespeches + peche
        leonardo.clear()
        leonardo.write(lespeches,font=("Gothic",25,"normal"))

"""

def test():
    global bonus
    bonus = bonus +1

"""

def faveur():
    global bonus
    global lespeches
    bonus = bonus-20
    lespeches = lespeches - 100

# aleatoire d'ajout d'une aide ou non

def papeoudiable():
    chance = random.randint(0,250)
    if chance == 50:
        ok = 1
        return ok
    if chance == 51 :
        ok = 2
        return ok
    #cookiedor

def retraitespirtuelle():
    global tauxdepeche
    global cpt
    tauxdepeche = tauxdepeche - 1
    cpt = cpt - 100

# verification de la victoire

def victoire():
    global cpt
    global lespeches
    global don
    findujeu = 0

    #cpt >= 1 000 000 et lespeches <= 0 and don >= 50
    # modifiable pour vérifier le bon fonctionnement du code
    if cpt >= 10000 and lespeches <= 0 and don >= 50:
        findujeu = 1
    return findujeu

def messagevictoire(findujeu):
    global jeutermine
    global p
    global v
    global d
    if findujeu == 1:
        test = snake()
        if findujeu == 1 and test == 1:
            donatello.penup()
            donatello.clear()
            michelangelo.clear()
            turtle.clear()
            raphael.clear()
            leonardo.clear()
            donatello.goto(-220,-220)
            donatello.pendown()
            donatello.write("Vous êtes le vainqueur !\n Vous voici au paradis...", font=("Gothic", 20, "normal"))
            win = turtle.Screen()
            win.bgpic('victoiredeux.gif')
            p.stop()
            v.play()
            jeutermine = 0
            return jeutermine
        else :
            messagevictoire(2)
    else :
        donatello.penup()
        donatello.clear()
        turtle.clear()
        leonardo.clear()
        michelangelo.clear()
        raphael.clear()
        donatello.goto(-220,-220)
        donatello.pendown()
        donatello.write("Vous êtes le perdant\n Bienvenue en enfer...", font=("Gothic", 20, "normal"))
        win = turtle.Screen()
        win.bgpic('hell.gif')
        p.stop()
        d.play()
        jeutermine = 0
        return jeutermine

# bis defaite

def defaite():
    global lespeches
    global bonus
    global cpt
    findujeu = 0
    #10 000
    # modifiable pour vérifier le bon fonctionnement du code
    if lespeches >= 1000 or bonus <= -20 or cpt <= -50:
        findujeu = 2
    return findujeu



#def minijeu():


#def tempsreel() :

    #trouver, comme pour le DM de Java ou de Python, un moyen d'ajouter des indulgences par secondes en fonction des bonus choisis

# le serpent final

def snake():
    pygame.init()
    pygame.display.set_caption('Vaincre le péché originel')
    ecran = pygame.display.set_mode((800,600))
    blanc = (255,255,255)
    noir = (0,0,0)
    rouge = (255,0,0)
    temps = pygame.time.Clock()

    #Pour gagner... il faut perdre !
    positionun = 100
    positiondeux = 100
    changementun = 0
    changementdeux = 0
    pygame.draw.rect(ecran, blanc, [positionun, positiondeux, 10, 10])
    findujeu = 0
    hasardun = random.randint(0,800)
    hasarddeux = random.randint(0,600)
    pygame.display.update()
    while findujeu == 0:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                findujeu = 1
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT:
                    changementun = -10
                    changementdeux = 0
                else :
                    if event.key == pygame.K_RIGHT:
                        changementun = 10
                        changementdeux = 0
                    else :
                        if event.key == pygame.K_UP:
                            changementun = 0
                            changementdeux = -10
                        else :
                            if event.key == pygame.K_DOWN:
                                changementun = 0
                                changementdeux = 10
        if positionun >= 800 or positionun < 0 or positiondeux >= 600 or positiondeux < 0:
            findujeu = 1
            pygame.quit()
        else:
            positionun = positionun + changementun
            positiondeux = positiondeux + changementdeux
            ecran.fill(noir)
            pygame.draw.rect(ecran,blanc,[positionun,positiondeux,10,10])
            pygame.draw.rect(ecran, rouge, [hasardun, hasarddeux, 10, 10])
            pygame.display.update()
            temps.tick(30)
            #print(positionun)
            #print(positiondeux)
        if positionun == hasardun and positiondeux == hasarddeux:
            findujeu = 2
            pygame.quit()


    return findujeu



dessinercadre()
jeu()

