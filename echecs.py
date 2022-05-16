from upemtk import *

# PARTIE 1

def debut_jeu():
    
    """ Fonction affichant le menu du début du jeu permettant de choisir le nom
    des joueurs et affichant quelques indidcations pour le joueur
    
    """
    affiche_fond_debut()
    rectangle(10,100,500,20,'black','black')
    texte(35,37,"SAISIR LE NOM DU JEU NOIR",'white',taille=30)
    rectangle(700,100,1190,20,'black','black')
    texte(725,37,'SAISIR LE NOM DU JEU BLANC','white',taille=30)
    rectangle(300,120,900,275,'black',epaisseur=5)
    texte(310,140,'-Le menu Pause est accessible en appuyant sur la\ntouche "P"\n\n-Double-cliquez sur un pion pour le sélectionner','black',taille=25)
    nb_choix=0
    while nb_choix<2:
        choix=attend_clic_gauche()
        x,y=choix
        if x>=10 and x<=500 and y>=20 and y<=100:
            nom_noir=input("Saisissez le nom du joueur noir: ")
        if x>=700 and x<=1190 and y<=100 and y>=20:
            nom_blanc=input("Saisissez le nom du joueur blanc: ")
        nb_choix+=1
    return nom_blanc,nom_noir
    
def affiche_morts(morts):
    
    """ Fonction permettant d'afficher les pions morts dans une case à droite du
    jeu
    
    """
    nb_morts_blancs=0
    nb_morts_noirs=0
    nb_pions=0
    
    while nb_morts_blancs<len(morts):
        if morts[nb_morts_blancs]=='pion_blanc':
            fichier= 'données/images/pion_blanc.gif'
            x=825
            y=150
            image(x,y, fichier)
            nb_pions=morts.count('pion_blanc')
            i=1
            while i<nb_pions:
                if i==1:
                    x=825+(i*75)
                    image(x,y, fichier)
                if i==2:
                    x=825+(i*75)
                    image(x,y, fichier)
                if i==3:
                    x=825+(i*75)
                    image(x,y, fichier)
                if i==4:
                    x=825+(i*75)
                    image(x,y, fichier)
                if i==5:
                    y=250
                    x=825
                    image(x,y, fichier)
                if i==6:
                    y=250
                    j=1
                    x=825+(j*75)
                    image(x,y, fichier)
                if i==7:
                    y=250
                    j=2
                    x=825+(j*75)
                    image(x,y, fichier)
                i+=1
        elif morts[nb_morts_blancs]=='tour_blanc':
            fichier= 'données/images/tour_blanc.gif'
            x=1020
            y=250
            image(x,y, fichier)
            nb_pions=morts.count('tour_blanc')-1
            i=0
            while i<nb_pions:
                if x<1150:
                    x+=(nb_pions*75)
                    image(x,y, fichier)
                else:
                    x+=((nb_pions-5)*75)
                    image(x,y, fichier)
                i+=1
        elif morts[nb_morts_blancs]=='fou_blanc':
            fichier= 'données/images/fou_blanc.gif'
            x=825
            y=350
            image(x,y, fichier)
            nb_pions=morts.count('fou_blanc')-1
            i=0
            while i<nb_pions:
                if x<1150:
                    x+=(nb_pions*75)
                    image(x,y, fichier)
                else:
                    x+=((nb_pions-5)*75)
                    image(x,y, fichier)
                i+=1
        elif morts[nb_morts_blancs]=='cavalier_blanc':
            fichier= 'données/images/cavalier_blanc.gif'
            x=1020
            y=350
            image(x,y, fichier)
            nb_pions=morts.count('cavalier_blanc')-1
            i=0
            while i<nb_pions:
                if x<1150:
                    x+=(nb_pions*75)
                    image(x,y, fichier)
                else:
                    x+=((nb_pions-5)*75)
                    image(x,y, fichier)
                i+=1
        elif morts[nb_morts_blancs]=='reine_blanc':
            fichier= 'données/images/reine_blanc.gif'
            image(1150,350, fichier)
        nb_morts_blancs+=1
        
    while nb_morts_noirs<len(morts):
        if morts[nb_morts_noirs]=='pion_noir':
            fichier= 'données/images/pion_noir.gif'
            x=825
            y=650
            image(x,y, fichier)
            nb_pions=morts.count('pion_noir')
            i=1
            while i<nb_pions:
                if i==1:
                    x=825+(i*75)
                    image(x,y, fichier)
                if i==2:
                    x=825+(i*75)
                    image(x,y, fichier)
                if i==3:
                    x=825+(i*75)
                    image(x,y, fichier)
                if i==4:
                    x=825+(i*75)
                    image(x,y, fichier)
                if i==5:
                    y=550
                    x=825
                    image(x,y, fichier)
                if i==6:
                    y=550
                    j=1
                    x=225+(j*75)
                    image(x,y, fichier)
                if i==7:
                    y=550
                    j=2
                    x=825+(j*75)
                    image(x,y, fichier)
                i+=1
        elif morts[nb_morts_noirs]=='tour_noir':
            fichier= 'données/images/tour_noir.gif'
            x=1020
            y=550
            image(x,y, fichier)
            nb_pions=morts.count('tour_noir')-1
            i=0
            while i<nb_pions:
                if x<1150:
                    x+=(nb_pions*75)
                    image(x,y, fichier)
                else:
                    x+=((nb_pions-5)*75)
                    image(x,y, fichier)
                i+=1
        elif morts[nb_morts_noirs]=='fou_noir':
            fichier= 'données/images/fou_noir.gif'
            x=825
            y=450
            image(x,y, fichier)
            nb_pions=morts.count('fou_noir')-1
            i=0
            while i<nb_pions:
                if x<1150:
                    x+=(nb_pions*75)
                    image(x,y, fichier)
                else:
                    x+=((nb_pions-5)*75)
                    image(x,y, fichier)
                i+=1
        elif morts[nb_morts_noirs]=='cavalier_noir':
            fichier= 'données/images/cavalier_noir.gif'
            x=1020
            y=450
            image(x,y, fichier)
            nb_pions=morts.count('cavalier_noir')-1
            i=0
            while i<nb_pions:
                if x<1150:
                    x+=(nb_pions*75)
                    image(x,y, fichier)
                else:
                    x+=((nb_pions-5)*75)
                    image(x,y, fichier)
                i+=1
        elif morts[nb_morts_noirs]=='reine_noir':
            fichier= 'données/images/reine_noir.gif'
            image(1150,450, fichier)
        nb_morts_noirs+=1
def respawn(morts,joueur,fin):
    
    """Fonction permettant à un pion ayant été mangé de réapparaitre si le coup
    pendant lequel le pion a été mangé est annulé
    
    """
    if joueur==1:
        mort=morts.pop()
        if mort=='pion_blanc':
            pion_blanc.append(fin)
        elif mort=='tour_blanc':
            tour_blanc.append(fin)
        elif mort=='cavalier_blanc':
            cavalier_blanc.append(fin)
        elif mort=='fou_blanc':
            fou_blanc.append(fin)
        elif mort=='reine_blanc':
            reine_blanc.append(fin)
            
    elif joueur==2:
        mort=morts.pop()
        if mort=='pion_noir':
            pion_noir.append(fin)
        elif mort=='tour_noir':
            tour_noir.append(fin)
        elif mort=='cavalier_noir':
            cavalier_noir.append(fin)
        elif mort=='fou_noir':
            fou_noir.append(fin)
        elif mort=='reine_blanc':
            reine_noir.append(fin)
        
def affiche_score(pions_blanc,pions_noir,morts,score_noir,score_blanc):
    
    """ Fonction affichant le score, c'est-à-dire le nombre de pions mangés de 
    chaque joueur 
    
    """
    i=0
    while i<5:
        if pions_blanc[i] in morts:
            mort=pions_blanc[i]
            j=morts.count(mort)
            score_noir+=j
        if pions_noir[i] in morts:
            mort=pions_noir[i]
            j=morts.count(mort)
            score_blanc+=j
        i+=1
        
    rectangle(1035,720,1170,680,'black','red')
    rectangle(1035,80,1170,120,'black','red')
    texte(1040,85,'SCORE=')
    texte(1150,85,score_noir)
    texte(1040,685,'SCORE=')
    texte(1150,685,score_blanc)
    
def affiche_tours(joueur,nom_blanc,nom_noir):
    
    """ Fonction recevant le nom des deux joueurs et renvoyant deux string 
    affichant le tour du joueur
    
    """
    if joueur==1:
        texte(815,730,'TOUR DE',taille=40)
        texte(1010,730,nom_blanc,taille=40)
    if joueur==2:
        texte(815,30,'TOUR DE',taille=40)
        texte(1010,30,nom_noir,taille=40)

def affiche_fond_debut():
    
    """ Fonction affichant le fond d'écran du menu de départ du jeu
    
    """
    fichier='données/images/fond.gif'
    image(600,400,fichier)

def plateau():
    
    """Fonction dessinant les cases du plateau
    
    """
    colonne = 0
    ligne= 0
    ax = 0
    bx = 100
    ay = 0
    by = 100
    bleu = True
    while colonne < 8:
        while ligne < 8:
            if bleu == True:
                rectangle(ax, ay, bx, by, couleur='blue',remplissage='blue')
                ligne +=1
                ax += 100
                bx += 100
                bleu = False
            else:
                rectangle(ax, ay, bx, by, couleur='white',remplissage='white')
                ligne +=1
                ax += 100
                bx += 100
                bleu = True
        ligne = 0
        colonne += 1
        if colonne == 1 or colonne == 3 or colonne == 5 or colonne == 7:
            bleu = False
        else:
            bleu = True
        ax = 0
        ay = by
        bx = 100
        by += 100

def affiche_pieces(pos_blanc, pos_noir, img, img2):
    
    """Affiche l'ensemble des pieces à sa position établie
    
    """
    fichier = 'données/images/' + img
    fichier_2 = 'données/images/' + img2
    i = 0
    while i < len(pos_blanc):
        x, y = case_to_pixel(pos_blanc[i])
        image(x, y, fichier)
        i += 1
    i = 0
    while i < len(pos_noir):
        x, y = case_to_pixel(pos_noir[i])
        image(x, y, fichier_2)
        i += 1
    
    # PARTIE 2
    
def case_to_pixel(c):
    
    """	Fonction recevant les coordonnées d'une case du plateau sous la 
    forme d'un couple d'entiers (ligne, colonne) et renvoyant les 
    coordonnées du pixel se trouvant au centre de cette case. Ce calcul 
    prend en compte la taille de chaque case, donnée ici par la variable case
    
    """
    ax,ay=c
    return ((ax + 5)*case,(ay + 5)*case)
    
def case_selectionnee(début,jeu):
    
    """Fonction recevant les coordonées de la case sélectionnée et permettant 
    de créer un contour rouge autour de celle-ci afin d'informer le joueur de la 
    case qu'il a selectionné
    
    """
    if jeu==True:
        x,y= début
        x,y= x*10,y*10
        bx,by= x+100,y+100
        rectangle(x,y,bx,by, couleur='red', epaisseur = 6)
    
def nouv_coord(choix):
    
    """Fonction recevant une position en abcisse et en ordonee et renvoyant 
    des nouvelles coordonées pour permettre une meilleure identification
    
    """
    x,y=choix

    surplus_x=x%100
    x=(x-surplus_x)//10
    surplus_y =y%100
    y=(y-surplus_y)//10
    return x,y

def indice_x(liste,x):
    
    """Fonction recevant une liste et une valeur, et renvoyant la position de 
    cette valeur dans la liste mise pour argument
    
    """
    j=0
    while liste[j]!=x:
        j+=1
    return j

def mouv_cavaliers(début, fin):
    
    """Fonction recevant les coordonées de base du cavalier et les coordonées
    de la case où le joueur souhaite faire déplacer le cavalier
    permettant de vérifier si ce déplacement respecte les règles de base de 
    l'échec
    
    """
    j=0
    x,y=début
    bx,by=fin
    if début==fin:
        return False
    while j<2:
        if x-bx==20 and y-by==10:
            return True
        elif x-bx==20 and y-by==-10:
            return True
        elif x-bx==-20 and y-by==10:
            return True
        elif x-bx==-20 and y-by==-10:
            return True
        y,x=début
        by,bx=fin
        j+=1
    return False

def mouv_tour(début, fin, ennemi, allie):
    
    """Fonction permettant de savoir si une pièce du jeu se trouve sur le chemin
    de la tour établi par le joueur et permmettant de savoir si la case 
    selectionnee par le joueur respecte les regles de deplacement de la tour   
    
    """
    x,y=début
    bx,by=fin
    if début==fin:
        return False
    if bx>x:
        bx-=10
        while bx>x:
            if ennemi.count((bx,by))==1 or allie.count((bx,by))==1:
                return False
            bx-=10
        return True
    elif bx<x :
        bx+=10
        while bx<x :
            if ennemi.count((bx,by))==1 or allie.count((bx,by))==1:
                return False
            bx+=10
        return True
    elif  by>y:
        by-=10
        while by>y:
            if ennemi.count((bx,by))==1 or allie.count((bx,by))==1:
                return False
            by-=10
        return True
    elif by<y:
        by+=10
        while by<y:
            if ennemi.count((bx,by))==1 or allie.count((bx,by))==1:
                return False
            by+=10
        return True

def mouv_fou(début, fin, ennemi, allie):
    
    """Fonction ayant la même fonction que celle de la tour mais pour le fou
    
    """
    x,y=début
    bx,by=fin
    if début==fin:
        return False
    if bx>x and by>y:
        by-=10
        bx-=10
        while bx>x:
            if (ennemi.count((bx,by))==1 or allie.count((bx,by))==1):
                return False
            bx-=10 
            by-=10
        return True
    elif bx<x and by<y:
        by+=10
        bx+=10
        while bx<x:
            if (ennemi.count((bx,by))==1 or allie.count((bx,by))==1):
                return False
            by+=10
            bx+=10
        return True
    elif  by>y and bx<x:
        by-=10
        bx+=10
        while by>y:
            if (ennemi.count((bx,by))==1 or allie.count((bx,by))==1):
                return False
            by-=10
            bx+=10
        return True
    elif by<y  and bx>x :
        by+=10
        bx-=10
        while by<y:
            if (ennemi.count((bx, by))==1 or allie.count((bx,by))==1):
                return False
            by+=10
            bx-=10
        return True

def regle_depl_pions(piece, début, fin, allie, ennemi, piece_id):
    
    """Fonction vérifiant que le déplacement du pion respecte les règles de base
    du jeu d'échec
    
    """
    x,y=début
    bx,by=fin
    i=indice_x(piece, début)
    if allie.count(fin)==0:
        if piece_id==1:
            if verification_kill_pion(fin, ennemi)==False:
                if y==60:
                    if y-by>20 or y-by<=0 or x-bx!=0:
                        return False
                    else:
                        piece[i]=fin
                        return True
                else:
                    if y-by!=10 or x!=bx:
                        return False
                    else:
                        piece[i]=fin
                        return True
            elif verification_kill_pion(fin, ennemi):
                if y-by==10 and x-bx==10:
                    piece[i]=fin

                    return True
                elif y-by==10 and x-bx==-10:
                    piece[i]=fin
                    return True

        elif piece_id==2:
            if  verification_kill_pion(fin, ennemi)==False:
                if y==10:
                    if y-by<-20 or y-by>=0 or x!=bx:
                        return False
                    else:
                        piece[i]=fin
                        return True
                else:
                    if y-by!=-10 or x!=bx:
                        return False
                    else:
                        piece[i]=fin
                        return True
            elif verification_kill_pion(fin, ennemi):
                if y-by==-10 and x-bx==-10:
                    piece[i]=fin
                    return True
                elif y-by==-10 and x-bx==10:
                    piece[i]=fin
                    return True
                else:
                    return False
    else:
        return False

def regle_depl_tour(piece, début, fin, ennemi, allie):
    
    """Fonction ayant le même but que celle pour le pion mais avec la tour
    
    """
    x,y=début
    bx,by=fin
    i=indice_x(piece, début)
    if allie.count(fin)==0:
        if y<80 and x-bx==0:
            if mouv_tour(début,fin,ennemi,allie):
                piece[i]=fin
                return True
        elif y-by==0 and bx<80:
            if mouv_tour(début,fin,ennemi,allie):
                piece[i] = fin
                return True
    return False

def regle_depl_cavalier(piece, début, fin, ennemi, allie):
    
    """Fonction ayant le même but que celle pour le pion mais avec le cavalier
    
    """
    x,y=début
    bx,by=fin
    i=indice_x(piece,début)
    if mouv_cavaliers(début,fin):
        piece[i]=fin
        return True
    return False

def regle_depl_fou(piece, début, fin, ennemi, allie):
    
    """Fonction ayant le même but que celle pour le pion mais avec le fou
    
    """
    x,y=début
    bx,by=fin
    i=indice_x(piece, début)
    if allie.count(fin)==0:
        if y-by==x-bx or y-by==-(x-bx):
            if mouv_fou(début,fin,ennemi,allie):
                piece[i]=fin
                return True
    return False

def regle_depl_reine(piece, début, fin ,ennemi, allie):
    
    """Fonction ayant le même but que celle pour le pion mais avec la reine
    
    """
    x,y=début
    bx,by=fin
    i=indice_x(piece, début)
    if allie.count(fin)==0:
        if y<80 and x-bx==0:
            if mouv_tour(début,fin,ennemi,allie):
                piece[i]=fin
                return True
        elif y-by==0 and bx<80:
            if mouv_tour(début,fin,ennemi,allie):
                piece[i]=fin
                return True
        elif y-by==x-bx or y-by==-(x-bx):
            if mouv_fou(début,fin,ennemi,allie):
                piece[i]=fin
                return True
    return False

def regle_depl_roi(piece, début, fin, ennemi, allie):
    
    """Fonction ayant le même but que celle pour le pion mais avec le Roi
    
    """
    x,y=début
    bx,by=fin
    i=indice_x(piece, début)
    if allie.count(fin)==0:
        if début!=fin:
            if y-by==-10 or y-by==10 or y-by==0:
                if x-bx==10 or x-bx==-10 or x-bx==0:
                    piece[i]=fin
                    return True
    return False
    
def verification_elim_pion(pos, pion, tour, fou, cavalier, reine, roi,morts,joueur,score_blanc,score_noir):
    
    """Fonction entrainant la suppression de la pièce si celle-ci peut etre 
    mangée 
    
    """
    if pion.count(pos)!=0:
        i=indice_x(pion,pos)
        if joueur==1:
            mort='pion_noir'
        else:
            mort='pion_blanc'
        morts.append(mort)
        pion.pop(i)
        return True
    if tour.count(pos)!=0:
        i=indice_x(tour,pos)
        if joueur==1:
            mort='tour_noir'
        else:
            mort='tour_blanc'
        morts.append(mort)
        tour.pop(i)
        return True
    if fou.count(pos)!=0:
        i=indice_x(fou,pos)
        if joueur==1:
            mort='fou_noir'
        else:
            mort='fou_blanc'
        morts.append(mort)
        fou.pop(i)
        return True
    if cavalier.count(pos)!=0:
        i=indice_x(cavalier,pos)
        if joueur==1:
            mort='cavalier_noir'
        else:
            mort='cavalier_blanc'
        morts.append(mort)
        cavalier.pop(i)
        return True
    if reine.count(pos)!=0:
        i=indice_x(reine,pos)
        if joueur==1:
            mort='reine_noir'
        else:
            mort='reine_blanc'
        morts.append(mort)
        reine.pop(i)
        return True
    if roi.count(pos)!=0:
        roi.pop()

def verification_kill_pion(fin, ennemi):
    
    """Fonction permettant de vérifier si une pièce ennemie est sur la diagonale
    d'un pion, si oui, elle renvoie True
    
    """
    if ennemi.count(fin)!=0:
        return True
    else:
        return False

def mouv(joueur, pion, tour, fou, cavalier, reine, roi, début, fin, allie, ennemi,
            pion_2, tour_2, fou_2, cavalier_2, reine_2, roi_2):
                  
    """Fonction recevant la pièce de la case sélectionnée et faisant appel à la 
    fonction validant le déplacement de cette pièce pour valider son déplacement
    
    """
    if pion.count(début)!=0:
        if regle_depl_pions(pion, début, fin, allie, ennemi, joueur):
            verification_elim_pion(fin, pion_2, tour_2, fou_2,
                       cavalier_2, reine_2, roi_2,morts,joueur,score_blanc,score_noir)
            x,y=fin
            if( joueur==1 and y==0) or (joueur==2 and y==70):
                choix_nouv_piece(fin, pion, fou, tour, cavalier, reine)
            return True
            
    elif cavalier.count(début)!=0:
        if regle_depl_cavalier(cavalier, début, fin, ennemi, allie):
            verification_elim_pion(fin, pion_2, tour_2, fou_2,
                       cavalier_2, reine_2, roi_2,morts,joueur,score_blanc,score_noir)
            return True

    elif tour.count(début)!=0:
        if regle_depl_tour(tour, début, fin, ennemi, allie):
            verification_elim_pion(fin, pion_2, tour_2, fou_2,
                       cavalier_2, reine_2, roi_2,morts,joueur,score_blanc,score_noir)
            return True
            
    elif fou.count(début)!=0:
        if regle_depl_fou(fou, début, fin, ennemi, allie):
            verification_elim_pion(fin, pion_2, tour_2, fou_2,
                       cavalier_2, reine_2, roi_2,morts,joueur,score_blanc,score_noir)
            return True

    elif reine.count(début)!=0:
        if regle_depl_reine(reine, début, fin, ennemi, allie):
            verification_elim_pion(fin, pion_2, tour_2, fou_2,
                       cavalier_2, reine_2, roi_2,morts,joueur,score_blanc,score_noir)
            return True

    elif roi.count(début)!=0:
        if regle_depl_roi(roi, début, fin, ennemi, allie):
            verification_elim_pion(fin, pion_2, tour_2, fou_2,
                       cavalier_2, reine_2, roi_2,morts,joueur,score_blanc,score_noir)
            return True

    else:
        return False

def victoire(roi_blanc,roi_noir):
    
    """Fonction vérifiant que le roi est mort, si oui la fonction renvoie true 
    et le jeu s'arrete, l'un des joueurs a gagné
    
    """
    if len(roi_blanc)<=0 or len(roi_noir)<=0:
        return True
        
    # PARTIE 3
    
def choix_nouv_piece(pos, pion, fou, tour, cavalier, reine):
    
    """Fonction permettant à un pion, s'il atteint le bout opposé de son coté 
    initial, de choisir la "réincarnation" d'une piece parmi 4 au choix
    
    """
    rectangle(100,100,700,700, remplissage='white', couleur='black', epaisseur=5)
    rectangle(200,200,300,300, remplissage='white', couleur='black', epaisseur=2)
    image(250, 250, 'données/images/fou_blanc.gif')
    texte(300, 250, 'Fou')
    rectangle(200,300,300,400, remplissage='white', couleur='black', epaisseur=2)
    image(250, 350, 'données/images/tour_blanc.gif')
    texte(300, 350, 'Tour')
    rectangle(200,400,300,500, remplissage='white', couleur='black', epaisseur=2)
    image(250, 450, 'données/images/cavalier_blanc.gif')
    texte(300, 450, 'Cavalier')
    rectangle(200,500,300,600, remplissage='white', couleur='black', epaisseur=2)
    image(250, 550, 'données/images/reine_blanc.gif')
    texte(300, 550, 'Reine')
    choix = attend_clic_gauche()
    x,y=choix
    i=indice_x(pion, pos)
    pion.pop(i)
    if x>=200 and x<=300 and y>=200 and y<=300:
        fou.append(pos)
    if x>=200 and x<=300 and y>=300 and y<=400:
        tour.append(pos)
    if x>=200 and x<=300 and y>=400 and y<=500:
        cavalier.append(pos)
    if x>=200 and x<=300 and y>=500 and y<=600:
        reine.append(pos)

def menu():
    
    """ Fonction permettant d'afficher le menu Pause en offrant deux choix au
    joueur
    
    """
    rectangle(100,100,700,700, remplissage='white', couleur='black', epaisseur=5)
    rectangle(110,110,690,390,couleur='black', epaisseur=5)
    rectangle(110,400,690,690,couleur='black', epaisseur=5)
    texte(280,220,'QUITTER', couleur='black',taille=50)
    texte(170,520,'ANNULER LE COUP', couleur='black',taille=50)
    
def annuler_coup(fin,début,joueur,pion_blanc,tour_blanc, fou_blanc, cavalier_blanc,
                            reine_blanc, roi_blanc, blanc, noir,
                            pion_noir, tour_noir, fou_noir, cavalier_noir,
                            reine_noir, roi_noir):
    """ Fonction permettant d'annuler un coup et de revenir à la case initiale
    
    """
    if joueur==2:
        if pion_blanc.count(fin)!=0:
            i=indice_x(pion_blanc,fin)
            pion_blanc[i]=début
        if tour_blanc.count(fin)!=0:
            i=indice_x(tour_blanc,fin)
            tour_blanc[i]=début
        if fou_blanc.count(fin)!=0:
            i=indice_x(fou_blanc,fin)
            fou_blanc[i]=début
        if cavalier_blanc.count(fin)!=0:
            i=indice_x(cavalier_blanc,fin)
            cavalier_blanc[i]=début
        if reine_blanc.count(fin)!=0:
            i=indice_x(reine_blanc,fin)
            reine_blanc[i]=début
        if roi_blanc.count(fin)!=0:
            i=indice_x(roi_blanc,fin)
            roi_blanc[i]=début
    if joueur==1:
        if pion_noir.count(fin)!=0:
            i=indice_x(pion_noir,fin)
            pion_noir[i]=début
        if tour_noir.count(fin)!=0:
            i=indice_x(tour_noir,fin)
            tour_noir[i]=début
        if fou_noir.count(fin)!=0:
            i=indice_x(fou_noir,fin)
            fou_noir[i]=début
        if cavalier_noir.count(fin)!=0:
            i=indice_x(cavalier_noir,fin)
            cavalier_noir[i]=début
        if reine_noir.count(fin)!=0:
            i=indice_x(reine_noir,fin)
            reine_noir[i]=début
        if roi_noir.count(end)!=0:
            i=indice_x(roi_noir,end)
            roi_noir[i]=début
        
#PROGRAMME PRINCIPAL
        
    #Initialisation de chaque pièce et variable
    
pion_blanc = [(0,60),(10,60),(20,60),(30,60),(40,60),(50,60),(60,60),(70,60)]
pion_noir = [(0,10),(10,10),(20,10),(30,10),(40,10),(50,10),(60,10),(70,10)]
tour_blanc = [(0,70), (70,70)]
tour_noir = [(0,0),(70,0)]
fou_blanc = [(20,70),(50,70)]
fou_noir = [(20,0),(50,0)]
cavalier_blanc = [(10,70),(60,70)]
cavalier_noir = [(10,0),(60,0)]
reine_blanc = [(30, 70)]
reine_noir = [(30, 0)]
roi_blanc = [(40, 70)]
roi_noir = [(40, 0)]
noir=[] #Variable (liste)contenant toutes les coordonnées de chaque pion du jeu noir
blanc=[] #Variable (liste)contenant toutes les coordonnées de chaque pion du jeu blanc
pions_blanc=['pion_blanc','tour_blanc','fou_blanc','cavalier_blanc','reine_blanc']
pions_noir=['pion_noir','tour_noir','fou_noir','cavalier_noir','reine_noir']
score_blanc=0 #nombre de pions mangés par le joueur blanc
score_noir=0 #nombre de pions mangés par le joueur blanc
hauteur_plateau = 120
largeur_plateau = 120
case = 10
morts=[] #liste des pions morts
joueur=1
jeu=False
    
if __name__=="__main__":
    t = "init"
    cree_fenetre(largeur_plateau*case, hauteur_plateau*case )

    #Boucle principale
    
    while True:
        efface_tout()
        
        #Interface de début du jeu
        
        if jeu==False:
            nom_blanc,nom_noir=debut_jeu()
            jeu=True
            efface_tout()
            
        #Ajout de chaque position de chaque pièce de chaque couleur dans les variables (listes) correspondantes
        
        blanc=pion_blanc + tour_blanc + fou_blanc + cavalier_blanc + reine_blanc + roi_blanc
        noir=pion_noir + tour_noir + fou_noir + cavalier_noir + reine_noir + roi_noir

        #Affichage de différentes options
        if jeu==True:
            plateau()
            affiche_score(pions_blanc,pions_noir,morts,score_noir,score_blanc)
            affiche_morts(morts)
            affiche_tours(joueur,nom_blanc,nom_noir)
            affiche_pieces(pion_blanc, pion_noir, "pion_blanc.gif", "pion_noir.gif")
            affiche_pieces(tour_blanc, tour_noir, "tour_blanc.gif","tour_noir.gif")
            affiche_pieces(fou_blanc, fou_noir, "fou_blanc.gif","fou_noir.gif")
            affiche_pieces(cavalier_blanc, cavalier_noir, "cavalier_blanc.gif","cavalier_noir.gif")
            affiche_pieces(reine_blanc, reine_noir, "reine_blanc.gif","reine_noir.gif")
            affiche_pieces(roi_blanc, roi_noir, "roi_blanc.gif", "roi_noir.gif")
            rectangle(820,80,1025,120,'black','red')
            rectangle(820,720,1025,680,'black','red')
            texte(830,85,'PIONS MANGES:')
            texte(830,685,'PIONS MANGES:')
        
        #Vérification victoire de la partie
        
        if victoire(roi_blanc,roi_noir)==True:
            if joueur==1:
                texte(400,430,nom_noir,couleur='black',taille=40,ancrage='center')
                texte(400,480, "A GAGNE!!", couleur ='black', taille=40,ancrage='center')
                attend_clic_gauche()
            elif joueur==2:
                texte(400,430,nom_blanc,couleur='black',taille=40,ancrage='center')
                texte(400,480, "A GAGNE!!", couleur='black', taille=40,ancrage='center')
            attend_clic_gauche()
            break
            
        #Le joueur saisi P pour faire pause, un menu s'offre à lui
        
        ev=attend_ev()
        if touche(ev)=="p":
            menu()
            choix=attend_clic_gauche()
            x,y=choix
            if x<=690 and x>=110 and y>=110 and y<=390:
                break
            elif x>=110 and x<=690 and y>=400 and y<=690:
                annuler_coup(fin,début,joueur,pion_blanc,tour_blanc, fou_blanc, cavalier_blanc,
                            reine_blanc, roi_blanc, blanc, noir,
                            pion_noir, tour_noir, fou_noir, cavalier_noir,
                            reine_noir, roi_noir)
                if joueur==2:
                    if (verification_elim_pion):
                        if len(morts)>0:
                            respawn(morts,joueur,fin)
                    joueur=1
                elif joueur==1:
                    if (verification_elim_pion):
                        if len(morts)>0:
                            respawn(morts,joueur,fin)
                    joueur=2
                continue
        
        #Le joueur selectionne le pion qu'il souhaite déplacer
        
        début=attend_clic_gauche()
        début=nouv_coord(début)
        case_selectionnee(début,jeu)
            
        #Le joueur choisit la destination de sa pièce
        
        if joueur==1:
            fin=attend_clic_gauche()
            fin=nouv_coord(fin)
            if mouv(joueur, pion_blanc,tour_blanc, fou_blanc, cavalier_blanc,
                            reine_blanc, roi_blanc, début, fin, blanc, noir,
                            pion_noir, tour_noir, fou_noir, cavalier_noir,
                            reine_noir, roi_noir):
                joueur=2
                        
        elif joueur==2:
            fin=attend_clic_gauche()
            fin=nouv_coord(fin)
            if mouv(joueur, pion_noir,tour_noir, fou_noir, cavalier_noir,
                        reine_noir, roi_noir, début, fin, noir, blanc,
                        pion_blanc, tour_blanc, fou_blanc, cavalier_blanc,
                        reine_blanc, roi_blanc,):
                joueur=1
        mise_a_jour()
        
#Si le joueur a saisi "p" et "quitter" ou a gagné la partie, la fenêtre se fermera 
ferme_fenetre()
