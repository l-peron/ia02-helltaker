import sys
from helltaker_utils import grid_from_file, check_plan
import time
import clingo


def planify_asp(infos):
    """
    this function planifies the grid using the asp solver clingo
    the grid is a file is in the infos argument
    the basis og the asp file is in "helltaker.lp"
    :param infos:
    :return:
    """

    basis = ""

    with open("helltaker.lp", "r", encoding="utf-8") as f:
        basis = f.read()

    # parse the grid in the level_specificities string

    level_specificities += f"step(0..{infos['max_steps']}).\n"
    for i in range(infos["m"]):
        for j in range(infos["n"]):
            if not infos["grid"][i][j] == "#":
                level_specificities += f"cell({i},{j}).\n"
            if infos["grid"][i][j] == "H":
                level_specificities += f"init(at({i},{j})).\n"
            if infos["grid"][i][j] in ("B", "O", "P", "Q"):
                level_specificities += f"init(block({i},{j})).\n"
            if infos["grid"][i][j] == "D":
                level_specificities += f"demoness({i},{j}).\n"
                level_specificities += f"goal(at({i - 1},{j})).\n"
                level_specificities += f"goal(at({i},{j - 1})).\n"
                level_specificities += f"goal(at({i + 1},{j})).\n"
                level_specificities += f"goal(at({i},{j + 1})).\n"
            if infos["grid"][i][j] == "K":
                level_specificities += f"init(key({i},{j})).\n"
            if infos["grid"][i][j] == "L":
                level_specificities += f"init(chest({i},{j})).\n"
            if infos["grid"][i][j] in ("S", "O"):
                level_specificities += f"spikes({i},{j}).\n"
            if infos["grid"][i][j] in ("T", "P"):
                level_specificities += f"{{trap({i}, {j}, S, T) : state_trap(S)}} = 1 :- step(T). :- trap({i}, {j}, S, 0), S != on.\n"
            if infos["grid"][i][j] in ("U", "Q"):
                level_specificities += f"{{trap({i}, {j}, S, T) : state_trap(S)}} = 1 :- step(T). :- trap({i}, {j}, S, 0), S != off.\n"

    asp = level_specificities + basis

    print(asp)

    ctl = clingo.Control()
    ctl.add("base", [], asp)
    # ctl.ground([("base", [])])
    print("ouais3")

    ctl.solve()
    print("ouais4")
    plan = []
    for model in ctl.solve():
        for atom in model.symbols(shown=True):
            if atom.name == "do":
                plan.append(atom.arguments[0].number)

    print(plan)
    return "hbgd"


def main():
    # récupération du nom du fichier depuis la ligne de commande
    filename = sys.argv[1]

    # récupération de al grille et de toutes les infos
    infos = grid_from_file(filename)

    # calcul du plan
    plan = planify_asp(infos)

    # affichage du résultat
    if check_plan(plan):
        print("[OK]", plan)
    else:
        print("[Err]", plan, file=sys.stderr)
        sys.exit(2)


main()
