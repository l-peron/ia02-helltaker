**Representation en STRIPS de Helltaker**

Predicats :
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
    man(x,y') ∧ ¬man(x,y)) ∧ time(t-1)

- do(movedown,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ ¬lock(x,y') ∧ ¬demoness(x,y') ∧ ¬key(x,y')
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-1)

- do(moveleft,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ ¬lock(x',y) ∧ ¬demoness(x',y) ∧ ¬key(x',y)
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-1)

- do(moveright,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ ¬lock(x',y) ∧ ¬demoness(x',y) ∧ ¬key(x',y)
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-1)

____

- do(kickblockup,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ block(x,y') ∧ ¬block(x,y") ∧ empty(x,y") ∧ ¬skeleton(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets:
    ¬block(x,y') ∧ block(x,y") ∧ time(t-1)

- do(kickblockdown,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ block(x,y') ∧ ¬block(x,y") ∧ empty(x,y") ∧ ¬skeleton(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets :
    ¬block(x,y') ∧ block(x,y") ∧ time(t-1)

- do(kickblockleft,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ block(x',y) ∧ ¬block(x",y) ∧ empty(x",y) ∧ ¬skeleton(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    ¬block(x',y) ∧ block(x",y) ∧ time(t-1)

- do(kickblockright,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ block(x',y) ∧ ¬block(x",y) ∧ empty(x",y) ∧ ¬skeleton(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    ¬block(x',y) ∧ block(x",y) ∧ time(t-1)

___

- do(kickskeletonup,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ empty(x,y") ∧ ¬squeleton(x,y") ∧ ¬block(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets:
    ¬skeleton(x,y') ∧ skeleton(x,y") ∧ time(t-1)

- do(kickskeletondown,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ empty(x,y") ∧ ¬squeleton(x,y") ∧ ¬block(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets :
    ¬skeleton(x,y') ∧ skeleton(x,y") ∧ time(t-1)

- do(kickskeletonleft,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ empty(x",y) ∧ ¬squeleton(x",y) ∧ ¬block(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    ¬skeleton(x',y) ∧ skeleton(x",y) ∧ time(t-1)

- do(kickskeletonright,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ empty(x",y) ∧ ¬squeleton(x",y) ∧ ¬block(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    ¬skeleton(x',y) ∧ skeleton(x",y) ∧ time(t-1)

___

- do(kickskeleton_on_trap_up,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ empty(x,y") ∧ skeleton(x,y') ∧ trap(x,y") ∧ ¬block(x,y") ∧ ¬lock(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t-1)

- do(kickskeleton_on_trap_down,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ empty(x,y") ∧ skeleton(x,y') ∧ empty(x,y") ∧ ¬block(x,y') ∧ ¬lock(x,y')
  Effets :
    ¬skeleton(x,y') ∧ time(t-1)

- do(kickskeleton_on_trap_left,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ empty(x",y) ∧ skeleton(x',y) ∧ empty(x",y) ∧ ¬block(x',y) ∧ ¬lock(x',y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

- do(kickskeleton_on_trap_right,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ empty(x",y) ∧ skeleton(x',y) ∧ empty(x",y) ∧ ¬block(x',y) ∧ ¬lock(x',y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

____

- do(kickskeleton_on_wall_up,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ ¬empty(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t-1)

- do(kickskeleton_on_wall_down,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ ¬empty(x,y")
  Effets :
    ¬skeleton(x,y') ∧ time(t-1)

- do(kickskeleton_on_wall_left,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ ¬empty(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

- do(kickskeleton_on_wall_right,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ ¬empty(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

___

- do(kickskeletonup_on_block_up,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ block(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t-1)

- do(kickskeleton_on_block_down,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ block(x,y")
  Effets :
    ¬skeleton(x,y') ∧ time(t-1)

- do(kickskeleton_on_block_left,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ block(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

- do(kickskeleton_on_block_right,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ block(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

____

- do(kickskeleto_on_lock_up,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ lock(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t-1)

- do(kickskeleton_on_lock_down,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ lock(x,y")
  Effets :
    ¬skeleton(x,y') ∧ time(t-1)

- do(kickskeleton_on_lock_left,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ lock(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

- do(kickskeleton_on_lock_right,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ lock(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

___

- do(kickskeleton_on_skeleton_up,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ skeleton(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t-1)

- do(kickskeleton_on_skeleton_down,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ skeleton(x,y")
  Effets :
    ¬skeleton(x,y') ∧ time(t-1)

- do(kickskeleton_on_skeleton_left,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ skeleton(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

- do(kickskeleton_on_skeleton_right,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ skeleton(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

___

- do(getkeyup,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y') ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ ¬lock(x,y') ∧ key(x,y') ∧ ¬demoness(x,y')
  Effets:
    man(x,y') ∧ ¬man(x,y)) ∧ time(t-1) ∧ haskey(1)

- do(getkeydown,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ ¬lock(x,y') ∧ ¬demoness(x,y') ∧ key(x,y')
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-1) ∧ haskey(1)

- do(getkeyleft,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ ¬lock(x',y) ∧ ¬demoness(x',y) ∧ key(x',y)
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-1) ∧ haskey(1)

- do(getkeyright,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ ¬lock(x',y) ∧ ¬demoness(x',y) ∧ key(x',y)
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-1) ∧ haskey(1)

___

- do(openlockup,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y') ∧ haskey(1) ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ lock(x,y') ∧ ¬demoness(x,y')
  Effets:
    time(t-1) ∧ ¬lock(x,y')

- do(openlockdown,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ haskey(1) ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ lock(x,y') ∧ ¬demoness(x,y')
  Effets :
    time(t-1) ∧ ¬lock(x,y')

- do(openlockleft,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ haskey(1) ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ lock(x',y) ∧ ¬demoness(x',y)
  Effets :
    time(t-1) ∧ ¬lock(x',y)

- do(openlockright,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x)  ∧ haskey(1) ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ lock(x',y) ∧ ¬demoness(x',y)
  Effets :
    time(t-1) ∧ ¬lock(x',y)

___

- do(kickblock_on_obstacle_up,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ block(x,y') ∧ ¬block(x,y") ∧ empty(x,y") ∧ ¬skeleton(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets:
    time(t-1)

- do(kickblock_on_obstacle_down,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ block(x,y') ∧ ¬block(x,y") ∧ empty(x,y") ∧ ¬skeleton(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets :
    time(t-1)

- do(kickblock_on_obstacle_left,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ block(x',y) ∧ ¬block(x",y) ∧ empty(x",y) ∧ ¬skeleton(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    time(t-1)

- do(kickblock_on_obstacle_right,(x,y),(x',y'),time(t))
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ block(x',y) ∧ ¬block(x",y) ∧ empty(x",y) ∧ ¬skeleton(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    time(t-1)

Taper le Block (le block ne bouge pas, le perso non plus, on a juste utilisé un coup pour perdre du temps : si bloc,mur ou skeleton derrière)

Action(kickBlockContreBlockD(x,y),
PRECOND: perso(x,y) ∧ inc(y,y') ∧ inc(y',y") ∧ block(x,y')∧ block(x,y")
EFFECT : )

Action(kickBlockContreBlockG(x,y),
PRECOND: perso(x,y) ∧ inc(y',y) ∧ inc(y",y') ∧ block(x,y') ∧ block(x,y")
EFFECT : )

Action(kickBlockContreBlockH(x,y),
PRECOND: perso(x,y) ∧ inc(x',x) ∧ inc(x",x') ∧ block(x",y) ∧ block(x',y)
EFFECT : block(x",y) ∧ ¬block(x',y))

Action(kickBlockContreBlockB(x,y),
PRECOND: perso(x,y) ∧ inc(x,x') ∧ inc(x,x") ∧block(x',y) ∧ block(x",y)
EFFECT : )


--Pareil mais pour skeleton :

Action(kickBlockContreskeletonD(x,y),
PRECOND: perso(x,y) ∧ inc(y,y') ∧ inc(y',y") ∧ block(x,y')∧ skeleton(x,y")
EFFECT : )

Action(kickBlockContreskeletonG(x,y),
PRECOND: perso(x,y) ∧ inc(y',y) ∧ inc(y",y') ∧ block(x,y') ∧ skeleton(x,y")
EFFECT : )

Action(kickBlockContreskeletonH(x,y),
PRECOND: perso(x,y) ∧ inc(x',x) ∧ inc(x",x') ∧ skeleton(x",y) ∧ block(x',y)
EFFECT : block(x",y) ∧ ¬block(x',y))

Action(kickBlockContreskeletonB(x,y),
PRECOND: perso(x,y) ∧ inc(x,x') ∧ inc(x,x") ∧block(x',y) ∧ skeleton(x",y)
EFFECT : )


--Pareil mais pour Mur :

Action(kickBlockContreMurD(x,y),
PRECOND: perso(x,y) ∧ inc(y,y') ∧ inc(y',y") ∧ block(x,y')∧ mur(x,y")
EFFECT : )

Action(kickBlockContreMurG(x,y),
PRECOND: perso(x,y) ∧ inc(y',y) ∧ inc(y",y') ∧ block(x,y') ∧ mur(x,y")
EFFECT : )

Action(kickBlockContreMurH(x,y),
PRECOND: perso(x,y) ∧ inc(x',x) ∧ inc(x",x') ∧ mur(x",y) ∧ block(x',y)
EFFECT : block(x",y) ∧ ¬block(x',y))

Action(kickBlockContreMurB(x,y),
PRECOND: perso(x,y) ∧ inc(x,x') ∧ inc(x,x") ∧block(x',y) ∧ mur(x",y)
EFFECT : )

--Pareil mais pour lock :

Action(kickBlockContrelockD(x,y),
PRECOND: perso(x,y) ∧ inc(y,y') ∧ inc(y',y") ∧ block(x,y')∧ lock(x,y")
EFFECT : )

Action(kickBlockContrelockG(x,y),
PRECOND: perso(x,y) ∧ inc(y',y) ∧ inc(y",y') ∧ block(x,y') ∧ lock(x,y")
EFFECT : )

Action(kickBlockContrelockH(x,y),
PRECOND: perso(x,y) ∧ inc(x',x) ∧ inc(x",x') ∧ lock(x",y) ∧ block(x',y)
EFFECT : block(x",y) ∧ ¬block(x',y))

Action(kickBlockContrelockB(x,y),
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
