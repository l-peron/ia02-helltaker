import sys
import time
from optparse import OptionParser

from helltaker_utils import grid_from_file, check_plan
import heapq
from typing import (
    Dict,
    List,
    Tuple,
    Callable,
    Set,
    NamedTuple,
    FrozenSet,
    Optional,
    Union,
)

Action = NamedTuple("Action", [("verb", str), ("direction", str)])

actionNames = ["move", "push", "kill", "unlock/key"]

actions: Dict[str, Action] = {d: [] for d in "hbgd"}

for d in "hbgd":
    for a in actionNames:
        actions[d].append(Action(a, d))

State = NamedTuple(
    "State",
    [
        ("hero", Tuple[int, int]),
        ("steps", int),
        ("blocks", FrozenSet[Tuple[int, int]]),
        ("key", Tuple[int, int]),
        ("lock", Tuple[int, int]),
        ("mobs", FrozenSet[Tuple[int, int]]),
        ("safeTraps", FrozenSet[Tuple[int, int]]),
        ("unsafeTraps", FrozenSet[Tuple[int, int]]),
    ],
)

# ALL UTILS

# DICT 2 PATH (print)
def dict2path(
    s: State, d: Dict[State, Tuple[State, Action]]
) -> List[Tuple[State, Optional[str]]]:

    l: List[Tuple[State, Optional[str]]] = [(s, None)]
    while not d[s] is None:
        parent, a = d[s]
        l.append((parent, a.direction))
        s = parent
    l.reverse()
    return l


# PILE / FILES UTILS


def insert_tail(s: State, l: List[State]):
    l.append(s)
    return l


def insert_head(s: State, l: List[State]):
    l.insert(0, s)
    return s


def remove_head(l: List[State]):
    return l.pop(0), l


def remove_tail(l: List[State]):
    return l.pop(), l


# PARSING ELEMENTS TO FLUENTS AND NON FLUENTS
def parsingInfos(
    grid: List[List[str]], maxstep: int, m: int, n: int
) -> Tuple[Dict[str, set], State]:

    hero = None
    blocks = set()
    key = None
    lock = None
    mobs = set()
    safeTraps = set()
    unsafeTraps = set()

    map_rules: Dict[str, Union[set, int]] = {
        "D": set(),
        "S": set(),
        "#": set(),
        "max": int,
    }

    map_rules["max"] = maxstep

    for x in range(m):
        for y in range(n):
            if grid[x][y] == "#":
                map_rules["#"].add((x, y))
            if grid[x][y] == "D":
                map_rules["D"].add((x, y))
            if grid[x][y] == "S" or grid[x][y] == "O":
                map_rules["S"].add((x, y))
            if grid[x][y] == "H":
                hero = (x, y)
            if grid[x][y] in ["B", "P", "Q", "O"]:
                blocks.add((x, y))
            if grid[x][y] in ["K"]:
                key = (x, y)
            if grid[x][y] in ["L"]:
                lock = (x, y)
            if grid[x][y] in ["M"]:
                mobs.add((x, y))
            if grid[x][y] in ["T", "P"]:
                safeTraps.add((x, y))
            if grid[x][y] in ["U", "Q"]:
                unsafeTraps.add((x, y))

    state = State(
        hero,
        maxstep,
        frozenset(blocks),
        key,
        lock,
        frozenset(mobs),
        frozenset(safeTraps),
        frozenset(unsafeTraps),
    )

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


def moving_frozenset(
    fset: frozenset, supr: Tuple[int, int] = None, new: Tuple[int, int] = None
):
    raw = {x for x in fset}
    if supr:
        raw.remove(supr)
    if new:
        raw.add(new)
    return frozenset(raw)


# CHECK IF FREE
def free_factory(map_rules):
    def free(position):
        return not ((position in map_rules["#"]) or (position in map_rules["D"]))

    return free


def updating_state(
    map_rules: Dict[str, List[int]],
    state: State,
    newHero: Tuple[int],
    mobs: FrozenSet[Tuple[int, int]] = frozenset(),
    blocks: FrozenSet[Tuple[int, int]] = frozenset(),
    keyFinded: bool = False,
    lockOpenable: bool = False,
    mobCleared: bool = False,
):

    # KILLINGS MOBS
    newMobs = state.mobs
    if mobs or mobCleared:
        newMobs = frozenset(mobs)
    for mob in newMobs:
        if (mob in state.safeTraps) or (mob in map_rules["S"]):
            newMobs = moving_frozenset(newMobs, supr=mob)

    # KEY AND CHEST INTERACTIONS
    newLock = state.lock
    if lockOpenable:
        newLock = tuple()
    newKey = state.key
    if keyFinded:
        newKey = tuple()

    # MOVING BLOCKS IF NECESSARY
    newBlocks = state.blocks
    if blocks:
        newBlocks = blocks

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
            blocks=frozenset(newBlocks),
            lock=newLock,
            key=newKey,
        )


def do_inplace(action: Action, state: State, map_rules: Dict[str, set[int]]):

    hero = state.hero
    blocks = state.blocks
    mobs = state.mobs
    key = state.key
    lock = state.lock

    newHero = one_step(hero, action.direction)

    # DEFINES FACTORIES
    free = free_factory(map_rules)

    if action.verb == "move":
        if (
            free(newHero)
            and not (newHero in mobs | blocks)
            and newHero != lock
            and newHero != key
        ):
            return updating_state(map_rules, state, newHero)

    if action.verb == "push":
        newPose = one_step(newHero, action.direction)
        if newHero in blocks:
            if not free(newPose) or newPose in mobs | blocks or newPose == lock:
                return updating_state(
                    map_rules,
                    state,
                    hero
                )
            elif free(newPose) and (not newPose in mobs | blocks) and newPose != lock:
                return updating_state(
                    map_rules,
                    state,
                    hero,
                    blocks=moving_frozenset(blocks, newHero, newPose)
                )
        if newHero in mobs and newPose != key and free(newPose) and not (newPose in mobs | blocks) and not newPose == lock:
            return updating_state(
                map_rules,
                state,
                hero,
                mobs=moving_frozenset(mobs, newHero, newPose),
            )

    if action.verb == "kill":
        newPose = one_step(newHero, action.direction)
        if (newHero in mobs) and (
            not free(newPose) or newPose in blocks or newPose == lock
        ):
            if not moving_frozenset(mobs, newHero):
                return updating_state(
                    map_rules,
                    state,
                    hero,
                    mobs=moving_frozenset(mobs, newHero),
                    mobCleared=True,
                )
            else:
                return updating_state(
                    map_rules, state, hero, mobs=moving_frozenset(mobs, newHero)
                )

    if action.verb == "unlock/key":

        if newHero == lock and not key:
            return updating_state(
                map_rules,
                state,
                newHero,
                lockOpenable=True,
            )
        if newHero == key and not key in blocks:
            return updating_state(map_rules, state, newHero, keyFinded=True)

    return None


# DEFINING GOAL
def goal_factory(map_rules: Dict[str, set]) -> Callable[[State], bool]:
    def goals(state: State):
        offsets = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        goalsCases = [(state.hero[0] + x[0], state.hero[1] + x[1]) for x in offsets]
        for demon in map_rules["D"]:
            if demon in goalsCases:
                return True
        return False

    return goals


# DEFINING SUCCESSORS
def succ_factory(map_rules: Dict[str, set]) -> Callable[[State], Dict[State, Action]]:
    def succ(state: State) -> Dict[State, Action]:
        l = []
        for x in actions.values():
            for a in x:
                l.append((do_inplace(a, state, map_rules), a))
        return {el[0]: el[1] for el in l}

    return succ


# DEFINING HEURISTIC

# GLOUTON
def manhattan_distance_factory(map_rules: Dict[str, set]) -> Callable:
    def dist_to_closest_demon(state: State) -> int:
        return min(
            abs(state.hero[0] - demon[0]) + abs(state.hero[1] - demon[1])
            for demon in map_rules["D"]
        )

    return dist_to_closest_demon


# A*
def manhattan_distance_astar_factory(map_rules: Dict[str, set]) -> Callable:
    def dist_to_closest_demon(state: State, action: Action) -> int:
        manOrClid = True
        passedCost = (1/(1 + map_rules["max"] - state.steps))
        booster = 1
        minDist = 0
        if state.key:
            if manOrClid:
                minDist = ((state.key[0] - state.hero[0])**2 + (state.key[1] - state.hero[1])**2)**(1/2)
            else:
                minDist = abs(state.key[0] - state.hero[0]) + abs(state.key[1] - state.hero[1])
            if action:
                booster = (0.8, 0.6)[action.verb == "unlock/key"]
        if state.lock and not state.key:
            if manOrClid:
                minDist = ((state.lock[0] - state.hero[0]) ** 2 + (state.lock[1] - state.hero[1]) ** 2) ** (1/2)
            else:
                minDist = abs(state.lock[0] - state.hero[0]) + abs(state.lock[1] - state.hero[1])
            if action:
                booster = (0.4, 0.2)[action.verb == "unlock/key"]
        else:
            if manOrClid:
                minDist = min(
                    ((demon[0] - state.hero[0]) ** 2 + (demon[1] - state.hero[1]) ** 2) ** (1/2)
                    for demon in map_rules["D"]
                )
            else:
                minDist = min(
                    abs(state.hero[0] - demon[0]) + abs(state.hero[1] - demon[1])
                    for demon in map_rules["D"]
                )
        return minDist*1*booster + passedCost*1.5

    return dist_to_closest_demon

# SEARCH ALGO (GREEDY & A*)
def search_heuristic(
    s0: State,
    goals: Callable,
    succ: Callable,
    heuristic,
    debug: bool = True,
) -> Tuple[State, Dict[State, Action]]:
    l = []
    heapq.heapify(l)
    heapq.heappush(l, (heuristic(s0, None), s0))
    save = {s0: None}
    heapq.heapify(l)
    while l:
        score, s = heapq.heappop(l)
        for s2, a in succ(s).items():
            if debug:
                print("Previous State=", s)
                print("A=", a)
                print("New State =", s2)
            if not s2:
                continue
            if not s2 in save:
                save[s2] = (s, a)
                if goals(s2):
                    return s2, save
                heapq.heappush(l, (heuristic(s2, a), s2))
    return None, save


# SEARCH ALGO (DSF & BSF)
def search_with_parents(
    s0: State,
    goals: Callable,
    succ: Callable,
    remove: Callable,
    insert: Callable,
    debug: bool = True,
) -> Tuple[State, Dict[State, Action]]:
    l = [s0]
    save = {s0: None}
    s = s0
    while l:
        s, l = remove(l)
        for s2, a in succ(s).items():
            if debug:
                print("Previous State=", s)
                print("A=", a)
                print("New State =", s2)
            if not s2:
                continue
            if not s2 in save:
                save[s2] = (s, a)
                if goals(s2):
                    return s2, save
                insert(s2, l)
    return None, save


def readCommand(argv: List[str]) -> List[str]:

    parser = OptionParser()
    parser.add_option(
        "-l",
        "--level",
        dest="HellTakerLevels",
        help="level of game to play",
        default="level1.txt",
    )
    parser.add_option(
        "-m", "--method", dest="agentMethod", help="research method", default="astar"
    )
    args = dict()
    options, _ = parser.parse_args(argv)

    args["layout"] = grid_from_file(options.HellTakerLevels)
    args["method"] = options.agentMethod
    return args


def main():

    # Récupération Grille et Méthode de recherche
    infos, method = readCommand(sys.argv[1:]).values()
    map_rules, s0 = parsingInfos(
        infos["grid"], infos["max_steps"], infos["m"], infos["n"]
    )

    end, save = None, None

    if method == "astar":
        end, save = search_heuristic(
            s0,
            goal_factory(map_rules),
            succ_factory(map_rules),
            manhattan_distance_astar_factory(map_rules),
            debug=False,
        )
    if method == "greedy":
        end, save = search_heuristic(
            s0,
            goal_factory(map_rules),
            succ_factory(map_rules),
            manhattan_distance_factory(map_rules),
            debug=False,
        )
    if method == "bfs":
        end, save = search_with_parents(
            s0,
            goal_factory(map_rules),
            succ_factory(map_rules),
            remove_head,
            insert_tail,
            debug=False,
        )
    if method == "dfs":
        end, save = search_with_parents(
            s0,
            goal_factory(map_rules),
            succ_factory(map_rules),
            remove_head,
            insert_head,
            debug=False,
        )

    if end:
        plan = "".join([a for _, a in dict2path(end, save) if a])
        if check_plan(plan):
            #print("[Niveau] ", infos["title"])
            #print(f"[Temps] {(stop-start)*1000:.2f} ms")
            print(plan)
        else:
            print("[Err]", plan, file=sys.stderr)
    else:
        print("Pas de solution trouvée")

    sys.exit(2)


if __name__ == "__main__":
    main()
