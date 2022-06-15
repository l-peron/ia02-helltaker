# SOLVEUR DE NIVEAU DU JEU HELLTAKER POUR L'UV IA02

## Présentation

Projet de solving de niveau du jeu helltaker, comprenant une solution résolvant les niveaux en python et une solution les resolvant en ASP.
Projet réalisé par Adrien Simon, Julie Pichon, et Léo Peron.

## Lancement des solveurs

Dans chaque dossier correspondant aux différentes solutions, un README explique comment déployer la solution et l'utiliser sur les niveaux.

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
