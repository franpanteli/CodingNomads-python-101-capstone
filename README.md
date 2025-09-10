# CodingNomads-python-101-capstone

### About This Repository
I independently completed CodingNomads’ [Python 101 - Introduction to Python](https://codingnomads.com/course/python-programming-101) certification to invest in my Python skills. This course is the first of ten in the [CodingNomads Python Web Development Career Track](https://codingnomads.com/career-track/python-web-development-learn-python-bootcamp). This repository contains my capstone project for this course. This is a Command-Line Interface (CLI) role-playing game inspired by Dungeons and Dragons. This project has three versions: [Version 1.0](https://github.com/franpanteli/CodingNomads-python-101-capstone/blob/main/dungeons_and_dragon_game.py), developed during the first course as part of this career track, [Version 2.0](https://github.com/franpanteli/CodingNomads-python-101-capstone/blob/main/dungeons_and_dragon_game_2.0.py) and [Version 3.0](https://github.com/franpanteli/CodingNomads-python-101-capstone/blob/main/dungeons_and_dragon_game_3.0.py), containing updates with more complex concepts as part of the second course in the career track.

---

### Project Overview

#### Version 1.0
- The player is prompted for their name and is greeted by the game
- The user is offered a choice between two doors (left and right)
- The left door leads to an empty room
- The right door leads to a sword that can be picked up
- The user can next encounter a dragon, depending on their choice of door
- The game is won or lost, depending on whether the sword has been acquired
- `if` statements and Boolean tracking are implemented in terms of game logic

#### Version 2.0
[Version 2.0](https://github.com/franpanteli/CodingNomads-python-101-capstone/blob/main/dungeons_and_dragon_game_2.0.py) is an extension of Version 1.0, completed as part of the [CodingNomads 2 Python 201 - Procedural Python course](https://codingnomads.com/course/python-programming-201). The stages of this version are as follows:   
- The user can choose between four rooms, instead of two: left, right, forward, and back
- An inventory system is used, in which players can pick up items (a sword and or shield)
- The user can encounter and fight a dragon and or a goblin, as a result of their door choices
- Battles use a randomised dice roll to decide whether the user wins the game
- Losing a fight causes the user's inventory to be completely wiped
- Functions are used for repeated logic (for example, the `fight()` and `explore_room()` functions)

#### Version 3.0
[Version 3.0](https://github.com/franpanteli/CodingNomads-python-101-capstone/blob/main/dungeons_and_dragon_game_3.0.py) is the same as the second version of the game. However, it leverages a new function called log_status(), which appends the moves that the user makes throughout the game to a new txt file called [game_log.txt](https://github.com/franpanteli/CodingNomads-python-101-capstone/blob/main/game_log.txt). This is done by leveraging the Python open() function in append mode, to append the user's moves to an output txt file.

---

### Python Concepts Applied
- Variables, data types, input/output
- Conditional logic: `if`, `elif`, `else`
- Loops: an infinite `while` loop (Version 2.0) 
- Functions and parameters 
- Lists for inventory management
- Randomisation, using the `random` module
- CLI-based game design
- File I/O
- Sets ({} collections)
- f-Strings
- Global variables
- Imports / modules
- Return values in functions
- Docstrings

---

### To Clone This Repository
```bash
git clone https://github.com/franpanteli/CodingNomads-python-101-capstone.git



