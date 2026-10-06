# Assignment 07 Q02 - Armaan Bhandal

import random

def create_data_file(filename):
    ranks = ['assistant', 'associate', 'full']
    with open(filename, 'w') as file:
        for i in range(1, 1001):
            rank = random.choice(ranks)
            if rank == 'assistant':
                salary = random.uniform(50000, 80000)
            elif rank == 'associate':
                salary = random.uniform(60000, 110000)
            else:
                salary = random.uniform(75000, 130000)
            file.write(f"FirstName{i} LastName{i} {rank} {salary:.2f}\n")

def read_data_file(filename):
    totals = {'assistant': 0, 'associate': 0, 'full': 0}
    counts = {'assistant': 0, 'associate': 0, 'full': 0}
    with open(filename, 'r') as file:
        for line in file:
            _, _, rank, salary = line.rsplit(' ', 3)
            salary = float(salary)
            totals[rank] += salary
            counts[rank] += 1
    for rank in totals:
        avg = totals[rank] / counts[rank]
        print(f"Total salary for {rank} professors: {totals[rank]:.2f}")
        print(f"Average salary for {rank} professors: {avg:.2f}")

def main():
    create_data_file("Salary.txt")
    read_data_file("Salary.txt")

if __name__ == "__main__":
    main()
