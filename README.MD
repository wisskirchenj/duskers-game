# IDEA EDU Course

Project implemented in the track 'Practicing Algorithms with Python' of hyperskill.org JetBrains Academy. 
Purpose of doing this project is to make progress in this track and improve my Python knowledge.

## Technology / External Libraries

- Python 3.11.6,
- with packages: jsonpickle, time, datetime, typing, argparse, os, random, unittest, unittest.mock, parameterized

## Repository Contents

The sources of main project tasks (6 stages) and pytest testing.

## Installation

Install the wheel file using pip after clone/fork:

    > pip install dist/duskers-game-3.11.6-py3-none-any.whl

## Program description

Duskers game is a Python-based strategic game inspired by "Duskers" where a team of robots explores mysterious locations
and looks for titanium. We build it from scratch starting from the menu and adding the game hub, some animation,
a few upgrade options, and some spooky enemies to spice things up..

Have fun!

## Project progress

Project was completed on 29.10.23

30.09.23 Project started and Stage 1 completed - welcome and menu for starting, exiting the game

30.09.23 Stage 2 completed - more menu structure, help, high scores added, improved `menu.py`

14.10.23 Stage 3 completed - structure game related stuff into `play.py`, use setup of stage 2 and improve on it.

20.10.23 Stage 4 completed - new modules `pseudo_random.py`, `animation.py` and `explorer.py` to implement explore 
functionality based on random choices. Also use argparse with defaults and positional arguments for parameters (`nargs=?`).

28.10.23 Stage 5 completed - new modules `state.py`, `state_manager.py` to implement load and save of game states, using
jsonpickle to (de-)serialize custom classes.

29.10.23 Final Stage 6 completed - new module `score_manager.py` to implement load and save of scores using
jsonpickle. Added upgrades for display of titanium, encounters with enemies. Robot amount is now variable.
