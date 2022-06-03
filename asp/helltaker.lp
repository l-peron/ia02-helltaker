%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%     HELLTAKING IN ASP      %%%
%%%        version: 0.1        %%%
%%%   authors : Adrien Simon   %%%
%%%             Julie Pichon   %%%
%%%             Léo Peron      %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%% CREATION DE L ENVIRONNEMENT %%%%%%%%
step(0..maxstep-1).

%... création des cellules walkables
cell(0, 0). cell(0, 1). cell(0, 2).
cell(1, 2). cell(1, 3). cell(2, 3).

%%%%%%%% INITIALISATION DES ACTIONS %%%%%%%%
action(
  right;
  left;
  top;
  bottom;
  push_brick_right;
  push_brick_left;
  push_brick_top;
  push_brick_bottom;
  push_monster_right;
  push_monster_left;
  push_monster_top;
  push_monster_bottom;
  nothing
).

%%%%%%%% INITIALISIATION DES FLUENTS %%%%%%%%
init(at(0, 0)). %position initiale du joueur

init(brick(0, 5)).

fluent(F, 0) :- init(F).

%%%%%%%% INITIALISATION DES BUTS %%%%%%%%
goal(at(2, 3)).
achieved(T) :- fluent(F, T), goal(F).

%%%%%%%% INITIALISATION DES BUTS %%%%%%%%
{ do(Act, T): action(Act) } = 1 :- step(T).

%%%%%%%% CREATION DES ACTIONS %%%%%%%%

% go left
:- do(left, T),
   fluent(at(X, Y), T),
   fluent(brick(X, Y - 1), T).
:- do(left, T),
   fluent(at(X, Y), T),
   not cell(X, Y - 1).
fluent(at(X, Y - 1), T + 1) :-
   do(left, T),
   fluent(at(X, Y), T).
removed(at(X, Y), T) :-
   do(left, T),
   fluent(at(X, Y), T).

% go right
:- do(right, T),
   fluent(at(X, Y), T),
   fluent(brick(X, Y + 1), T).
:- do(right, T),
   fluent(at(X, Y), T),
   not cell(X, Y + 1).
fluent(at(X, Y + 1), T + 1) :-
   do(right, T),
   fluent(at(X, Y), T).
removed(at(X, Y), T) :-
   do(right, T),
   fluent(at(X, Y), T).

% go top
:- do(top, T),
   fluent(at(X, Y), T),
   fluent(brick(X + 1, Y), T).
:- do(top, T),
   fluent(at(X, Y), T),
   not cell(X + 1, Y).
fluent(at(X + 1, Y), T + 1) :-
   do(top, T),
   fluent(at(X, Y), T).
removed(at(X, Y), T) :-
   do(top, T),
   fluent(at(X, Y), T).

% go top
:- do(bottom, T),
   fluent(at(X, Y), T),
   fluent(brick(X - 1, Y), T).
:- do(bottom, T),
   fluent(at(X, Y), T),
   not cell(X - 1, Y).
fluent(at(X - 1, Y), T + 1) :-
   do(bottom, T),
   fluent(at(X, Y), T).
removed(at(X, Y), T) :-
   do(bottom, T),
   fluent(at(X, Y), T).

%%%%%%%% FRAME PROBLEM %%%%%%%%
fluent(F, T + 1) :-
    fluent(F, T),
    T + 1 < horizon,
    not removed(F, T).

fluent(F, T + 1) :-
    fluent(F, T),
    achieved(T),
    T + 1 <= horizon.

%%%%%%%% AFFICHAGE %%%%%%%%
#show do/2.
