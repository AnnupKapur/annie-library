def main():
    position = 50
    count_of_zeros = 0

    with open("./input.txt") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            direction = line[0] # 'R' or 'L'
            amount = int(line[1:]) # number of steps to move

            if direction == "R":
                position = (position + amount) % 100
            elif direction == "L":
                position = (position - amount) % 100

            if position == 0:
                count_of_zeros += 1

    print("")
    print("Answer: ")
    print(count_of_zeros)
    print("")


main()
