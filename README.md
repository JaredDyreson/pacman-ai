# pacman-ai

A Pacman maze solving project for CS 481

## Submission 1

Date: 02/19/2021

- Jared Dyreson
- Mason Godfrey
- Chris Nutter
- Estrella Meija

### Tasks Completed

- DFS
- BFS

Both algorithms are implemented using an iterative approach that were outlined in the lectures.
Essentially they function the same but differ in the retrieval of the successors of the currently selected node.
In DFS, you would emplace the children at the front of the container.
The proper data structure for this would be a stack, because it is first in, first out.
DFS requires us to process the current node's children first, then itself.
However in BFS, you would emplace the children at the end of the container.
Here, using a regular queue because it is last in, last out.
BFS requires us to process the current node, and then it's children.
