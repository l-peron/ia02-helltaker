%wall().
wall(here(3,1)).
%fixedtrap().
fixedtrap(here(3,1)).
%demon()
%door().
%key().
key(1,2).
%empty()
empty(1,2).
empty(2,2).
empty(1,1).
empty(2,1).
empty(0,0).
empty(0,1).
%empty(0,2).
%rock()
%mob()

%man()

%initial state :
init(state(at(2,2), blocks([here(1,2)]), opentraps([]), closedtraps([here(1,2)]), mobs([]), lock([here(2,1)]), haskey(1), 4)).
init2(state(at(1,2), blocks([]), opentraps([]), closedtraps([]), mobs([]), haskey(0), lock([]), haskey(0), 3)).

pop_elem([H|T], H, T).
pop_elem([H|T], X, [H|T2]) :-
  dif(H,X),
  pop_elem(T,X,T2).

not_member(_,[]).
not_member(X,[H|T]) :-
  dif(H,X),
  not_member(X,T).

member(X,[X|_]).
member(X,[H|T]) :-
  dif(H,X),
  member(X,T).
%positiion relative

next(up, here(X,Y), here(X2,Y)) :-
  X2 is X-1,
  empty(X,Y),
  empty(X2,Y).

next(down, here(X,Y), here(X2,Y)) :-
  X2 is X+1,
  empty(X,Y),
  empty(X2,Y).

next(left, here(X,Y), here(X,Y2)) :-
  Y2 is Y-1,
  empty(X,Y),
  empty(X,Y2).

next(right, here(X,Y), here(X,Y2)) :-
  Y2 is Y+1,
  empty(X,Y),
  empty(X,Y2).

%actions
%state(at(X,Y), blocks(B), opentraps(TO), closedtraps(TC), mobs(M), lock(L), key(K),haskey(X), TIMER),

do( action(moveonempty, To),
  state(at(X,Y), blocks(B), opentraps(TO), closedtraps(TC), mobs(M), lock(L), haskey(C), TIMER),
  state(at(X1,Y1), blocks(B), opentraps(TC), closedtraps(TO), mobs(M), lock(L), haskey(C), TIMER2))
  :-
    TIMER > 0,
    next(To, here(X,Y), here(X1,Y1)),
    not_member(here(X1,Y1), B),%no blocks
    not_member(here(X1,Y1), M),%no mobs
    not_member(here(X1,Y1), TC),%no closed trap
    not_member(here(X1,Y1), L),%no lock
    \+wall(here(X1,Y1)),%no wall
    \+fixedtrap(here(X1,Y1)),
    \+key(X1,Y1),
    TIMER2 is TIMER - 1.

%in case of fixed trap
do( action(moveontrapfix, To),
  state(at(X,Y), blocks(B), opentraps(TO), closedtraps(TC), mobs(M), lock(L), haskey(C), TIMER),
  state(at(X1,Y1), blocks(B), opentraps(TC), closedtraps(TO), mobs(M), lock(L), haskey(C), TIMER2))
  :-
    TIMER > 0,
    next(To, here(X,Y), here(X1,Y1)),
    not_member(here(X1,Y1), B),%no blocks
    not_member(here(X1,Y1), M),%no mobs
    not_member(here(X1,Y1), TC),%no closed trap
    not_member(here(X1,Y1), L),%no lock
    \+wall(here(X1,Y1)),%no wall
    \+key(X1,Y1),
    fixedtrap(here(X1,Y1)),
    TIMER2 is TIMER - 2.

%in case of a opening trap
do( action(moveontrapnotfix, To),
  state(at(X,Y), blocks(B), opentraps(TO), closedtraps(TC), mobs(M), lock(L),haskey(C), TIMER),
  state(at(X1,Y1), blocks(B), opentraps(TC), closedtraps(TO), mobs(M), lock(L),haskey(C), TIMER2))
  :-
    TIMER > 0,
    next(To, here(X,Y), here(X1,Y1)),
    not_member(here(X1,Y1), B),%no blocks
    not_member(here(X1,Y1), M),%no mobs
    member(here(X1,Y1), TC),% closed trap
    not_member(here(X1,Y1), TO),% closed trap
    not_member(here(X1,Y1), L),%no lock
    \+wall(here(X1,Y1)),%no wall
    \+fixedtrap(here(X1,Y1)),
    \+key(X1,Y1),
    TIMER2 is TIMER - 2.

do( action(moveonkey, To),
  state(at(X,Y), blocks(B), opentraps(TO), closedtraps(TC), mobs(M), lock(L), haskey(_), TIMER),
  state(at(X1,Y1), blocks(B), opentraps(TC), closedtraps(TO), mobs(M), lock(L), haskey(1), TIMER2))
  :-
    TIMER > 0,
    next(To, here(X,Y), here(X1,Y1)),
    not_member(here(X1,Y1), B),%no blocks
    not_member(here(X1,Y1), M),%no mobs
    not_member(here(X1,Y1), TC),% closed trap
    not_member(here(X1,Y1), L),%no lock
    key(X1,Y1),
    \+wall(here(X1,Y1)),%no wall
    \+fixedtrap(here(X1,Y1)),
    TIMER2 is TIMER - 1.


do( action(moveonclewithtrap, To),
  state(at(X,Y), blocks(B), opentraps(TO), closedtraps(TC), mobs(M), lock(L), haskey(_), TIMER),
  state(at(X1,Y1), blocks(B), opentraps(TC), closedtraps(TO), mobs(M), lock(L),haskey(1), TIMER2))
  :-
    TIMER > 0,
    next(To, here(X,Y), here(X1,Y1)),
    not_member(here(X1,Y1), B),%no blocks
    not_member(here(X1,Y1), M),%no mobs
    not_member(here(X1,Y1), L),%no lock
    key(X1,Y1),
    \+wall(here(X1,Y1)),%no wall
    (fixedtrap(here(X1,Y1));member(here(X1,Y1), TC)),
    TIMER2 is TIMER - 2.
%
do( action(opendoor, To),
  state(at(X,Y), blocks(B), opentraps(TO), closedtraps(TC), mobs(M), lock(L), haskey(1), TIMER),
  state(at(X1,Y1), blocks(B), opentraps(TC), closedtraps(TO), mobs(M), lock(L), haskey(0), TIMER2))
  :-
    TIMER > 0,
    next(To, here(X,Y), here(X1,Y1)),
    not_member(here(X1,Y1), B),%no blocks
    not_member(here(X1,Y1), M),%no mobs
    member(here(X1,Y1), L),%lock
    \+wall(here(X1,Y1)),%no wall
    TIMER2 is TIMER - 1.

do( action(kickblock, To),
  state(at(X,Y), blocks(B), opentraps(TO), closedtraps(TC), mobs(M), lock(L), haskey(C), TIMER),
  state(at(X,Y), blocks([here(X2,Y2)|B2]), opentraps(TC), closedtraps(TO), mobs(M), lock(L), haskey(C), TIMER2))
  :-
    TIMER > 0,
    next(To, here(X,Y), here(X1,Y1)),
    next(To, here(X1,Y1), here(X2,Y2)),
    not_member(here(X2,Y2), L),%lock
    not_member(here(X2,Y2), B),%no blocks
    not_member(here(X2,Y2), M),%no mobs
    member(here(X1,Y1),B),
    pop_elem(B,here(X1,Y1),B2),
    \+wall(here(X2,Y2)),%no wall
    TIMER2 is TIMER - 1.

do( action(kickonobstacle, To),
  state(at(X,Y), blocks(B), opentraps(TO), closedtraps(TC), mobs(M), lock(L), haskey(C), TIMER),
  state(at(X,Y), blocks(B), opentraps(TC), closedtraps(TO), mobs(M), lock(L), haskey(C), TIMER2))
  :-
    TIMER > 0,
    next(To, here(X,Y), here(X1,Y1)),
    next(To, here(X1,Y1), here(X2,Y2)),
    (member(here(X2,Y2), L); member(here(X2,Y2), B); member(here(X2,Y2), M)),
    (member(here(X1,Y1),B); member(here(X1,Y1),M)),%no wall
    TIMER2 is TIMER - 1.

do( action(kickonobstacle, To),
  state(at(X,Y), blocks(B), opentraps(TO), closedtraps(TC), mobs(M), lock(L), haskey(C), TIMER),
  state(at(X,Y), blocks(B), opentraps(TC), closedtraps(TO), mobs(M), lock(L), haskey(C), TIMER2))
  :-
    TIMER > 0,
    next(To, here(X,Y), here(X1,Y1)),
    \+next(To, here(X1,Y1), here(_,_)),
    (member(here(X1,Y1),B); member(here(X1,Y1),M)),
    TIMER2 is TIMER - 1.

do( action(kickmob, To),
  state(at(X,Y), blocks(B), opentraps(TO), closedtraps(TC), mobs(M), lock(L), haskey(C), TIMER),
  state(at(X,Y), blocks(B), opentraps(TC), closedtraps(TO), mobs([here(X2,Y2)|M2]), lock(L), haskey(C), TIMER2))
  :-
    TIMER > 0,
    next(To, here(X,Y), here(X1,Y1)),
    next(To, here(X1,Y1), here(X2,Y2)),
    not_member(here(X2,Y2), L),%lock
    not_member(here(X2,Y2), B),%no blocks
    not_member(here(X2,Y2), M),%no mobs
    member(here(X1,Y1),M),
    pop_elem(M,here(X1,Y1),M2),
    \+wall(here(X2,Y2)),%no wall
    TIMER2 is TIMER - 1.

do( action(destroymob, To),
  state(at(X,Y), blocks(B), opentraps(TO), closedtraps(TC), mobs(M), lock(L), haskey(C), TIMER),
  state(at(X,Y), blocks(B), opentraps(TC), closedtraps(TO), mobs([here(X2,Y2)|M2]), lock(L), haskey(C), TIMER2))
  :-
    TIMER > 0,
    next(To, here(X,Y), here(X1,Y1)),
    next(To, here(X1,Y1), here(X2,Y2)),
    not_member(here(X2,Y2), L),%lock
    not_member(here(X2,Y2), B),%no blocks
    not_member(here(X2,Y2), M),%no mobs
    member(here(X1,Y1),M),
    pop_elem(M,here(X1,Y1),M2),
    \+wall(here(X2,Y2)),%no wall
    TIMER2 is TIMER - 1.
