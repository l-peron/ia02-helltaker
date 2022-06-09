%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%      HELLTAKER IN ASP      %%%
%%%        version: 0.1        %%%
%%%    authors : Adrien Simon  %%%
%%%              Julie Pichon  %%%
%%%              Léo Peron     %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%% clingo -c maxstep=10 -n0 helltaker.lp

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%% INITIALISATION %%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#const n = 6.
#const m = 6.
step(0..maxstep-1).

cell(0..m-1, 0..n-1).

%%%%%% ACTIONS %%%%%%
action(
  right;
  left;
  up;
  down;
  push_right;
  nop).

%%%%%% INIT %%%%%%
% player
init(at(0, 1)).

% boxes
init(box(2, 2)).
init(box(1, 3)).

fluent(F, 0) :- init(F).

%%%%%%%%%%%%%%%%%%%%
%%%%%%% BUTS %%%%%%%
%%%%%%%%%%%%%%%%%%%%

goal(at(2, 3)).

achieved(T) :- fluent(F, T), goal(F).

:- not achieved(_).
:- achieved(T), T > maxstep.
:- achieved(T), do(Act, T), Act != nop.
:- do(nop, T), not achieved(T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%
%%%%%% ACTIONS %%%%%%
%%%%%%%%%%%%%%%%%%%%%

{ do(Act, T): action(Act) } = 1 :- step(T).

%%%%%% ACTION LEFT %%%%%%
% préconditions
:-  do(left, T),
    fluent(at(X, Y), T),
    not cell(X, Y - 1).

:-  do(left, T),
    fluent(at(X, Y), T),
    fluent(box(X, Y - 1), T).

% effets
fluent(at(X, Y - 1), T + 1) :-
    do(left, T),
    fluent(at(X, Y), T),
    cell(X, Y - 1),
    not fluent(box(X, Y - 1), T).

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

% effets
fluent(at(X, Y + 1), T + 1) :-
    do(right, T),
    fluent(at(X, Y), T),
    cell(X, Y + 1),
    not fluent(box(X, Y + 1), T).

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

% effets
fluent(at(X + 1, Y), T + 1) :-
    do(up, T),
    fluent(at(X, Y), T),
    cell(X + 1, Y),
    not fluent(box(X + 1, Y), T).

removed(at(X, Y), T) :-
    do(up, T),
    fluent(at(X, Y), T).


%%%%%% ACTION DOWN %%%%%%
% préconditions
:-  do(down, T),
    fluent(at(X, Y), T),
    not cell(X - 1, Y).

:-  do(up, T),
    fluent(at(X, Y), T),
    fluent(box(X - 1, Y), T).

% effets
fluent(at(X - 1, Y), T + 1) :-
    do(down, T),
    fluent(at(X, Y), T),
    cell(X - 1, Y),
    not fluent(box(X - 1, Y), T).

removed(at(X, Y), T) :-
    do(down, T),
    fluent(at(X, Y), T).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%% FRAME PROBLEM %%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%

fluent(F, T + 1) :-
    fluent(F, T),
    T + 1 < maxstep,
    not removed(F, T).

fluent(F, T + 1) :-
    fluent(F, T),
    achieved(T),
    T + 1 <= maxstep.

#show do/2.
