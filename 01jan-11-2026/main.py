def main():
    start_position = 50
    count_of_zeros = 0

    with open("./input.txt") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            amount = int(line[1:])

            if direction == "R":
                start_position = (start_position + amount) % 100
            elif direction == "L":
                start_position = (start_position - amount) % 100

            if start_position == 0:
                count_of_zeros += 1

    print(count_of_zeros)


main()

