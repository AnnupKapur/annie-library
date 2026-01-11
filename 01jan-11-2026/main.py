def main():
    with open("./input.txt") as file:
        for line in file:
            direction = line[0]
            amount = line[1:]

main()
