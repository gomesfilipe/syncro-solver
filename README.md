# Syncro

<a href="https://rawegg.itch.io/syncro">Syncro</a> is a mathematical game developed by <a href="https://www.youtube.com/@MathGurl" >MathGurl</a>. Its objective is to solve puzzles based in Automata Theory, as explained in this <a href="https://www.youtube.com/watch?v=iXgm0qmP3cw&ab_channel=MathGurl">vídeo</a>.

This repository can solve all phases of game using a recursive bruteforce algorithm. The automatas used in Syncro are in ``/phases`` directory and its answers are in ``/solutions`` directory.

In these files, ``Q``, ``T`` and ``B`` means, respectively, Square, Triangle and Circle. The numbers in ``/phases`` means the index of each slot, which was arbitraly chosen. It's not difficult to understand how the edges are represented.

## Creating your own phase

The script ``run_template.py`` creates a json file that contains the basic structure which SyncroSolver class consider as valid.

Example in command line:

```
python3 run_template.py --name PHASE_NAME --path DIR_TO_SAVE
```

Use ``-h`` flag to read more details of command.

## Finding the solutions

Once you've created your phase, just use ``run_solve.py`` script.

Example in command line:

```
python3 run_solve.py --outdir OUTPUT_DIR --indir PHASE_DIR --filename PHASE_FILENAME --all True
```

Use ``-h`` flag to read more details of command.
