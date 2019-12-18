# -*- coding: utf-8 -*-
from transition import *
from state import *
import os
import copy
from sp import *
from parser import *
from itertools import product
from automateBase import AutomateBase

class Automate(AutomateBase):
        
    def succElem(self, state, lettre):
        """State x str -> list[State]
        rend la liste des états accessibles à partir d'un état
        state par l'étiquette lettre
        """
        successeurs = []
        # t: Transitions
        for t in self.getListTransitionsFrom(state):
            if t.etiquette == lettre and t.stateDest not in successeurs:
                successeurs.append(t.stateDest)
        return successeurs


    def succ (self, listStates, lettre):
        """list[State] x str -> list[State]
        rend la liste des états accessibles à partir de la liste d'états
        listStates par l'étiquette lettre
        """

        succ = [] 
        ret = []
        tmp = set()
        for i in listStates : #On parcourt l'ensemble des etats de (listState)
            succ = succ + (self.succElem(i,lettre)) #On ajoute a (succ) les etats successeurs des etats de (list)
            tmp = set(succ)
        for j in tmp:
            ret.append(j)
        return ret             




    """ Définition d'une fonction déterminant si un mot est accepté par un automate.
    Exemple :
            a=Automate.creationAutomate("monAutomate.txt")
            if Automate.accepte(a,"abc"):
                print "L'automate accepte le mot abc"
            else:
                print "L'automate n'accepte pas le mot abc"
    """
    @staticmethod
    def accepte(auto,mot) :
        """ Automate x str -> bool
        rend True si auto accepte mot, False sinon
        """
        liste = auto.getListInitialStates() #Liste des etats initial

        for o in mot : #On parcourt les lettres du mot
            liste = auto.succ(liste, o) 
        #liste sera egal à la liste des etats obtenus en appliquant le mot

        #On compare la liste obtenue et la liste des états finaux

        # (ancien code) for i in liste : #On parcourt l'ensemble des etats obtenus
        # (ancien code)     for e in auto.getListFinalStates() : #On parcourt l'ensemble des etats finaux
        # (ancien code)         if i == e : #Si un etat de notre liste est dans la liste des etats finaux
        # (ancien code)             return True 

        #nouveau code (optimiser)
        for i in liste :
            if i in auto.getListFinalStates() :
                return True
        return False


    @staticmethod
    def estComplet(auto,alphabet) :
        """ Automate x str -> bool
         rend True si auto est complet pour alphabet, False sinon
        """
        for lettre in alphabet : #On parcourt l'ensemble des lettres de l'alphabet
            for etat in auto.listStates : #On partcourt l'ensemble des etats
                if auto.succElem(etat, lettre) == [] : #Si un etat successeurs d'un etat est egale à l'ensemble vide (ça veut dire qu'il n'existe pas de transition partant de l'etat avec la lettre)                                 
                    return False
        return True 


        
    @staticmethod
    def estDeterministe(auto) :
        """ Automate  -> bool
        rend True si auto est déterministe, False sinon
        """
        cpt = 0 
        for etat in auto.listStates : #On parcourt l'ensemble des etats
            for transi1 in auto.getListTransitionsFrom(etat) : #On parcourt l'ensemble des transitions de l'etat
                for transi2 in auto.getListTransitionsFrom(etat) : #On parcourt l'ensemble des transitions l'etat
                    if transi1.etiquette == transi2.etiquette : #Si l'etiquette d'une transition est dans la liste des transitions
                        cpt = cpt + 1 #On ajoute +1 si l'etiquette d'une transition est dans la liste des transitions       
                        if cpt >= 2 : #Si cpt >= 2, ça veut dire qu'il existe plusieurs transitions avec la meme etiquette partant d'un etat
                            return False
                cpt = 0
        return True
        

       
    @staticmethod
    def completeAutomate(auto,alphabet) :
        """ Automate x str -> Automate
        rend l'automate complété d'auto, par rapport à alphabet
        hypothèse : on suppose que les ID sont dans l'ordre 0...1...2...n (n étant le dernier état)
        """
        if(auto.estComplet(auto,alphabet)): #Si l'automate est déjà complet, on renvoie le meme automate
            return auto

        # (ancien code) cpt = 0
        # (ancien code) for i in auto.listStates : #On recupere le nombre de states déjà existants
        # (ancien code)     cpt = cpt + 1 
        # (ancien code) puit = State(cpt,False,False) #On construit notre puit

        #nouveau code (optimiser)
        puit = State(len(auto.listStates), False, False)
        auto.addState(puit) #On ajoute notre puit à l'automate

        for lettre in alphabet : #On parcourt l'ensemble des lettres de l'alphabet
            for etat in auto.listStates : #On partcourt l'ensemble des etats
                if auto.succElem(etat, lettre) == [] : #Si un etat successeurs d'un etat est egale à l'ensemble vide (ça veut dire qu'il n'existe pas de transition partant de l'etat avec la lettre)
                    auto.addTransition(Transition(etat, lettre, puit)) #On ajoute une transition partant de l'état concerné allant dans le puit avec la lettre concerné
        return auto

        

    @staticmethod
    def determinisation(auto) :
        """ Automate  -> Automate
        rend l'automate déterminisé d'auto
        """


        #Si l'automate est déterministe, on retourne auto
        if (Automate.estDeterministe(auto)) :
            return auto
        
        #Liste des états finaux de l'automate de départ
        liste_etats_finaux = auto.getListFinalStates()
        #Liste des états d'entree de l'automate de départ
        liste_etats_initiaux = auto.getListInitialStates()
        #Liste des etats du nouvel automate sous la forme list[set[State]]
        liste_new_etat = [set(liste_etats_initiaux)]
        #La liste des transitions du nouvel automate sous la forme list[ list[set[State],str,set[State]] ]
        liste_new_transition = []
        #La liste des états à traiter sous la forme list[list[State]]
        etats_en_cours = [liste_etats_initiaux]
        #L'alphabet de l'automate list[str]
        alphabet = auto.getAlphabetFromTransitions()
        count_nb_etats = 0


        while(len(etats_en_cours) != 0) :

            index_courant = len(etats_en_cours)-1
            #Pour chaque ensemble d'états dans la liste à traiter
            while index_courant >= 0 :
                ens_state = etats_en_cours[index_courant]
                #Liste des transitions de tous les sous_etat
                liste_transitions = []
                #Pour chaque sous_état dans l'ensemble d'états
                for sous_state in ens_state :
                    #On prend les transitions du sous état et on les ajoute à la liste
                    liste_transitions += auto.getListTransitionsFrom(sous_state)

                #Pour chaque lettre de l'alphabet, on va regarder si il y en a une avec une étiquette
                for etiquette in alphabet :
                    #La variable qui va contenir l'ensemble des etats suivants
                    ens_etats_suivants = set()
                    #Pour chaque transition à partir du sous-etat, on check celle(s) qui est associée à une lettre de l'alphabet
                    for transition in liste_transitions :
                        if etiquette == transition.etiquette :
                            ens_etats_suivants.add(transition.stateDest)
                    
                    #On n'ajoute pas un état vide
                    if ens_etats_suivants != set() :
                        #Si l'état n'est pas déjà présent dans la liste des états à traiter, on l'ajoute
                        #Si l'état n'est pas déjà présent dans la liste des états finaux
                        if list(ens_etats_suivants) not in etats_en_cours and ens_etats_suivants not in liste_new_etat :
                            etats_en_cours.append(list(ens_etats_suivants))
                            liste_new_etat.append(ens_etats_suivants)

                        #On ajoute la transition dans la liste des transisions finales
                        liste_new_transition.append([set(ens_state),etiquette,ens_etats_suivants])

                #On retire de la liste l'état que l'on vient de traiter
                etats_en_cours.remove(ens_state)
                #On décrémente l'index courant
                index_courant -= 1

        
        #print(liste_new_etat)
        #print(liste_new_transition)
        #On a donc liste_new_etat = [ {etat0, etat1, ...} , {etat0, ...} ... ]
        #Et on a liste_new_transition = [ [{etat0, etat1, ...}, char, {etat0, ...}], ... ]

        #Liste des transitions qui vont nous permettre de construire le nouvel automate           
        liste_transitions_final_simplifie = []

        #Pour chaque transition que l'on a crée précédemment, il nous faut créer les états qui corresondent 
        for transition in liste_new_transition :
            #Les booléens qui vont renseigner la nature d l'état
            if_etat_init1 = False
            if_etat_final1 = False
            if_etat_init2 = False
            if_etat_final2 = False
            for etat in transition[0] :
                if etat in liste_etats_initiaux :
                    if_etat_init1 = True

                if etat in liste_etats_finaux :
                    if_etat_final1 = True
            
            for etat in transition[2] :
                if etat in liste_etats_initiaux :
                    if_etat_init2 = True
        
                if etat in liste_etats_finaux :
                    if_etat_final2 = True

            etat1 = State(liste_new_etat.index(transition[0]),if_etat_init1,if_etat_final1,transition[0])
            etat2 = State(liste_new_etat.index(transition[2]),if_etat_init2,if_etat_final2,transition[2])
            etiquette = transition[1]
            liste_transitions_final_simplifie.append(Transition(etat1,etiquette,etat2))
                
        
        return Automate(liste_transitions_final_simplifie)


        
    @staticmethod
    def complementaire(auto, alphabet):
        """ Automate x str -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de auto
        """

        auto1 = Automate.determinisation(auto)
        auto2 = Automate.completeAutomate(auto1, alphabet)

        for s in auto2.listStates :
            s.fin = not(s.fin)
        return auto2
   
    @staticmethod
    def intersection (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'intersection des langages des deux automates
        """
        return

    @staticmethod
    def union (auto0, auto1):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage l'union des langages des deux automates
        """
        return
        

   
       

    @staticmethod
    def concatenation (auto1, auto2):
        """ Automate x Automate -> Automate
        rend l'automate acceptant pour langage la concaténation des langages des deux automates
        """
        return
        
       
    @staticmethod
    def etoile (auto):
        """ Automate  -> Automate
        rend l'automate acceptant pour langage l'étoile du langage de a
        """
        return




