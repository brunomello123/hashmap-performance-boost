Python Example: Performance Comparison Between O(N) and O(1)
This project demonstrates the performance difference between two search approaches using lists and dictionaries in Python.

Objective
The goal of this project is to compare the execution time of a linear search on a list (O(N)) versus an optimized search using a dictionary (O(1)), using an example with large data sets (1,000,000 departments).

Project Structure
main.py: The main file that contains the performance comparison implementation.
Data generation example (10,000,000 departments).
Implementation of two search functions:
get_employees_on(department): Linear search in a list of tuples (O(N)).
get_employees_o1(department): Optimized search using a dictionary (O(1)).
Measuring the execution time of both approaches.
How to Run the Project
Clone this repository to your local environment:

git clone https://github.com/brunomello123/hashmap-performance-boost.git
cd PythonExample

Install Python 3.11 (or higher) if you don't have it already:

# Check if Python is installed
python --version

# Run the main.py script to observe the performance comparison:

python main.py

The program will print the execution time of each approach to the console:

O(N) Time (List search)
O(1) Time (Optimized search with dictionary)

