# SOLVEUR DE NIVEAU DU JEU HELLTAKER POUR L'UV IA02

## Présentation

Projet de solving de niveau du jeu helltaker, comprenant une solution résolvant les niveaux en python et une solution les resolvant en ASP.
Projet réalisé par Adrien Simon, Julie Pichon, et Léo Peron.

## Lancement des solveurs
### Comment exécuter espace d'état ?

Pour exécuter l'espace d'état, il suffit de faire 
`python3 -l nomdufichier.txt`

### Comment exécuter l'ASP ?
En console, vous avez juste à taper `python3 main.py path_to_txt_file` pour lancer le programme.
Le programme renverra sous la forme "hbgd" un modèle valide pour le niveau

## Structure des niveaux

Un simple `.txt` avec un titre en première ligne, un nombre maximum de coups en deuxième ligne, la description du niveau ensuite. Les lignes ne sont pas forcément finies.

- `H`: hero
- `D`: demoness
- `#`: wall
- ` ` : empty
- `B`: block
- `K`: key
- `L`: lock
- `M`: mob (skeleton)
- `S`: spikes
- `T`: trap (safe)
- `U`: trap (unsafe)
- `O`: block on spike
- `P`: block on trap (safe)
- `Q`: block on trap (unsafe)

### Exemple

```
Level 1
23
     ###
  ### H#
 #  M  #
 # M M#
#  ####
# B  B #
# B B  D#
#########
```

