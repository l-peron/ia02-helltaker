import sys
from helltaker_utils import grid_from_file, check_plan
from collections import namedtuple
from typing import Dict, List, Tuple, Callable, Set

Action = namedtuple("action", ("verb", "direction"))

actionNames = ["move", "push"]
# "unlock", "pushBlock", "pushMob", "killMob"

actions = {d: [] for d in "hbgd"}

for d in "hbgd":
    for a in actionNames:
        actions[d].append(Action(a, d))

State = namedtuple(
    "state",
    ("hero", "steps", "blocks", "key", "lock", "mobs", "safeTraps", "unsafeTraps"),
)

# ALL UTILS

# FROZEN SET (for immuable)
def add_in_frozenset(fset : frozenset, elt : Tuple[int, int]) -> frozenset:
    s = {x for x in fset}
    s.add(elt)
    return frozenset(s)

def remove_in_frozenset(fset : frozenset,elt : Tuple[int, int]) -> frozenset:
    s = {x for x in fset}
    s.remove(elt)
    return frozenset(s)

# DICT 2 PATH (print)
def dict2path(s: State, d: Dict[State, Tuple[State, Action]]) -> List[str]:
    l = [(s, None)]
    while not d[s] is None:
        parent, a = d[s]
        l.append((parent, a.direction))
        s = parent
    l.reverse()
    return l


# PILE / FILES UTILS

def insert_tail(s, l):
    l.append(s)
    return l

def remove_head(l):
    return l.pop(0), l

def remove_tail(l):
    return l.pop(), l

# PARSING ELEMENTS TO FLUENTS AND NON FLUENTS
def parsingInfos(grid: List[List[str]], maxstep: int) -> Tuple[Dict[str, set], State]:
    hero = None
    blocks = set()
    key = None
    lock = None
    mobs = set()
    safeTraps = set()
    unsafeTraps = set()

    map_rules = { 'D': set(), 'S': set(), '#': set()}

    for x, subgrid in enumerate(grid):
        for y, c in enumerate(subgrid):
            if c in "DS#O":
                if c == "O":
                    c = "S"
                map_rules[c].add((x, y))
            elif c == "H":
                hero = (x, y)
            elif c in ["B", "P", "Q"]:
                blocks.add((x, y))
            elif c in ["K"]:
                key = (x, y)
            elif c in ["L"]:
                lock = (x, y)
            elif c in ["M"]:
                mobs.add((x, y))
            elif c in ["T", "P"]:
                safeTraps.add((x, y))
            elif c in ["U", "Q"]:
                unsafeTraps.add((x, y))

    state = State(hero, maxstep, frozenset(blocks), key, lock, frozenset(mobs), frozenset(safeTraps), frozenset(unsafeTraps))

    return map_rules, state


# MOVING ONE STEP
def one_step(position: Tuple[int, int], direction: str) -> Tuple[int, int]:
    x, y = position
    return {"d": (x, y + 1), "g": (x, y - 1), "h": (x - 1, y), "b": (x + 1, y)}[
        direction
    ]


# COPY AND MODIFY STATE
def modify_state_factory(state: State) -> Callable:
    def mod(
        hero=state.hero,
        steps=state.steps,
        blocks=state.blocks,
        key=state.key,
        lock=state.lock,
        mobs=state.mobs,
        safeTraps=state.safeTraps,
        unsafeTraps=state.unsafeTraps,
    ):
        return State(hero, steps, blocks, key, lock, mobs, safeTraps, unsafeTraps)
    return mod

def moving_frozenset(fset: frozenset, supr: Tuple[int, int], new: Tuple[int, int]):
    raw = {x for x in fset}
    raw.remove(supr)
    raw.add(new)
    return frozenset(raw)

# CHECK IF FREE
def free_factory(map_rules):
    def free(position):
        return not ((position in map_rules["#"]) or (position in map_rules["D"]))

    return free


def updating_state(map_rules: Dict[str, List[int]], state: State, newHero: List[int], mobs:List[Tuple[int,int]]=[], blocks:List[Tuple[int,int]]=[]):

    # KILLINGS MOBS
    newMobs = []
    if mobs :
        newMobs=list(mobs)
    else:
        newMobs = list(state.mobs)
    for mob in newMobs:
        if (mob in state.safeTraps) or (mob in map_rules["S"]):
            newMobs.remove(mob)

    # MOVING BLOCKS IF NECESSARY
    newBlocks = []
    if blocks:
        print(blocks)
        newBlocks = list(blocks)
    else:
        newBlocks = state.blocks

    # DEFINE COST
    cost = 0
    if (newHero in state.safeTraps) or (newHero in map_rules["S"]):
        cost = 2
    else:
        cost = 1

    # GAME OVER
    if state.steps - cost < 0:
        return None

    # SWITCHING TRAPS, UPDATING MOBS AND STEPS
    else:
        return modify_state_factory(state)(
            hero=newHero,
            safeTraps=state.unsafeTraps,
            unsafeTraps=state.safeTraps,
            mobs=frozenset(newMobs),
            steps=state.steps - cost,
            blocks=frozenset(newBlocks)
        )


def do_inplace(action: Action, state: State, map_rules: Dict[str, set]):

    hero = state.hero
    goal = map_rules["D"]
    blocks = state.blocks
    mobs = state.mobs
    spikes = map_rules["S"]
    safeTraps = state.safeTraps
    unsafeTraps = state.unsafeTraps
    key = state.key
    lock = state.lock

    newHero = one_step(hero, action.direction)

    # DEFINES FACTORIES
    free = free_factory(map_rules)

    if action.verb == "move":
        if free(newHero) and not (newHero in mobs | blocks):
            return updating_state(map_rules, state, newHero)

    if action.verb == "push":
        newPose = one_step(newHero, action.direction)
        if (newHero in blocks | mobs) and free(newPose) and not (newPose in mobs | blocks) and not newPose == lock and not newPose == goal:
            if newHero in blocks:
                return updating_state(map_rules, state, newHero, blocks=moving_frozenset(blocks, newHero, newPose))
            if newHero in mobs:
                return updating_state(map_rules, state, newHero, mobs=moving_frozenset(mobs, newHero, newPose))

    return None


# DEFINING GOAL
def goal_factory(map_rules: Dict[str, set]) -> Callable[[State], bool]:
    def goals(state: State):
        offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        goalsCases = [ (state.hero[0] + x[0], state.hero[1] + x[1]) for x in offsets]
        for demon in map_rules['D']:
            if demon in goalsCases:
                return True
        return False

    return goals


# DEFINING SUCCESSORS
def succ_factory(map_rules: Dict[str, set]) -> Set[Tuple[State, Action]]:
    def succ(state):
        l = []
        for x in actions.values():
            for a in x:
                l.append((do_inplace(a, state, map_rules), a))
        return {el[0]: el[1] for el in l}

    return succ


# SEARCH ALGO
def search_with_parent(s0, goals, succ, remove, insert, debug=True):
    l = [s0]
    save = {s0: None}
    s = s0
    while l:
        s, l = remove(l)
        for s2, a in succ(s).items():
            #if debug:
            #    print("S=", s2)
            #    print("A=", a)
            if not s2:
                continue
            if not s2 in save:
                save[s2] = (s, a)
                if goals(s2):
                    return s2, save
                insert(s2, l)
    return None, save

def main():
    # récupération du nom du fichier depuis la ligne de commande
    filename = sys.argv[1]

    # récupération de al grille et de toutes les infos
    infos = grid_from_file(filename)
    map_rules, s0 = parsingInfos(infos["grid"], infos["max_steps"])

    end, save = search_with_parent(s0, goal_factory(map_rules), succ_factory(map_rules), remove_head, insert_tail, debug=False)

    # for s, _ in dict2path(end, save):
    #     if s:
    #         print(s)

    # calcul du plan
    if(end):
        plan = ''.join([a for _, a in dict2path(end, save) if a])
        if check_plan(plan):
            print("[OK]", plan)
        else:
            print("[Err]", plan, file=sys.stderr)
    else:
        print("Pas de solution trouvée")

    sys.exit(2)

def testing():
    mobs = set()
    mobs.add((3,4))
    mobs.add((1,7))
    mobs.add((2,9))
    frozen = frozenset(mobs)
    print(moving_frozenset(frozen, (3,4), (7,6)))
    pass

if __name__ == "__main__":
    main()
