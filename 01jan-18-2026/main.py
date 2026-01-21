def main():

    with open("./input.txt") as file:
        for line in file:
            number_ranges = line.strip().split(',')
            for item in number_ranges: 
                numbers = item.split('-')
                start = int(numbers[0])
                end = int(numbers[1])
            for every_number in range (start, end +1):
                string = str(every_number)
                length = len(string)
            if length % 2 == 0:
                mid = length // 2
                first_half = string[:mid]
                second_half = string[mid:]
            if first_half == second_half: 
                total = total + every_number
            print("Answer:", total)
main()
