A collection of my solutions to [Advent of Code 2025](https://adventofcode.com/2025/) challenges.

Remarks: 

* Day 10 second part: In order to solve the problem efficiently, i decided to use `scipy.optimize.milp`.
* Day 12 : A heuristic check to see if each region can be filled with 3x3 shapes of the same total amounts. It turns out that either it is the case or the region surface is simply less than the total surfaces of the required shapes.
