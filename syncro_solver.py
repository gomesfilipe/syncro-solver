from typing import Dict, List, Union, MutableSet
import copy

class SyncroSolver():
  def __init__(
      self,
      name: str,
      automaton: Dict[str, Dict[str, str]],
      slot_capacity: int,
      max_plays: int,
      slots: Union[Dict[str, int], None] = None
    ) -> None:
    self.__name = name
    self.__automaton = automaton
    self.__slot_capacity = slot_capacity
    self.__max_plays = max_plays

    self.__slots = self.__default_slots() if slots is None else slots
    self.__converted_automaton, self.__buttons = self.__convert_automaton()

    self.__stack: List[str] = []
    self.__solutions: List[List[str]] = []

  def __default_slots(self) -> Dict[str, int]:
    slots = {}

    for slot in self.__automaton:
      slots[slot] = 1

      for button in self.__automaton[slot]:
        slots[self.__automaton[slot][button]] = 1

    return slots

  def __convert_automaton(self) -> Dict[str, Dict[str, str]]:
    converted_automaton = {}
    buttons: MutableSet[int] = set()

    for slot in self.__automaton:
      for button in self.__automaton[slot]:
        buttons.add(button)

        if button in converted_automaton:
          converted_automaton[button][slot] = self.__automaton[slot][button]
        else:
          converted_automaton[button] = {}
          converted_automaton[button][slot] = self.__automaton[slot][button]

    return converted_automaton, list(buttons)

  def __press_button(self, button: str) -> Dict[str, int]:
    tmp_slots = copy.deepcopy(self.__slots)

    for slot1 in self.__converted_automaton[button]:
      slot2 = self.__converted_automaton[button][slot1]

      tmp_slots[slot2] += self.__slots[slot1]
      tmp_slots[slot1] -= self.__slots[slot1]

    return tmp_slots

  def __check_vitory(self) -> bool:
    return any(self.__slots[slot] == self.__slot_capacity for slot in self.__slots)

  def solve(self, all_solutions: bool = False) -> List[str]:
    self.__stack = []
    self.__solutions = []

    for _button in self.__buttons:
      if self.__solve_recursive(_button, all_solutions) and not all_solutions:
        return self.__solutions

    return self.__solutions

  def __solve_recursive(self, button: str, all_solutions: bool = False) -> bool:
    slots_backup = copy.deepcopy(self.__slots)
    self.__stack.append(button)

    self.__slots = self.__press_button(button)

    if self.__check_vitory():
      self.__solutions.append(self.__stack.copy())
      self.__slots = slots_backup
      self.__stack.pop()
      return True

    if len(self.__stack) == self.__max_plays:
      self.__slots = slots_backup
      self.__stack.pop()
      return False

    for _button in self.__buttons:
      if self.__solve_recursive(_button, all_solutions) and not all_solutions:
        return True

    self.__slots = slots_backup
    self.__stack.pop()
    return False

  def solve_to_dict(self, all_solutions: bool = False, format_solutions: bool = False) -> Dict[str, Union[str, List[str]]]:
    self.solve(all_solutions)

    return {
      'name': self.__name,
      'solutions': self.__format_solutions() if format_solutions else self.__solutions,
    }

  def __format_solutions(self) -> List[str]:
    return ['[' + ', '.join(solution) + ']' for solution in self.__solutions]
