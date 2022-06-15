import sys
from helltaker_utils import grid_from_file, check_plan
import time
import clingo


def planify_asp(infos):
    basis = ""

    pb = """\
step(0..maxstep-1).

init(has_key(0)).
state_trap(on; off).
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
    spikes(X, Y - 1),
    not do(on_spike, T + 1).

:- do(left, T),
    fluent(at(X, Y), T),
    trap(X, Y - 1, on, T),
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
    spikes(X, Y - 1),
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
    spikes(X, Y + 1),
    not do(on_spike, T + 1).

:- do(right, T),
    fluent(at(X, Y), T),
    trap(X, Y + 1, on, T),
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
    spikes(X, Y + 1),
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
    spikes(X + 1, Y),
    not do(on_spike, T + 1).

:- do(up, T),
    fluent(at(X, Y), T),
    trap(X + 1, Y, on, T),
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
    spikes(X + 1, Y),
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
    spikes(X - 1, Y),
    not do(on_spike, T + 1).

:- do(down, T),
    fluent(at(X, Y), T),
    trap(X - 1, Y, on, T),
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
    spikes(X - 1, Y),
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
    spikes(X, Y),
    not do(on_spike, T + 1).

:-  do(push_left, T),
    fluent(at(X, Y), T),
    trap(X, Y, on, T),
    not do(on_spike, T + 1).

% effets
fluent(box(X, Y - 2), T + 1) :-
    do(push_left, T),
    fluent(at(X, Y), T),
    not demoness(X, Y - 2),
    not fluent(box(X, Y - 2), T),
    not fluent(chest(X, Y - 2), T),
    not fluent(monster(X, Y - 2), T).

fluent(box(X, Y - 1), T + 1) :-
    do(push_left, T),
    fluent(at(X, Y), T),
    demoness(X, Y - 2).

fluent(box(X, Y - 1), T + 1) :-
    do(push_left, T),
    fluent(at(X, Y), T),
    fluent(box(X, Y - 2), T).

fluent(box(X, Y - 1), T + 1) :-
    do(push_left, T),
    fluent(at(X, Y), T),
    fluent(chest(X, Y - 2), T).

fluent(box(X, Y - 1), T + 1) :-
    do(push_left, T),
    fluent(at(X, Y), T),
    fluent(monster(X, Y - 2), T).

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
    spikes(X, Y),
    not do(on_spike, T + 1).

:-  do(push_right, T),
    fluent(at(X, Y), T),
    trap(X, Y, on, T),
    not do(on_spike, T + 1).

% effets
fluent(box(X, Y + 2), T + 1) :-
    do(push_right, T),
    fluent(at(X, Y), T),
    not demoness(X, Y + 2),
    not fluent(box(X, Y + 2), T),
    not fluent(chest(X, Y + 2), T),
    not fluent(monster(X, Y + 2), T).

fluent(box(X, Y + 1), T + 1) :-
    do(push_right, T),
    fluent(at(X, Y), T),
    demoness(X, Y + 2).

fluent(box(X, Y + 1), T + 1) :-
    do(push_right, T),
    fluent(at(X, Y), T),
    fluent(box(X, Y + 2), T).

fluent(box(X, Y + 1), T + 1) :-
    do(push_right, T),
    fluent(at(X, Y), T),
    fluent(chest(X, Y + 2), T).

fluent(box(X, Y + 1), T + 1) :-
    do(push_right, T),
    fluent(at(X, Y), T),
    fluent(monster(X, Y + 2), T).

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
    spikes(X, Y),
    not do(on_spike, T + 1).

:-  do(push_up, T),
    fluent(at(X, Y), T),
    trap(X, Y, on, T),
    not do(on_spike, T + 1).

% effets
fluent(box(X + 2, Y), T + 1) :-
    do(push_up, T),
    fluent(at(X, Y), T),
    not demoness(X + 2, Y),
    not fluent(box(X + 2, Y), T),
    not fluent(chest(X + 2, Y), T),
    not fluent(monster(X + 2, Y), T).

fluent(box(X + 1, Y), T + 1) :-
    do(push_up, T),
    fluent(at(X, Y), T),
    demoness(X + 2, Y).

fluent(box(X + 1, Y), T + 1) :-
    do(push_up, T),
    fluent(at(X, Y), T),
    fluent(box(X + 2, Y), T).

fluent(box(X + 1, Y), T + 1) :-
    do(push_up, T),
    fluent(at(X, Y), T),
    fluent(chest(X + 2, Y), T).

fluent(box(X + 1, Y), T + 1) :-
    do(push_up, T),
    fluent(at(X, Y), T),
    fluent(monster(X + 2, Y), T).

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
    spikes(X, Y),
    not do(on_spike, T + 1).

:-  do(push_down, T),
    fluent(at(X, Y), T),
    trap(X, Y, on, T),
    not do(on_spike, T + 1).

% effets
fluent(box(X - 2, Y), T + 1) :-
    do(push_down, T),
    fluent(at(X, Y), T),
    not demoness(X - 2, Y),
    not fluent(box(X - 2, Y), T),
    not fluent(chest(X - 2, Y), T),
    not fluent(monster(X - 2, Y), T).

fluent(box(X - 1, Y), T + 1) :-
    do(push_down, T),
    fluent(at(X, Y), T),
    demoness(X - 2, Y).

fluent(box(X - 1, Y), T + 1) :-
    do(push_down, T),
    fluent(at(X, Y), T),
    fluent(box(X - 2, Y), T).

fluent(box(X - 1, Y), T + 1) :-
    do(push_down, T),
    fluent(at(X, Y), T),
    fluent(chest(X - 2, Y), T).

fluent(box(X - 1, Y), T + 1) :-
    do(push_down, T),
    fluent(at(X, Y), T),
    fluent(monster(X - 2, Y), T).

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

:- do(monster_left, T),
    fluent(at(X, Y), T),
    trap(X, Y, off, T),
    not do(on_spike, T + 1).

% effets
fluent(monster(X, Y - 2), T + 1) :-
    do(monster_left, T),
    cell(X, Y - 2),
    fluent(at(X, Y), T),
    not fluent(box(X, Y - 2), T),
    not fluent(chest(X, Y - 2), T).

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

:- do(monster_right, T),
    fluent(at(X, Y), T),
    trap(X, Y, off, T),
    not do(on_spike, T + 1).

% effets
fluent(monster(X, Y + 2), T + 1) :-
    do(monster_right, T),
    cell(X, Y + 2),
    fluent(at(X, Y), T),
    not fluent(box(X, Y + 2), T),
    not fluent(chest(X, Y + 2), T).

removed(monster(X, Y + 1), T) :-
    do(monster_right, T),
    fluent(at(X, Y), T).

removed(monster(X, Y + 1), T) :-
    fluent(box(X, Y + 2), T),
    do(monster_right, T),
    fluent(at(X, Y), T).

removed(monster(X, Y + 1), T) :-
    spikes(X, Y + 2),
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

:- do(monster_up, T),
    fluent(at(X, Y), T),
    trap(X, Y, off, T),
    not do(on_spike, T + 1).

% effets
fluent(monster(X + 2, Y), T + 1) :-
    do(monster_up, T),
    cell(X + 2, Y),
    fluent(at(X, Y), T),
    not fluent(box(X + 2, Y), T),
    not fluent(chest(X + 2, Y), T).

removed(monster(X + 1, Y), T) :-
    do(monster_up, T),
    fluent(at(X, Y), T).

removed(monster(X + 1, Y), T) :-
    fluent(box(X + 2, Y), T),
    do(monster_up, T),
    fluent(at(X, Y), T).

removed(monster(X + 1, Y), T) :-
    spikes(X + 2, Y),
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

:- do(monster_down, T),
    fluent(at(X, Y), T),
    trap(X, Y, off, T),
    not do(on_spike, T + 1).

% effets
fluent(monster(X - 2, Y), T + 1) :-
    do(monster_down, T),
    cell(X - 2, Y),
    fluent(at(X, Y), T),
    not fluent(box(X - 2, Y), T),
    not fluent(chest(X - 2, Y), T).

removed(monster(X - 1, Y), T) :-
    do(monster_down, T),
    fluent(at(X, Y), T).

removed(monster(X - 1, Y), T) :-
    fluent(box(X - 2, Y), T),
    do(monster_down, T),
    fluent(at(X, Y), T).

removed(monster(X - 1, Y), T) :-
    spikes(X - 2, Y),
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
    not spikes(X, Y),
    not trap(X, Y, off, T).

% effets
fluent(at(X, Y), T) :-
    do(on_spike, T + 1),
    spikes(X, Y),
    fluent(at(X, Y), T).

fluent(at(X, Y), T) :-
    do(on_spike, T + 1),
    trap(X, Y, on, T + 1),
    fluent(at(X, Y), T).

%%%%%% SWITCH TRAPS %%%%%%

:- trap(X, Y, S1, T), trap(X, Y, S2, T + 1), S1 = S2.

removed(monster(X, Y), T) :-
    trap(X, Y, on, T),
    fluent(monster(X, Y), T).

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

removed(key(X, Y), T) :-
    fluent(at(X, Y), T).

removed(has_key(0), T) :-
    fluent(has_key(1), T),
    fluent(at(X, Y), T),
    fluent(key(X, Y), T).

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
"""

    # parse the grid in the level_specificities string

    level_specificities = ""

    for m in range(1, infos["m"] - 1):
        i = infos["m"] - (m + 2)
        for n in range(1, infos["n"] - 1):
            j = n - 1
            if infos["grid"][m][n] != "#":
                level_specificities += f"cell({i},{j}).\n"
            if infos["grid"][m][n] == "H":
                level_specificities += f"init(at({i},{j})).\n"
            if infos["grid"][m][n] in ("B", "O", "P", "Q"):
                level_specificities += f"init(box({i},{j})).\n"
            if infos["grid"][m][n] == "D":
                level_specificities += f"demoness({i},{j}).\n"
                level_specificities += f"goal(at({i - 1},{j})).\n"
                level_specificities += f"goal(at({i},{j - 1})).\n"
                level_specificities += f"goal(at({i + 1},{j})).\n"
                level_specificities += f"goal(at({i},{j + 1})).\n"
            if infos["grid"][m][n] == "K":
                level_specificities += f"init(key({i},{j})).\n"
            if infos["grid"][m][n] == "M":
                level_specificities += f"init(monster({i},{j})).\n"
            if infos["grid"][m][n] == "L":
                level_specificities += f"init(chest({i},{j})).\n"
            if infos["grid"][m][n] in ("S", "O"):
                level_specificities += f"spikes({i},{j}).\n"
            if infos["grid"][m][n] in ("T", "P"):
                level_specificities += f"{{trap({i}, {j}, S, T) : state_trap(S)}} = 1 :- step(T). :- trap({i}, {j}, S, 0), S != on.\n"
            if infos["grid"][m][n] in ("U", "Q"):
                level_specificities += f"{{trap({i}, {j}, S, T) : state_trap(S)}} = 1 :- step(T). :- trap({i}, {j}, S, 0), S != off.\n"

    asp = level_specificities + pb

    ctl = clingo.Control([f"-c maxstep={infos['max_steps']}"], logger=log) # ajouter '-n0' pour afficher tt les modeles
    ctl.add("base", [], asp)

    ctl.ground([("base", [])])

    plan = [0] * infos["max_steps"]

    model_count = 0
    with ctl.solve(yield_=True) as handle:
        for model in handle:
            model_count += 1
            for atom in model.symbols(atoms=True):
                if atom.name == "do":
                    plan[atom.arguments[1].number] = atom.arguments[0].name

    #print(f"Model count: {model_count}")

    plan_str = ""
    for i in range(len(plan)):
        if "up" in plan[i]:
            plan_str += "h"
        if "down" in plan[i]:
            plan_str += "b"
        if "left" in plan[i]:
            plan_str += "g"
        if "right" in plan[i]:
            plan_str += "d"

    return plan_str


def log(code, message):
    """Cette fonction permet de récupérer les logs et de ne rien en faire afin de ne pas
    afficher des warnings inutiles dans la console lors du solving."""
    pass

def main():
    # récupération du nom du fichier depuis la ligne de commande
    filename = sys.argv[1]

    # récupération de al grille et de toutes les infos
    infos = grid_from_file(filename)

    # calcul du plan
    start = time.time()
    plan = planify_asp(infos)
    end = time.time()

    # affichage du résultat
    if check_plan(plan):
        # print(f"Temps d'exécution : {(end - start):.2f} secondes.")
        print("[OK]", plan)
        # print("")
    else:
        print("[Err]", plan, file=sys.stderr)
        sys.exit(2)


main()
