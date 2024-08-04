from typing import Dict
import json
import os
import argparse

parser = argparse.ArgumentParser(description = 'Generate a template file for a Syncro Phase.')

parser.add_argument('--name', type = str, required = True, help = 'Phase\'s name.', )
parser.add_argument('--path', type = str, required = False, default = 'phases', help = 'Path to save the template.')

args = parser.parse_args()

template: Dict[str, object] = {
  "name": str(args.name),
  "slot_capacity": None,
  "max_plays": None,
  "automaton": {
    "0": {
      "Q": None,
      "B": None,
      "T": None,
    },
    "1": {
      "Q": None,
      "B": None,
      "T": None,
    },
    "2": {
      "Q": None,
      "B": None,
      "T": None,
    },
    "3": {
      "Q": None,
      "B": None,
      "T": None,
    },
    "4": {
      "Q": None,
      "B": None,
      "T": None,
    },
  }
}

os.makedirs(args.path, exist_ok = True)

with open(os.path.join(args.path, f'{args.name}.json'), 'w') as file:
  json.dump(template, file, ensure_ascii = True, indent = 2)
