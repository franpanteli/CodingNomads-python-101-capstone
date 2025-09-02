# CodingNomads-python-101-capstone

### About This Repository
I independently completed CodingNomads’ [Python 101 - Introduction to Python](https://codingnomads.com/course/python-programming-101) certification, to invest in my Python skills. This course is the first of ten in the [CodingNomads Python Web Development Career Track](https://codingnomads.com/career-track/python-web-development-learn-python-bootcamp). This repository contains my capstone project: a **Command-Line Interface (CLI) role-playing game** called *Dungeons and Dragons*. This project has two versions, Version 1.0, developed during the first course as part of this career track, and Version 2.0, an update with more complex concepts as part of its second course.

---

### Project Overview

#### Version 1.0
- Prompts the player for their name and greets them
- Offers a choice between two doors (left or right)
- Left door: empty room
- Right door: sword that can be picked up
- Encounter a dragon depending on player choices
- Win or lose depends on whether the sword is acquired
- Implements `if` statements and boolean tracking for simple game logic

#### Version 2.0 (Extension)
[Version 2.0](https://github.com/franpanteli/CodingNomads-python-101-capstone/blob/main/dungeons_and_dragon_game_2.0.py) is an extension of this project, completed as part of the [CodingNomads 2 Python 201 - Procedural Python course](https://codingnomads.com/course/python-programming-201).  
- Introduces multiple rooms: left, right, forward, and back
- Implements an **inventory system**: players can pick up items (sword, shield)
- Adds multiple enemies: dragons and goblins
- Battles use a **randomised dice roll** to determine victory
- Losing a fight results in **inventory loss**
- Randomised room outcomes make gameplay more dynamic and replayable
- Functions abstract repeated logic (e.g., `fight()`, `explore_room()`)

---

### Skills Demonstrated
- Python fundamentals: variables, data types, input/output
- Conditional logic: `if`, `elif`, `else`
- Loops: `while` for game flow
- Functions and parameters for modular code
- Lists and inventory management
- Randomisation using the `random` module
- CLI-based game design

---

### How to Run the Game
1. Clone this repository:
```bash
git clone https://github.com/franpanteli/CodingNomads-python-101-capstone.git

