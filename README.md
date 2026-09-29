# Practice files for learning Python

This repository contains a set of practice files to work through, starting easy and gradually getting more difficult. Some problems may be open ended, others may have more specific tasks. A comment at the top of each file will tell you your objective and any potential restrictions. **A** solution for a given file will generally be stored next to it, under the same name, but with `-SOLUTION` tacked on before the extension. For many files, the provided solution may not be the only way to complete that objective, perhaps not even the *best* way to complete the objective.

This is *not* meant to teach you Python on its own. This is meant to provide self-paced practice to supplement a proper curriculum. If you wish to learn Python from scratch, view [the official Python 3 documentation](https://docs.python.org/3/tutorial/index.html), or check out [the Python tutorial offered by W3Schools](https://www.w3schools.com/python/default.asp).

This repository is a work in progress. Please have patience.

I would suggest using VS Code as your IDE if you have not chosen an IDE yet. If you cannot install an IDE locally (for example if you are using a Chromebook) I would suggest using the [CS50 IDE](https://cs50.dev/), a cloud based IDE hosted by Harvard. (yes, that Harvard)

## Getting Started

To start, clone this repository into your workspace. The command below will clone the files into their own folder within the current working directory.
```
git clone https://github.com/Probably-Artemis/python-practice.git
```
For example, if I run that command from `~/work`, I will end up with `~/work/python-practice`. The file you are currently reading would thus be at `~/work/python-practice/README.md`.

If you use Windows, the above file paths likely look odd. If I run the command on Windows from `C:\Users\artemis\work`, the README file you're currently reading would be at `C:\Users\artemis\work\python-practice\README.md`.

If you do not wish to clone the repository from the terminal, you may instead download (and extract) a compressed zip archive [here](https://github.com/Probably-Artemis/python-practice/archive/refs/heads/main.zip).

## Running a File

While your IDE may provide you a shiny new run button to skip typing out the command, you should learn the commands.

You cannot run a Python file without the Python language installed. These files in particular expect you to use [Python 3](https://www.python.org/downloads/).

To run a file in Python, type `python3` followed by the relative path to the file you wish to run. If you are using Windows, `python3` may not work, in which case simply use `python` or `py` instead. For example, to run the introductory file in the strings section, I would run the following command from the project root (the `python-practice` folder).
```
python3 basics/strings/01-intro.py
```

---

## Basics

You should **start with [strings](https://github.com/Probably-Artemis/python-practice/tree/main/basics/strings)**, then progress to numbers, input, booleans, conditionals, loops, and finally lists. Beyond these sections, simply work on what you need to refresh. Dictionaries, tuples, and sets for example may call upon things from all prior sections.

## Debugging Basics

This section contains folders similar to Basics, but with a focus on debugging existing code instead of writing your own. Same suggested progression as Basics.

---

## Contributing

If you wish to contribute, create an issue or pull request!

## Questions

If you know me in person and use these files to practice, I am more than happy to answer your questions. You know how to reach me.

<sup>(hint: it's by walking up to me and just asking the question)</sup>

## An Aside

Developers frequently preach a far higher standard than they actually practice. I am not an exception. This repository is an amalgam of the fruit of my time assisting in introductory Python courses, not in the slightest how I actually write my code on a day-to-day basis.