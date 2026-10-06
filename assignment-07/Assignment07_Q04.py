# Assignment 07 Q04 - Armaan Bhandal

import csv

def main():
    with open("products.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        data = [row for row in reader]

    print(f"{'product':<10} {'color':<10} {'price':<10}")
    for row in data:
        print(f"{row[0]:<10} {row[1]:<10} {row[2]:<10}")

    total_suits = sum(int(row[2]) for row in data if row[0] == 'suit')
    total_shoes = sum(int(row[2]) for row in data if row[0] == 'shoes')

    print(f"Total suits price {total_suits}")
    print(f"Total shoes price {total_shoes}")

if __name__ == "__main__":
    main()
