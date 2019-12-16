from state import *
from parser import *
from sp import *
from transition import *
from automateBase import *
from automate import *
"""
#-----------------------Automate A-----------------------
#-----------------------Automate A-----------------------
#-----------------------Automate A-----------------------
print("----------Automate A----------")
print("----------Automate A----------")
print("----------Automate A----------")
#Complet et Déterministe
#Etats
aState0 = State(0,True,True)
aState1 = State(1,False,False)
aListe_state = [aState0,aState1]

#Transitions
aTransition0 = Transition(aState0,"a",aState0)
aTransition1 = Transition(aState0,"b",aState1)
aTransition2 = Transition(aState1,"a",aState1)
aTransition3 = Transition(aState1,"b",aState0)
aListe_trans = [aTransition0,aTransition1,aTransition2,aTransition3]

aAutomate = Automate(aListe_trans)
aAutomateComplete = Automate(aListe_trans)
aAutomateDeter = Automate(aListe_trans)
aAutomateComplementaire = Automate(aListe_trans)


print(aAutomate)
aAutomate.show("automateA")
#succ
print("\n")
print("----------succ----------")
print("Quelle est la liste des états à partir de la lettre 'a' ?")
print(aAutomate.succ(aListe_state,"a"))
print("Quelle est la liste des états à partir de la lettre 'b' ?")
print(aAutomate.succ(aListe_state,"b"))

#accepte
print("\n")
print("----------accepte----------")
print("le mot '' (vide) est-il accepté ?")
print(Automate.accepte(aAutomate,""))
print("le mot 'a' est-il accepté ?")
print(Automate.accepte(aAutomate,"a"))
print("le mot 'b' est-il accepté ?")
print(Automate.accepte(aAutomate,"b"))
print("le mot 'aabaabaa' est-il accepté ?")
print(Automate.accepte(aAutomate,"aabaabaa"))
print("le mot 'babab' est-il accepté ?")
print(Automate.accepte(aAutomate,"babab"))

#estComplet
print("\n")
print("----------estComplet----------")
print("l'automate Automate A est-il complet ?")
print(Automate.estComplet(aAutomate,"ab"))

#estDeterministe
print("\n")
print("----------estDeterministe----------")
print("l'automate Automate A est-il déterministe ?")
print(Automate.estDeterministe(aAutomate))

#completeAutomate
print("\n")
print("----------completeAutomate----------")
print("Voici l'automate complété :")
print(Automate.completeAutomate(aAutomateComplete,"ab"))

#determinisation
print("\n")
print("----------determinisation----------")
print("Voici l'automate determinisé :")
print(Automate.determinisation(aAutomateDeter))

#complementaire
print("\n")
print("----------complementaire----------")
print("Voici l'automate complementaire :")
print(Automate.complementaire(aAutomateComplementaire,"ab"))
"""
#-----------------------Automate B-----------------------
#-----------------------Automate B-----------------------
#-----------------------Automate B-----------------------
print("\n")
print("----------Automate B----------")
print("----------Automate B----------")
print("----------Automate B----------")
#Pas Complet et Non Déterministe
#Etats
bState0 = State(0,True,False)
bState1 = State(1,False,False)
bState2 = State(2,False,False)
bState3 = State(3,False,True)
bListe_state = [bState0,bState1,bState2,bState3]

#Transitions
bTransition0 = Transition(bState0,"a",bState0)
bTransition1 = Transition(bState0,"b",bState0)
bTransition2 = Transition(bState0,"a",bState1)
bTransition3 = Transition(bState1,"a",bState2)
bTransition4 = Transition(bState2,"a",bState3)
bTransition5 = Transition(bState3,"a",bState3)
bTransition6 = Transition(bState3,"b",bState3)

bListe_trans = [bTransition0,bTransition1,bTransition2,bTransition3,bTransition4,bTransition5,bTransition6]

bAutomate = Automate(bListe_trans)
bAutomateComplete = Automate(bListe_trans)
bAutomateDeter = Automate(bListe_trans)
bAutomateComplementaire = Automate(bListe_trans)

print(bAutomate)
bAutomate.show("automateB")

#succ
print("\n")
print("----------succ----------")
print("Quelle est la liste des états à partir de la lettre 'a' ?")
print(bAutomate.succ(bListe_state,"a"))
print("Quelle est la liste des états à partir de la lettre 'b' ?")
print(bAutomate.succ(bListe_state,"b"))

#accepte
print("\n")
print("----------accepte----------")
print("le mot '' (vide) est-il accepté ?")
print(Automate.accepte(bAutomate,""))
print("le mot 'a' est-il accepté ?")
print(Automate.accepte(bAutomate,"a"))
print("le mot 'b' est-il accepté ?")
print(Automate.accepte(bAutomate,"b"))
print("le mot 'aabaabaa' est-il accepté ?")
print(Automate.accepte(bAutomate,"aabaabaa"))
print("le mot 'aaa' est-il accepté ?")
print(Automate.accepte(bAutomate,"aaa"))
print("le mot 'aabaaabbbba' est-il accepté ?")
print(Automate.accepte(bAutomate,"aabaaabbbba"))

#estComplet
print("\n")
print("----------estComplet----------")
print("l'automate Automate B est-il complet ?")
print(Automate.estComplet(bAutomate,"ab"))

#estDeterministe
print("\n")
print("----------estDeterministe----------")
print("l'automate Automate B est-il déterministe ?")
print(Automate.estDeterministe(bAutomate))

#completeAutomate
print("\n")
print("----------completeAutomate----------")
print("Voici l'automate complété :")
print(Automate.completeAutomate(bAutomateComplete,"ab"))
Automate.completeAutomate(bAutomateComplete,"ab").show("CompletAutomateB")

#determinisation
print("\n")
print("----------determinisation----------")
print("Voici l'automate determinisé :")
print(Automate.determinisation(bAutomateDeter))
Automate.determinisation(bAutomateDeter).show("DeterAutomateB")

#complementaire
print("\n")
print("----------complementaire----------")
print("Voici l'automate complementaire :")
print(Automate.complementaire(bAutomateComplementaire,"ab"))
Automate.complementaire(bAutomateComplementaire,"ab").show("ComplementaireAutomateB")

"""
#-----------------------Automate C-----------------------
#-----------------------Automate C-----------------------
#-----------------------Automate C-----------------------
print("\n")
print("----------Automate C----------")
print("----------Automate C----------")
print("----------Automate C----------")
#Complet et Non Déterministe
#Etats
cState0 = State(0,True,False)
cState1 = State(1,False,True)
cListe_state = [cState0,cState1]

#Transitions
cTransition0 = Transition(cState0,"a",cState0)
cTransition1 = Transition(cState0,"b",cState0)
cTransition2 = Transition(cState0,"c",cState0)
cTransition3 = Transition(cState0,"a",cState1)
cTransition4 = Transition(cState1,"a",cState1)
cTransition5 = Transition(cState1,"b",cState1)
cTransition6 = Transition(cState1,"c",cState1)

cListe_trans = [cTransition0,cTransition1,cTransition2,cTransition3,cTransition4,cTransition5,cTransition6]

cAutomate = Automate(cListe_trans)
cAutomateComplete = Automate(cListe_trans)
cAutomateDeter = Automate(cListe_trans)
cAutomateComplementaire = Automate(cListe_trans)

print(cAutomate)
cAutomate.show("automateC")

#succ
print("\n")
print("----------succ----------")
print("Quelle est la liste des états à partir de la lettre 'a' ?")
print(cAutomate.succ(cListe_state,"a"))
print("Quelle est la liste des états à partir de la lettre 'b' ?")
print(cAutomate.succ(cListe_state,"b"))
print("Quelle est la liste des états à partir de la lettre 'c' ?")
print(cAutomate.succ(cListe_state,"c"))

#accepte
print("\n")
print("----------accepte----------")
print("le mot '' (vide) est-il accepté ?")
print(Automate.accepte(cAutomate,""))
print("le mot 'a' est-il accepté ?")
print(Automate.accepte(cAutomate,"a"))
print("le mot 'b' est-il accepté ?")
print(Automate.accepte(cAutomate,"b"))
print("le mot 'c' est-il accepté ?")
print(Automate.accepte(cAutomate,"c"))
print("le mot 'abc' est-il accepté ?")
print(Automate.accepte(cAutomate,"abc"))
print("le mot 'bbcc' est-il accepté ?")
print(Automate.accepte(cAutomate,"bbcc"))
print("le mot 'cbbcacbbc' est-il accepté ?")
print(Automate.accepte(cAutomate,"cbbcacbbc"))

#estComplet
print("\n")
print("----------estComplet----------")
print("l'automate Automate C est-il complet ?")
print(Automate.estComplet(cAutomate,"abc"))

#estDeterministe
print("\n")
print("----------estDeterministe----------")
print("l'automate Automate C est-il déterministe ?")
print(Automate.estDeterministe(cAutomate))

#completeAutomate
print("\n")
print("----------completeAutomate----------")
print("Voici l'automate complété :")
print(Automate.completeAutomate(cAutomateComplete,"abc"))
#            Automate.completeAutomate(cAutomateComplete,"ab").show("CompletAutomateC")

#determinisation
print("\n")
print("----------determinisation----------")
print("Voici l'automate determinisé :")
print(Automate.determinisation(cAutomateDeter))
Automate.determinisation(cAutomateDeter).show("DeterAutomateC")

#complementaire
print("\n")
print("----------complementaire----------")
print("Voici l'automate complementaire :")
print(Automate.complementaire(cAutomateComplementaire,"abc"))

#-----------------------Automate D-----------------------
#-----------------------Automate D-----------------------
#-----------------------Automate D-----------------------
print("\n")
print("----------Automate D----------")
print("----------Automate D----------")
print("----------Automate D----------")
#Pas Complet et Déterministe
#Etats
dState0 = State(0,True,False)
dState1 = State(1,False,False)
dState2 = State(2,False,False)
dState3 = State(3,False,True)
dListe_state = [dState0,dState1,dState2,dState3]

#Transitions
dTransition0 = Transition(dState0,"b",dState1)
dTransition1 = Transition(dState1,"a",dState2)
dTransition2 = Transition(dState2,"c",dState3)

dListe_trans = [dTransition0,dTransition1,dTransition2]

dAutomate = Automate(dListe_trans)
dAutomateComplete = Automate(dListe_trans)
dAutomateDeter = Automate(dListe_trans)
dAutomateComplementaire = Automate(dListe_trans)

print(dAutomate)
dAutomate.show("automateD")

#succ
print("\n")
print("----------succ----------")
print("Quelle est la liste des états à partir de la lettre 'a' ?")
print(dAutomate.succ(dListe_state,"a"))
print("Quelle est la liste des états à partir de la lettre 'b' ?")
print(dAutomate.succ(dListe_state,"b"))
print("Quelle est la liste des états à partir de la lettre 'c' ?")
print(dAutomate.succ(dListe_state,"c"))

#accepte
print("\n")
print("----------accepte----------")
print("le mot '' (vide) est-il accepté ?")
print(Automate.accepte(dAutomate,""))
print("le mot 'a' est-il accepté ?")
print(Automate.accepte(dAutomate,"a"))
print("le mot 'b' est-il accepté ?")
print(Automate.accepte(dAutomate,"b"))
print("le mot 'c' est-il accepté ?")
print(Automate.accepte(dAutomate,"c"))
print("le mot 'abc' est-il accepté ?")
print(Automate.accepte(dAutomate,"abc"))
print("le mot 'bac' est-il accepté ?")
print(Automate.accepte(dAutomate,"bac"))

#estComplet
print("\n")
print("----------estComplet----------")
print("l'automate Automate D est-il complet ?")
print(Automate.estComplet(dAutomate,"abc"))

#estDeterministe
print("\n")
print("----------estDeterministe----------")
print("l'automate Automate C est-il déterministe ?")
print(Automate.estDeterministe(dAutomate))

#completeAutomate
print("\n")
print("----------completeAutomate----------")
print("Voici l'automate complété :")
print(Automate.completeAutomate(dAutomateComplete,"abc"))
Automate.completeAutomate(dAutomateComplete,"abc").show("CompletAutomateD")

#determinisation
print("\n")
print("----------determinisation----------")
print("Voici l'automate determinisé :")
print(Automate.determinisation(dAutomateDeter))
Automate.determinisation(dAutomateDeter).show("DeterAutomateD")

#complementaire
print("\n")
print("----------complementaire----------")
print("Voici l'automate complementaire :")
print(Automate.complementaire(dAutomateComplementaire,"abc"))
Automate.complementaire(dAutomateComplementaire,"abc").show("ComplementaireAutomateD")
"""
