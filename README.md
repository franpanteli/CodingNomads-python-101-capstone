# CodingNomads-python-101-capstone

### About This Repository
I independently completed CodingNomads’ [Python 101 - Introduction to Python](https://codingnomads.com/course/python-programming-101) certification to invest in my Python skills. This course is the first of ten in the [CodingNomads Python Web Development Career Track](https://codingnomads.com/career-track/python-web-development-learn-python-bootcamp). This repository contains my capstone project: a Command-Line Interface (CLI) role-playing game called Dungeons and Dragons. This project has two versions: [Version 1.0](https://github.com/franpanteli/CodingNomads-python-101-capstone/blob/main/dungeons_and_dragon_game.py), developed during the first course as part of this career track, and [Version 2.0](https://github.com/franpanteli/CodingNomads-python-101-capstone/blob/main/dungeons_and_dragon_game_2.0.py), an update with more complex concepts as part of its second course.

---

### Project Overview

#### Version 1.0
- Prompts the player for their name and greets them
- Offers a choice between two doors (left and right)
- The left door leads to an empty room
- The right door leads to a sword, that can be picked up
- The user can encounter a dragon, depending on their choices
- The game is won or lost, which depends on whether the sword has been acquired
- `if` statements and boolean tracking are implemented in terms of game logic

#### Version 2.0
[Version 2.0](https://github.com/franpanteli/CodingNomads-python-101-capstone/blob/main/dungeons_and_dragon_game_2.0.py) is an extension of this project, completed as part of the [CodingNomads 2 Python 201 - Procedural Python course](https://codingnomads.com/course/python-programming-201).   
- The user can choose between four rooms, instead of two: left, right, forward, and back
- An inventory system is used, in which players can pick up items (a sword and or shield)
- The user can encounter and fight a dragons and or goblin as a result of their door choices
- Battles use a randomised dice roll, to decide whether the user wins the game
- Losing a fight causes the user's inventory to be completely wiped
- Functions are used for repeated logic (for example, the `fight()` and `explore_room()` functions)

---

### Applied Skills
- Variables, data types, input/output
- Conditional logic: `if`, `elif`, `else`
- Loops: an infinite `while` loop (Version 2.0) 
- Functions and parameters 
- Lists for inventory management
- Randomisation, using the `random` module
- CLI-based game design

---

### To Clone This Repository
```bash
git clone https://github.com/franpanteli/CodingNomads-python-101-capstone.git




