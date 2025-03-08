# Blind Valley

📌 Project Description

This project utilizes a backtracking algorithm to solve the puzzle game "Blind Valley". The goal is to fill all the spaces with H (High), B (Base), and N (Neutral) stones while following the given constraints.

🚀 Rules

A High (H) stone cannot be adjacent to another High stone.

A Base (B) stone cannot be adjacent to another Base stone.

All empty spaces must be filled.

The number of H and B stones in each row and column must follow the given constraints.

📥 Input Format

The input is taken from a file containing the following information:
1. The first four lines specify the row and column constraints.
   
2. The following lines define the domino layout using L, R, U, and D characters.
   
Example input:

2 1 - -

- - 3 2
    
L R L R

U D U D

📤 Output Format

The program prints a valid solution using H, B, and N characters if a valid arrangement is found. If no solution exists, it prints "No solution!".

Example output:

H B H B

B H B H

or

No solution!

📜 Algorithm Used

This solution employs the backtracking method:
* Starts placing H, B, and N from the top-left corner.
* Checks constraints after each placement.
* If a conflict arises, it backtracks and tries a different option.
