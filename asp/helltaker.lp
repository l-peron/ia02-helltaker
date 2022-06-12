%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%      HELLTAKER IN ASP      %%%
%%%        version: 0.1        %%%
%%%    authors : Adrien Simon  %%%
%%%              Julie Pichon  %%%
%%%              Léo Peron     %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%% clingo -c maxstep=n -n0 helltaker.lp

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% INITIALISATION %%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

step(0..maxstep-1).

cell(0, 5).
cell(1, 0..5).
cell(2, 0). cell(2, 2..5).
cell(3, 0). cell(3, 2..5).
cell(4, 0). cell(4, 2..5).
cell(5, 2..5).
cell(6, 3..4).

%%%%%% INIT %%%%%%
% player
init(at(4, 0)).

% boxes
init(box(5, 4)).
init(box(4, 4)).
init(box(2, 2)).
init(box(2, 3)).
init(box(2, 4)).
init(box(2, 5)).

% monsters
init(monster(2, 0)).

% spikes
spikes(1, 0).
spikes(4, 2).
spikes(3, 3).
spikes(3, 5).
spikes(1, 2).
spikes(1, 5).

% trap
traps(on; off).
init(trap(1, 0, off)).
init(trap(4, 2, off)).
init(trap(3, 3, off)).
init(trap(3, 5, off)).
init(trap(1, 2, off)).
init(trap(1, 5, off)).

% demoness
demoness(6, 4).

% chest & key
init(chest(5, 3)).
init(key(0, 5)).

init(has_key(0)).

fluent(F, 0) :- init(F).

%%%%%% ACTIONS %%%%%%
action(
  right;
  left;
  up;
  down;
  push_right;
  push_left;
  push_down;
  push_up;
  monster_right;
  monster_left;
  monster_down;
  monster_up;
  on_spike;
  nop).

%%%%%%%%%%%%%%%%%%%%
%%%%%%% BUTS %%%%%%%
%%%%%%%%%%%%%%%%%%%%

goal(at(6, 3)).
goal(at(5, 4)).

achieved(T) :- fluent(F, T), goal(F).

:- not achieved(_).
:- achieved(T), T > maxstep.
:- achieved(T), do(Act, T), Act != nop.
:- do(nop, T), not achieved(T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%% ACTIONS DEPLACEMENT %%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

{do(Act, T): action(Act)} = 1 :- step(T).

%%%%%% ACTION LEFT %%%%%%
% préconditions
:-  do(left, T),
    fluent(at(X, Y), T),
    not cell(X, Y - 1).

:-  do(left, T),
    fluent(at(X, Y), T),
    fluent(box(X, Y - 1), T).

:-  do(left, T),
    fluent(at(X, Y), T),
    fluent(monster(X, Y - 1), T).

:- do(left, T),
    fluent(at(X, Y), T),
    spikes(X, Y - 1), T),
    not do(on_spike, T + 1).

% effets
fluent(at(X, Y - 1), T + 1) :-
    do(left, T),
    fluent(at(X, Y), T),
    cell(X, Y - 1),
    not fluent(box(X, Y - 1), T),
    not fluent(monster(X, Y - 1), T),
    not fluent(chest(X, Y - 1), T).

fluent(at(X, Y - 1), T + 1) :-
    do(left, T),
    fluent(at(X, Y), T),
    cell(X, Y - 1),
    spikes(X, Y - 1), T),
    not fluent(box(X, Y - 1), T),
    not fluent(monster(X, Y - 1), T),
    not fluent(chest(X, Y - 1), T).

fluent(at(X, Y), T + 1) :-
    do(left, T),
    fluent(at(X, Y), T),
    cell(X, Y - 1),
    fluent(chest(X, Y - 1), T),
    fluent(has_key(0), T).

fluent(at(X, Y - 1), T + 1) :-
    do(left, T),
    fluent(at(X, Y), T),
    cell(X, Y - 1),
    fluent(chest(X, Y - 1), T),
    fluent(has_key(1), T).

removed(chest(X, Y - 1), T + 1) :-
    do(right, T),
    fluent(at(X, Y), T),
    fluent(has_key(1), T).

removed(at(X, Y), T) :-
    do(left, T),
    fluent(at(X, Y), T).

%%%%%% ACTION RIGHT %%%%%%
% préconditions
:-  do(right, T),
    fluent(at(X, Y), T),
    not cell(X, Y + 1).

:-  do(right, T),
    fluent(at(X, Y), T),
    fluent(box(X, Y + 1), T).

:-  do(right, T),
    fluent(at(X, Y), T),
    fluent(monster(X, Y + 1), T).

:- do(right, T),
    fluent(at(X, Y), T),
    spikes(X, Y + 1), T),
    not do(on_spike, T + 1).

% effets
fluent(at(X, Y + 1), T + 1) :-
    do(right, T),
    fluent(at(X, Y), T),
    cell(X, Y + 1),
    not fluent(box(X, Y + 1), T),
    not fluent(monster(X, Y + 1), T),
    not fluent(chest(X, Y + 1), T).

fluent(at(X, Y + 1), T + 1) :-
    do(right, T),
    fluent(at(X, Y), T),
    cell(X, Y + 1),
    spikes(X, Y + 1), T),
    not fluent(box(X, Y + 1), T),
    not fluent(monster(X, Y + 1), T),
    not fluent(chest(X, Y + 1), T).

fluent(at(X, Y), T + 1) :-
    do(right, T),
    fluent(at(X, Y), T),
    cell(X, Y + 1),
    fluent(chest(X, Y + 1), T),
    fluent(has_key(0), T).

fluent(at(X, Y + 1), T + 1) :-
    do(right, T),
    fluent(at(X, Y), T),
    cell(X, Y + 1),
    fluent(chest(X, Y + 1), T),
    fluent(has_key(1), T).

removed(chest(X, Y + 1), T + 1) :-
    do(right, T),
    fluent(at(X, Y), T),
    fluent(has_key(1), T).

removed(at(X, Y), T) :-
    do(right, T),
    fluent(at(X, Y), T).

%%%%%% ACTION UP %%%%%%
% préconditions
:-  do(up, T),
    fluent(at(X, Y), T),
    not cell(X + 1, Y).

:-  do(up, T),
    fluent(at(X, Y), T),
    fluent(box(X + 1, Y), T).

:-  do(up, T),
    fluent(at(X, Y), T),
    fluent(monster(X + 1, Y), T).

:- do(up, T),
    fluent(at(X, Y), T),
    spikes(X + 1, Y), T),
    not do(on_spike, T + 1).

% effets
fluent(at(X + 1, Y), T + 1) :-
    do(up, T),
    fluent(at(X, Y), T),
    cell(X + 1, Y),
    not fluent(box(X + 1, Y), T),
    not fluent(monster(X + 1, Y), T),
    not fluent(chest(X + 1, Y), T).

fluent(at(X + 1, Y), T + 1) :-
    do(up, T),
    fluent(at(X, Y), T),
    cell(X + 1, Y),
    spikes(X + 1, Y), T),
    not fluent(box(X + 1, Y), T),
    not fluent(monster(X + 1, Y), T),
    not fluent(chest(X + 1, Y), T).

fluent(at(X, Y), T + 1) :-
    do(up, T),
    fluent(at(X, Y), T),
    cell(X + 1, Y),
    fluent(chest(X + 1, Y), T),
    fluent(has_key(0), T).

fluent(at(X + 1, Y), T + 1) :-
    do(up, T),
    fluent(at(X, Y), T),
    cell(X + 1, Y),
    fluent(chest(X + 1, Y), T),
    fluent(has_key(1), T).

removed(chest(X + 1, Y), T + 1) :-
    do(up, T),
    fluent(at(X, Y), T),
    fluent(has_key(1), T).

removed(at(X, Y), T) :-
    do(up, T),
    fluent(at(X, Y), T).


%%%%%% ACTION DOWN %%%%%%
% préconditions
:-  do(down, T),
    fluent(at(X, Y), T),
    not cell(X - 1, Y).

:-  do(down, T),
    fluent(at(X, Y), T),
    fluent(box(X - 1, Y), T).

:-  do(down, T),
    fluent(at(X, Y), T),
    fluent(monster(X - 1, Y), T).

:- do(down, T),
    fluent(at(X, Y), T),
    spikes(X - 1, Y), T),
    not do(on_spike, T + 1).

% effets
fluent(at(X - 1, Y), T + 1) :-
    do(down, T),
    fluent(at(X, Y), T),
    cell(X - 1, Y),
    not fluent(box(X - 1, Y), T),
    not fluent(monster(X - 1, Y), T),
    not fluent(chest(X - 1, Y), T).

fluent(at(X - 1, Y), T + 1) :-
    do(down, T),
    fluent(at(X, Y), T),
    cell(X - 1, Y),
    spikes(X - 1, Y), T),
    not fluent(box(X - 1, Y), T),
    not fluent(monster(X - 1, Y), T),
    not fluent(chest(X - 1, Y), T).

fluent(at(X, Y), T + 1) :-
    do(down, T),
    fluent(at(X, Y), T),
    cell(X - 1, Y),
    fluent(chest(X - 1, Y), T),
    fluent(has_key(0), T).

fluent(at(X - 1, Y), T + 1) :-
    do(down, T),
    fluent(at(X, Y), T),
    cell(X - 1, Y),
    fluent(chest(X - 1, Y), T),
    fluent(has_key(1), T).

removed(chest(X - 1, Y), T + 1) :-
    do(down, T),
    fluent(at(X, Y), T),
    fluent(has_key(1), T).

removed(at(X, Y), T) :-
    do(down, T),
    fluent(at(X, Y), T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%% ACTIONS PUSH BOXES %%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%% ACTION PUSH LEFT %%%%%%
% préconditions
:-  do(push_left, T),
    fluent(at(X, Y), T),
    not fluent(box(X, Y - 1), T).

:-  do(push_left, T),
    fluent(at(X, Y), T),
    not cell(X, Y - 2).

:-  do(push_left, T),
    fluent(at(X, Y), T),
    demoness(X, Y - 2).

:-  do(push_left, T),
    fluent(at(X, Y), T),
    fluent(chest(X, Y - 2), T).

:-  do(push_left, T),
    fluent(at(X, Y), T),
    fluent(box(X, Y - 2), T).

:-  do(push_left, T),
    fluent(at(X, Y), T),
    fluent(monster(X, Y - 2), T).

:-  do(push_left, T),
    fluent(at(X, Y), T),
    spikes(X, Y),
    not do(on_spike, T + 1).

% effets
fluent(box(X, Y - 2), T + 1) :-
    do(push_left, T),
    fluent(at(X, Y), T).

removed(box(X, Y - 1), T) :-
    do(push_left, T),
    fluent(at(X, Y), T).

%%%%%% ACTION PUSH RIGHT %%%%%%
% préconditions
:-  do(push_right, T),
    fluent(at(X, Y), T),
    not fluent(box(X, Y + 1), T).

:-  do(push_right, T),
    fluent(at(X, Y), T),
    not cell(X, Y + 2).

:-  do(push_right, T),
    fluent(at(X, Y), T),
    demoness(X, Y + 2).

:-  do(push_right, T),
    fluent(at(X, Y), T),
    fluent(chest(X, Y + 2), T).

:-  do(push_right, T),
    fluent(at(X, Y), T),
    fluent(box(X, Y + 2), T).

:-  do(push_right, T),
    fluent(at(X, Y), T),
    fluent(monster(X, Y + 2), T).

:-  do(push_right, T),
    fluent(at(X, Y), T),
    spikes(X, Y),
    not do(on_spike, T + 1).

% effets
fluent(box(X, Y + 2), T + 1) :-
    do(push_right, T),
    fluent(at(X, Y), T).

removed(box(X, Y + 1), T) :-
    do(push_right, T),
    fluent(at(X, Y), T).

%%%%%% ACTION PUSH UP %%%%%%
% préconditions
:-  do(push_up, T),
    fluent(at(X, Y), T),
    not fluent(box(X + 1, Y), T).

:-  do(push_up, T),
    fluent(at(X, Y), T),
    not cell(X + 2, Y).

:-  do(push_up, T),
    fluent(at(X, Y), T),
    demoness(X + 2, Y).

:-  do(push_up, T),
    fluent(at(X, Y), T),
    fluent(chest(X + 2, Y), T).

:-  do(push_up, T),
    fluent(at(X, Y), T),
    fluent(box(X + 2, Y), T).

:-  do(push_up, T),
    fluent(at(X, Y), T),
    fluent(monster(X + 2, Y), T).

:-  do(push_up, T),
    fluent(at(X, Y), T),
    spikes(X, Y),
    not do(on_spike, T + 1).

% effets
fluent(box(X + 2, Y), T + 1) :-
    do(push_up, T),
    fluent(at(X, Y), T).

removed(box(X + 1, Y), T) :-
    do(push_up, T),
    fluent(at(X, Y), T).

%%%%%% ACTION PUSH DOWN %%%%%%
% préconditions
:-  do(push_down, T),
    fluent(at(X, Y), T),
    not fluent(box(X - 1, Y), T).

:-  do(push_down, T),
    fluent(at(X, Y), T),
    not cell(X - 2, Y).

:-  do(push_down, T),
    fluent(at(X, Y), T),
    demoness(X - 2, Y).

:-  do(push_down, T),
    fluent(at(X, Y), T),
    fluent(chest(X - 2, Y), T).

:-  do(push_down, T),
    fluent(at(X, Y), T),
    fluent(box(X - 2, Y), T).

:-  do(push_down, T),
    fluent(at(X, Y), T),
    fluent(monster(X - 2, Y), T).

:-  do(push_down, T),
    fluent(at(X, Y), T),
    spikes(X, Y),
    not do(on_spike, T + 1).

% effets
fluent(box(X - 2, Y), T + 1) :-
    do(push_down, T),
    fluent(at(X, Y), T).

removed(box(X - 1, Y), T) :-
    do(push_down, T),
    fluent(at(X, Y), T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%% ACTIONS PUSH MONSTERS %%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%% ACTION MONSTER LEFT %%%%%%
% préconditions
:-  do(monster_left, T),
    fluent(at(X, Y), T),
    not fluent(monster(X, Y - 1), T).

:-  do(monster_left, T),
    fluent(at(X, Y), T),
    fluent(monster(X, Y - 2), T).

:- do(monster_left, T),
    fluent(at(X, Y), T),
    spikes(X, Y),
    not do(on_spike, T + 1).

% effets
fluent(monster(X, Y - 2), T + 1) :-
    do(monster_left, T),
    cell(X, Y - 2),
    fluent(at(X, Y), T).

removed(monster(X, Y - 1), T) :-
    do(monster_left, T),
    fluent(at(X, Y), T).

removed(monster(X, Y - 1), T) :-
    fluent(box(X, Y - 2), T),
    do(monster_left, T),
    fluent(at(X, Y), T).

removed(monster(X, Y - 1), T) :-
    spikes(X, Y - 2),
    do(monster_left, T),
    fluent(at(X, Y), T).

removed(monster(X, Y - 1), T) :-
    not cell(X, Y - 2),
    do(monster_left, T),
    fluent(at(X, Y), T).

%%%%%% ACTION MONSTER RIGHT %%%%%%
% préconditions
:-  do(monster_right, T),
    fluent(at(X, Y), T),
    not fluent(monster(X, Y + 1), T).

:-  do(monster_right, T),
    fluent(at(X, Y), T),
    fluent(monster(X, Y + 2), T).

:- do(monster_right, T),
    fluent(at(X, Y), T),
    spikes(X, Y),
    not do(on_spike, T + 1).

% effets
fluent(monster(X, Y + 2), T + 1) :-
    do(monster_right, T),
    cell(X, Y + 2),
    fluent(at(X, Y), T).

removed(monster(X, Y + 1), T) :-
    do(monster_right, T),
    fluent(at(X, Y), T).

removed(monster(X, Y + 1), T) :-
    fluent(box(X, Y + 2), T),
    do(monster_right, T),
    fluent(at(X, Y), T).

removed(monster(X, Y + 1), T) :-
    spikes(X, Y + 2), T),
    do(monster_right, T),
    fluent(at(X, Y), T).

removed(monster(X, Y + 1), T) :-
    not cell(X, Y + 2),
    do(monster_right, T),
    fluent(at(X, Y), T).

%%%%%% ACTION MONSTER UP %%%%%%
% préconditions
:-  do(monster_up, T),
    fluent(at(X, Y), T),
    not fluent(monster(X + 1, Y), T).

:-  do(monster_up, T),
    fluent(at(X, Y), T),
    fluent(monster(X + 2, Y), T).

:- do(monster_up, T),
    fluent(at(X, Y), T),
    spikes(X, Y),
    not do(on_spike, T + 1).

% effets
fluent(monster(X + 2, Y), T + 1) :-
    do(monster_up, T),
    cell(X + 2, Y),
    fluent(at(X, Y), T).

removed(monster(X + 1, Y), T) :-
    do(monster_up, T),
    fluent(at(X, Y), T).

removed(monster(X + 1, Y), T) :-
    fluent(box(X + 2, Y), T),
    do(monster_up, T),
    fluent(at(X, Y), T).

removed(monster(X + 1, Y), T) :-
    spikes(X + 2, Y), T),
    do(monster_up, T),
    fluent(at(X, Y), T).

removed(monster(X + 1, Y), T) :-
    not cell(X + 2, Y),
    do(monster_up, T),
    fluent(at(X, Y), T).

%%%%%% ACTION MONSTER DOWN %%%%%%
% préconditions
:-  do(monster_down, T),
    fluent(at(X, Y), T),
    not fluent(monster(X - 1, Y), T).

:-  do(monster_down, T),
    fluent(at(X, Y), T),
    fluent(monster(X - 2, Y), T).

:- do(monster_down, T),
    fluent(at(X, Y), T),
    spikes(X, Y),
    not do(on_spike, T + 1).

% effets
fluent(monster(X - 2, Y), T + 1) :-
    do(monster_down, T),
    cell(X - 2, Y),
    fluent(at(X, Y), T).

removed(monster(X - 1, Y), T) :-
    do(monster_down, T),
    fluent(at(X, Y), T).

removed(monster(X - 1, Y), T) :-
    fluent(box(X - 2, Y), T),
    do(monster_down, T),
    fluent(at(X, Y), T).

removed(monster(X - 1, Y), T) :-
    spikes(X - 2, Y), T),
    do(monster_down, T),
    fluent(at(X, Y), T).

removed(monster(X - 1, Y), T) :-
    not cell(X - 2, Y),
    do(monster_down, T),
    fluent(at(X, Y), T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%% SPIKE SPECIFICS %%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%% ON SPIKE %%%%%%
% préconditions
:-  do(on_spike, T),
    fluent(at(X, Y), T),
    not spikes(X, Y).

% effets
fluent(at(X, Y), T) :-
    do(on_spike, T),
    spikes(X, Y),
    fluent(at(X, Y), T).

%%%%%% SWITCH TRAPS %%%%%%

fluent(trap(X, Y, on), T + 1) :-
    fluent(trap(X, Y, off), T).

fluent(trap(X, Y, off), T + 1) :-
    fluent(trap(X, Y, on), T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%% KEY AND CHEST %%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%

fluent(has_key(1), T) :-
    do(right, T),
    fluent(at(X, Y), T),
    fluent(key(X, Y + 1), T).

fluent(has_key(1), T) :-
    do(left, T),
    fluent(at(X, Y), T),
    fluent(key(X, Y - 1), T).

fluent(has_key(1), T) :-
    do(down, T),
    fluent(at(X, Y), T),
    fluent(key(X - 1, Y), T).

fluent(has_key(1), T) :-
    do(up, T),
    fluent(at(X, Y), T),
    fluent(key(X + 1, Y), T).

removed(has_key(0), T) :-
    fluent(has_key(1), T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%% FRAME PROBLEM %%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%

fluent(F, T + 1) :-
    fluent(F, T),
    T + 1 < maxstep,
    not removed(F, T).

fluent(F, T + 1) :-
    fluent(F, T),
    achieved(T),
    T + 1 <= maxstep.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#show do/2.
