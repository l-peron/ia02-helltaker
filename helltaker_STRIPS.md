# Representation en STRIPS de Helltaker

Predicats :
_empty/2_
_demoness/2_

## Fluents
_man/2_
_block/2_
_skeleton/2_
_safe-trap/2_
_unsafe-trap/2_
_lock/2_
_key/2_
_time/1_ :
_haskey/1_


Fonctions utiles
_next/2_ : next(x,x') => x = x'+ 1

## Etat initial

_is(X,Y)_
_demoness(...)_

## Objectif

arriver a la case a cote du démon :

## les actions

- act(moveup,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y') ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ ¬lock(x,y') ∧ ¬key(x,y') ∧ ¬demoness(x,y')
  Effets:
    man(x,y') ∧ ¬man(x,y)) ∧ time(t-1)

- act(movedown,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ ¬lock(x,y') ∧ ¬demoness(x,y') ∧ ¬key(x,y')
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-1)

- act(moveleft,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ ¬lock(x',y) ∧ ¬demoness(x',y) ∧ ¬key(x',y)
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-1)

- act(moveright,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ ¬lock(x',y) ∧ ¬demoness(x',y) ∧ ¬key(x',y)
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-1)

____

- act(moveontrap_up,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y') ∧ trap(x,y') ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ ¬lock(x,y') ∧ ¬key(x,y') ∧ ¬demoness(x,y')
  Effets:
    man(x,y') ∧ ¬man(x,y)) ∧ time(t-2)

- act(moveontrap_down,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ trap(x,y') ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ ¬lock(x,y') ∧ ¬demoness(x,y') ∧ ¬key(x,y')
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-2)

- act(moveontrap_left,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ trap(x',y) ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ ¬lock(x',y) ∧ ¬demoness(x',y) ∧ ¬key(x',y)
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-2)

- act(moveontrap_right,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ trap(x',y) ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ ¬lock(x',y) ∧ ¬demoness(x',y) ∧ ¬key(x',y)
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-2)

____


- act(kickblockup,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ block(x,y') ∧ ¬block(x,y") ∧ empty(x,y") ∧ ¬skeleton(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets:
    ¬block(x,y') ∧ block(x,y") ∧ time(t-1)

- act(kickblockdown,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ block(x,y') ∧ ¬block(x,y") ∧ empty(x,y") ∧ ¬skeleton(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets :
    ¬block(x,y') ∧ block(x,y") ∧ time(t-1)

- act(kickblockleft,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ block(x',y) ∧ ¬block(x",y) ∧ empty(x",y) ∧ ¬skeleton(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    ¬block(x',y) ∧ block(x",y) ∧ time(t-1)

- act(kickblockright,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ block(x',y) ∧ ¬block(x",y) ∧ empty(x",y) ∧ ¬skeleton(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    ¬block(x',y) ∧ block(x",y) ∧ time(t-1)

___

- act(kickskeletonup,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ empty(x,y") ∧ ¬squeleton(x,y") ∧ ¬block(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets:
    ¬skeleton(x,y') ∧ skeleton(x,y") ∧ time(t-1)

- act(kickskeletondown,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ empty(x,y") ∧ ¬squeleton(x,y") ∧ ¬block(x,y") ∧ ¬lock(x,y") ∧ ¬demoness(x,y")
  Effets :
    ¬skeleton(x,y') ∧ skeleton(x,y") ∧ time(t-1)

- act(kickskeletonleft,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ empty(x",y) ∧ ¬squeleton(x",y) ∧ ¬block(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    ¬skeleton(x',y) ∧ skeleton(x",y) ∧ time(t-1)

- act(kickskeletonright,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ empty(x",y) ∧ ¬squeleton(x",y) ∧ ¬block(x",y) ∧ ¬lock(x",y) ∧ ¬demoness(x",y)
  Effets :
    ¬skeleton(x',y) ∧ skeleton(x",y) ∧ time(t-1)

___

- act(kickskeleton_on_trap_up,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ empty(x,y") ∧ skeleton(x,y') ∧ trap(x,y") ∧ ¬block(x,y") ∧ ¬lock(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t-1)

- act(kickskeleton_on_trap_down,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ empty(x,y") ∧ skeleton(x,y') ∧ empty(x,y") ∧ ¬block(x,y') ∧ ¬lock(x,y')
  Effets :
    ¬skeleton(x,y') ∧ time(t-1)

- act(kickskeleton_on_trap_left,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ empty(x",y) ∧ skeleton(x',y) ∧ empty(x",y) ∧ ¬block(x',y) ∧ ¬lock(x',y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

- act(kickskeleton_on_trap_right,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ empty(x",y) ∧ skeleton(x',y) ∧ empty(x",y) ∧ ¬block(x',y) ∧ ¬lock(x',y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

____

- act(kickskeleton_on_wall_up,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ ¬empty(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t-1)

- act(kickskeleton_on_wall_down,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ ¬empty(x,y")
  Effets :
    ¬skeleton(x,y') ∧ time(t-1)

- act(kickskeleton_on_wall_left,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ ¬empty(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

- act(kickskeleton_on_wall_right,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ ¬empty(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

___

- act(kickskeletonup_on_block_up,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ block(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t-1)

- act(kickskeleton_on_block_down,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ block(x,y")
  Effets :
    ¬skeleton(x,y') ∧ time(t-1)

- act(kickskeleton_on_block_left,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ block(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

- act(kickskeleton_on_block_right,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ block(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

____

- act(kickskeleto_on_lock_up,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ lock(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t-1)

- act(kickskeleton_on_lock_down,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ lock(x,y")
  Effets :
    ¬skeleton(x,y') ∧ time(t-1)

- act(kickskeleton_on_lock_left,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ lock(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

- act(kickskeleton_on_lock_right,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ lock(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

___

- act(kickskeleton_on_skeleton_up,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ skeleton(x,y') ∧ skeleton(x,y")
  Effets:
    ¬skeleton(x,y') ∧ time(t-1)

- act(kickskeleton_on_skeleton_down,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ skeleton(x,y') ∧ skeleton(x,y")
  Effets :
    ¬skeleton(x,y') ∧ time(t-1)

- act(kickskeleton_on_skeleton_left,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ skeleton(x',y) ∧ skeleton(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

- act(kickskeleton_on_skeleton_right,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ skeleton(x',y) ∧ skeleton(x",y)
  Effets :
    ¬skeleton(x',y) ∧ time(t-1)

___

- act(getkeyup,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y') ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ ¬lock(x,y') ∧ key(x,y') ∧ ¬demoness(x,y')
  Effets:
    man(x,y') ∧ ¬man(x,y)) ∧ time(t-1) ∧ haskey(1)

- act(getkeydown,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ ¬lock(x,y') ∧ ¬demoness(x,y') ∧ key(x,y')
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-1) ∧ haskey(1)

- act(getkeyleft,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ ¬lock(x',y) ∧ ¬demoness(x',y) ∧ key(x',y)
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-1) ∧ haskey(1)

- act(getkeyright,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ ¬lock(x',y) ∧ ¬demoness(x',y) ∧ key(x',y)
  Effets :
    man(x,y')∧ ¬man(x,y)) ∧ time(t-1) ∧ haskey(1)

___

- act(openlockup,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y') ∧ haskey(1) ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ lock(x,y') ∧ ¬demoness(x,y')
  Effets:
    time(t-1) ∧ ¬lock(x,y')

- act(openlockdown,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ haskey(1) ∧ ¬block(x,y') ∧ empty(x,y') ∧ ¬skeleton(x,y') ∧ lock(x,y') ∧ ¬demoness(x,y')
  Effets :
    time(t-1) ∧ ¬lock(x,y')

- act(openlockleft,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ haskey(1) ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ lock(x',y) ∧ ¬demoness(x',y)
  Effets :
    time(t-1) ∧ ¬lock(x',y)

- act(openlockright,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x)  ∧ haskey(1) ∧ ¬block(x',y) ∧ empty(x',y) ∧ ¬skeleton(x',y) ∧ lock(x',y) ∧ ¬demoness(x',y)
  Effets :
    time(t-1) ∧ ¬lock(x',y)

___

- act(kickblock_on_block_up,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ block(x,y') ∧ block(x,y")
  Effets:
    time(t-1)

- act(kickblock_on_block_down,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ block(x,y') ∧ block(x,y")
  Effets :
    time(t-1)

- act(kickblock_on_block_left,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ block(x',y) ∧ block(x",y)
  Effets :
    time(t-1)

- act(kickblock_on_block_right,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ block(x',y) ∧ block(x",y)
  Effets :
    time(t-1)

___

- act(kickblock_on_lock_up,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ lock(x,y') ∧ block(x,y")
  Effets:
    time(t-1)

- act(kickblock_on_lock_down,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ lock(x,y') ∧ block(x,y")
  Effets :
    time(t-1)

- act(kickblock_on_lock_left,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ lock(x',y) ∧ block(x",y)
  Effets :
    time(t-1)

- act(kickblock_on_lock_right,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ lock(x',y) ∧ block(x",y)
  Effets :
    time(t-1)

___

- act(kickblock_on_wall_up,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ block(x,y') ∧ ¬empty(x,y")
  Effets:
    time(t-1)

- act(kickblock_on_wall_down,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ block(x,y') ∧ ¬empty(x,y")
  Effets :
    time(t-1)

- act(kickblock_on_wall_left,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ block(x',y) ∧ ¬empty(x",y)
  Effets :
    time(t-1)

- act(kickblock_on_wall_right,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ block(x',y) ∧ ¬empty(x",y)
  Effets :
    time(t-1)
___

- act(kickblock_on_skeleton_up,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y,y')  ∧ next(y',y") ∧ lock(x,y') ∧ skeleton(x,y")
  Effets:
    time(t-1)

- act(kickblock_on_skeleton_down,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(y',y) ∧ next(y",y') ∧ lock(x,y') ∧ skeleton(x,y")
  Effets :
    time(t-1)

- act(kickblock_on_skeleton_left,(x,y),(x',y'),time(t))<\br>
  Conditions:
    t>0 ∧ man(x,y) ∧ next(x,x') ∧ next(x',x") ∧ lock(x',y) ∧ skeleton(x",y)
  Effets :
    time(t-1)

- act(kickblock_on_skeleton_right,(x,y),(x',y'),time(t))<\br>

  Conditions:
    t>0 ∧ man(x,y) ∧ next(x',x) ∧ next(x",x') ∧ lock(x',y) ∧ skeleton(x",y)
  Effets :
    time(t-1)





##

Sokoban ne permet que de pousser les caisses et de deplacer le personnage. Ici :

- Pousser une "caisse" coute une action à part entière. Le bonhomme n'avance pas.
- On peut casser un certain type de caisse, les "skeletons", en les poussant contre des objets fixes.
- Certaines cases sont parfois piégées, parfois non. Cela se fait indépendamment de la décision du joueur!
- Un bloc peut être sur un piège
- Il y a une notion de clé, qui permet qu'un "mur" n'en soit plus un.

SURTOUT :
- Le but n'est pas de disposer les caisses à un endroit précis, mais bien de mettre le personnage sur une case adjacente à la sortie (ou mettre 3 ou 4 sorties).
