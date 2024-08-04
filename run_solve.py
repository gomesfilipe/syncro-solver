from syncro_solver import SyncroSolver
from typing import List
import json
import time
import os
import argparse
from enum import Enum

def str2bool(value: str):
  if value.lower() in ('yes', 'true', 't', 'y', '1'):
    return True

  if value.lower() in ('no', 'false', 'f', 'n', '0'):
    return False

  raise argparse.ArgumentTypeError(f"Invalid value: {value}. Use yes/no, true/false, y/n, 1/0.")

parser = argparse.ArgumentParser(description = 'Generate a template file for a Syncro Phase.')

parser.add_argument(
  '-od',
  '--outdir',
  type = str,
  required = False,
  default = 'solutions',
  help = 'Directory of solution files. Defaults to \'/solutions\'.',
)

parser.add_argument(
  '-id',
  '--indir',
  type = str,
  required = False,
  default = 'phases',
  help = 'Directory of phase files. Defaults to \'/phases\'.',
)

parser.add_argument(
  '-f',
  '--filename',
  type = str,
  required = False,
  help = 'Phase\'s file. If it is not present, all phases in the given indir will be solved.'
)

parser.add_argument(
  '-a',
  '--all',
  type = str2bool,
  default = False,
  required = False,
  help = 'Generate all existent solutions or only the first found. Defaults to False.'
)

args = parser.parse_args()

phase_filenames = sorted(os.listdir(args.indir)) if args.filename is None else [args.filename]

for phase_filename in phase_filenames:
  start: float = time.time()
  print(f'Solving {phase_filename}', end = ' ', flush = True)

  with open(os.path.join(args.indir, phase_filename), 'r') as file:
    phase = json.load(file)

  syncro_solver = SyncroSolver(
    phase['name'],
    phase['automaton'],
    phase['slot_capacity'],
    phase['max_plays'],
    phase['slots'] if 'slots' in phase else None,
  )

  steps_dict = syncro_solver.solve_to_dict(all_solutions = args.all, format_solutions = True)

  end: float = time.time()
  print(f'Time: {end - start} seconds', end = '\n')

  with open(os.path.join(args.outdir, phase_filename), 'w') as file:
    json.dump(steps_dict, file, ensure_ascii = True, indent = 2)
