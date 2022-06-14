##Representation en STRIPS de Helltaker##

#Predicats#
_empty/2_
_demoness/2_

#Fluents#
_man/2_
_block/2_
_skeleton/2_
_safe-trap/2_
_unsafe-trap/2_
_lock/2_
_key/2_
_time/1_ :
_haskey/1_


#Fonctions utiles#
_next/2_ : next(x,x') => x = x'+ 1

#Etat initial#

_is(X,Y)_
_demoness(...)_

#Objectif#

arriver a la case a cote du démon :

#les actions#

- do(moveup,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y') ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ ¬lock(x,y') ∧ ¬key(x,y') ∧ ¬demoness(x,y')
  Effets:
    man(x,y') ∧ ¬man(x,y)) ∧ time(t+1)

- do(movedown,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ ¬lock(x,y') ∧ ¬demoness(x,y') ∧ ¬key(x,y')
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t+1)

- do(moveleft,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ ¬lock(x',y) ∧ ¬demoness(x',y) ∧ ¬key(x',y)
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t+1)

- do(moveright,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ ¬lock(x',y) ∧ ¬demoness(x',y) ∧ ¬key(x',y)
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t+1)

____

- do(pushblockup,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ block(x,y') ∧ ¬block(x,y") ∧ empty(x,y") ∧ ¬skeleton(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets:
    ¬block(x,y') ∧ block(x,y") ∧ time(t+1)

- do(pushblockdown,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ block(x,y') ∧ ¬block(x,y") ∧ empty(x,y") ∧ ¬skeleton(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets :
    ¬block(x,y') ∧ block(x,y") ∧ time(t+1)

- do(pushblockleft,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ block(x',y) ∧ ¬block(x",y) ∧ empty(x",y) ∧ ¬skeleton(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    ¬block(x',y) ∧ block(x",y) ∧ time(t+1)

- do(pushblockright,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ block(x',y) ∧ ¬block(x",y) ∧ empty(x",y) ∧ ¬skeleton(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    ¬block(x',y) ∧ block(x",y) ∧ time(t+1)

___

- do(pushskeletonup,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ empty(x,y") ∧ ¬squeleton(x,y") ∧ ¬block(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets:
    ¬skeleton(x,y') ∧ skeleton(x,y") ∧ time(t+1)

- do(pushskeletondown,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ empty(x,y") ∧ ¬squeleton(x,y") ∧ ¬block(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets :
    ¬skeleton(x,y') ∧ skeleton(x,y") ∧ time(t+1)

- do(pushskeletonleft,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ empty(x",y) ∧ ¬squeleton(x",y) ∧ ¬block(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    ¬skeleton(x',y) ∧ skeleton(x",y) ∧ time(t+1)

- do(pushskeletonright,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ empty(x",y) ∧ ¬squeleton(x",y) ∧ ¬block(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    ¬skeleton(x',y) ∧ skeleton(x",y) ∧ time(t+1)

___

- do(pushskeleton_on_trap_up,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ empty(x,y") ∧ skeleton(x,y') ∧ trap(x,y") ∧ ¬block(x,y") ∧ ¬lock(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t+1)

- do(pushskeleton_on_trap_down,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ empty(x,y") ∧ skeleton(x,y') ∧ empty(x,y") ∧ ¬block(x,y') ∧ ¬lock(x,y')
  Effets :
    ¬skeleton(x,y') ∧ time(t+1)

- do(pushskeleton_on_trap_left,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ empty(x",y) ∧ skeleton(x',y) ∧ empty(x",y) ∧ ¬block(x',y) ∧ ¬lock(x',y)
  Effets :
    ¬skeleton(x',y) ∧ time(t+1)

- do(pushskeleton_on_trap_right,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ empty(x",y) ∧ skeleton(x',y) ∧ empty(x",y) ∧ ¬block(x',y) ∧ ¬lock(x',y)
  Effets :
    ¬skeleton(x',y) ∧ time(t+1)

____

- do(pushskeleton_on_wall_up,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ ¬empty(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t+1)

- do(pushskeleton_on_wall_down,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ ¬empty(x,y")
  Effets :
    ¬skeleton(x,y') ∧ time(t+1)

- do(pushskeleton_on_wall_left,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ ¬empty(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t+1)

- do(pushskeleton_on_wall_right,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ ¬empty(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t+1)

___

- do(pushskeletonup_on_block_up,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ block(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t+1)

- do(pushskeleton_on_block_down,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ block(x,y")
  Effets :
    ¬skeleton(x,y') ∧ time(t+1)

- do(pushskeleton_on_block_left,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ block(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t+1)

- do(pushskeleton_on_block_right,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ block(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t+1)

____

- do(pushskeleto_on_lock_up,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ lock(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t+1)

- do(pushskeleton_on_lock_down,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ lock(x,y")
  Effets :
    ¬skeleton(x,y') ∧ time(t+1)

- do(pushskeleton_on_lock_left,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ lock(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t+1)

- do(pushskeleton_on_lock_right,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ lock(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t+1)

___

- do(pushskeleton_on_skeleton_up,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ skeleton(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t+1)

- do(pushskeleton_on_skeleton_down,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ skeleton(x,y")
  Effets :
    ¬skeleton(x,y') ∧ time(t+1)

- do(pushskeleton_on_skeleton_left,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ skeleton(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t+1)

- do(pushskeleton_on_skeleton_right,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ skeleton(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t+1)


--------------------------------------------------------------------------------------------------------------

Obtenir une Clé : Action? ou juste un booléen dans programme?

Action(ObtenirCléD(x,y),
PRECOND: perso(x,y) ∧ inc(y,y') ∧ clé(x,y') ∧ ¬block(x,y') ∧ ¬skeleton(x,y')
EFFECT : perso(x,y')∧ ¬perso(x,y))

Action(ObtenirCléG(x,y),
PRECOND: perso(x,y) ∧ inc(y',y) ∧ clé(x,y') ∧ ¬block(x,y') ∧ ¬skeleton(x,y')
EFFECT : perso(x,y')∧ ¬perso(x,y))

Action(ObtenirCléH(x,y),
PRECOND: perso(x,y) ∧ inc(x',x) ∧ clé(x',y)∧ ¬block(x',y) ∧ ¬skeleton(x',y)
EFFECT : perso(x',y)∧ ¬perso(x,y))

Action(ObtenirCléB(x,y),
PRECOND: perso(x,y) ∧ inc(x,x') ∧ clé(x',y) ∧ ¬block(x',y) ∧ ¬skeleton(x',y)
EFFECT : perso(x',y)∧ ¬perso(x,y))

-----------------------------------------------------------------------------------------------------------------

Ouvrir une lock avec la clé : aClé est littéral qui dit si on a une clé ou pas!

Action(OuvrirlockD(x,y),
PRECOND: perso(x,y) ∧ inc(y,y') ∧ aClé ∧ lock(x,y')
EFFECT : perso(x,y')∧ ¬perso(x,y) ∧ ¬aClé ∧ ¬lock(x,y'))

Action(OuvrirlockG(x,y),
PRECOND: perso(x,y) ∧ inc(y',y) ∧ aClé ∧ lock(x,y')
EFFECT : perso(x,y')∧ ¬perso(x,y) ∧ ¬aClé ∧ ¬lock(x,y'))

Action(OuvrirlockH(x,y),
PRECOND: perso(x,y) ∧ inc(x',x) ∧ aClé ∧ lock(x',y)
EFFECT : perso(x',y)∧ ¬perso(x,y) ∧ ¬aClé ∧ ¬lock(x',y))

Action(OuvrirlockB(x,y),
PRECOND: perso(x,y) ∧ inc(x,x') ∧ aClé ∧ lock(x',y)
EFFECT : perso(x',y)∧ ¬perso(x,y) ∧ ¬aClé ∧ ¬lock(x',y))

---------------------------------------------------------------------------------------------------------------

Taper le Block (le block ne bouge pas, le perso non plus, on a juste utilisé un coup pour perdre du temps : si bloc,mur ou skeleton derrière)

Action(PushBlockContreBlockD(x,y),
PRECOND: perso(x,y) ∧ inc(y,y') ∧ inc(y',y") ∧ block(x,y')∧ block(x,y")
EFFECT : )

Action(PushBlockContreBlockG(x,y),
PRECOND: perso(x,y) ∧ inc(y',y) ∧ inc(y",y') ∧ block(x,y') ∧ block(x,y")
EFFECT : )

Action(PushBlockContreBlockH(x,y),
PRECOND: perso(x,y) ∧ inc(x',x) ∧ inc(x",x') ∧ block(x",y) ∧ block(x',y)
EFFECT : block(x",y) ∧ ¬block(x',y))

Action(PushBlockContreBlockB(x,y),
PRECOND: perso(x,y) ∧ inc(x,x') ∧ inc(x,x") ∧block(x',y) ∧ block(x",y)
EFFECT : )


--Pareil mais pour skeleton :

Action(PushBlockContreskeletonD(x,y),
PRECOND: perso(x,y) ∧ inc(y,y') ∧ inc(y',y") ∧ block(x,y')∧ skeleton(x,y")
EFFECT : )

Action(PushBlockContreskeletonG(x,y),
PRECOND: perso(x,y) ∧ inc(y',y) ∧ inc(y",y') ∧ block(x,y') ∧ skeleton(x,y")
EFFECT : )

Action(PushBlockContreskeletonH(x,y),
PRECOND: perso(x,y) ∧ inc(x',x) ∧ inc(x",x') ∧ skeleton(x",y) ∧ block(x',y)
EFFECT : block(x",y) ∧ ¬block(x',y))

Action(PushBlockContreskeletonB(x,y),
PRECOND: perso(x,y) ∧ inc(x,x') ∧ inc(x,x") ∧block(x',y) ∧ skeleton(x",y)
EFFECT : )


--Pareil mais pour Mur :

Action(PushBlockContreMurD(x,y),
PRECOND: perso(x,y) ∧ inc(y,y') ∧ inc(y',y") ∧ block(x,y')∧ mur(x,y")
EFFECT : )

Action(PushBlockContreMurG(x,y),
PRECOND: perso(x,y) ∧ inc(y',y) ∧ inc(y",y') ∧ block(x,y') ∧ mur(x,y")
EFFECT : )

Action(PushBlockContreMurH(x,y),
PRECOND: perso(x,y) ∧ inc(x',x) ∧ inc(x",x') ∧ mur(x",y) ∧ block(x',y)
EFFECT : block(x",y) ∧ ¬block(x',y))

Action(PushBlockContreMurB(x,y),
PRECOND: perso(x,y) ∧ inc(x,x') ∧ inc(x,x") ∧block(x',y) ∧ mur(x",y)
EFFECT : )

--Pareil mais pour lock :

Action(PushBlockContrelockD(x,y),
PRECOND: perso(x,y) ∧ inc(y,y') ∧ inc(y',y") ∧ block(x,y')∧ lock(x,y")
EFFECT : )

Action(PushBlockContrelockG(x,y),
PRECOND: perso(x,y) ∧ inc(y',y) ∧ inc(y",y') ∧ block(x,y') ∧ lock(x,y")
EFFECT : )

Action(PushBlockContrelockH(x,y),
PRECOND: perso(x,y) ∧ inc(x',x) ∧ inc(x",x') ∧ lock(x",y) ∧ block(x',y)
EFFECT : block(x",y) ∧ ¬block(x',y))

Action(PushBlockContrelockB(x,y),
PRECOND: perso(x,y) ∧ inc(x,x') ∧ inc(x,x") ∧block(x',y) ∧ lock(x",y)
EFFECT : )

#DIFFERENCES AVEC SOKOBAN :#

Sokoban ne permet que de pousser les caisses et de deplacer le personnage. Ici :

- Pousser une "caisse" coute une action à part entière. Le bonhomme n'avance pas.
- On peut casser un certain type de caisse, les "skeletons", en les poussant contre des objets fixes.
- Certaines cases sont parfois piégées, parfois non. Cela se fait indépendamment de la décision du joueur!
- Un bloc peut être sur un piège
- Il y a une notion de clé, qui permet qu'un "mur" n'en soit plus un.

SURTOUT :
- Le but n'est pas de disposer les caisses à un endroit précis, mais bien de mettre le personnage sur une case adjacente à la sortie (ou mettre 3 ou 4 sorties).
