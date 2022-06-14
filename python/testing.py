import os

def main():
    print("SIMULATION TOUS LES NIVEAUX")
    for i in range(1,10):
        print("------------------------------------")
        os.system(f"python3 main.py -l ../levels/level{i}.txt")
    pass

if __name__ == "__main__":
    main()