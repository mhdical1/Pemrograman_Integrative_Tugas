def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def print_sum_with_comma_separator(numbers):
    total = sum(numbers)
    formatted_total = '{:,.2f}'.format(total)
    print(formatted_total, end="")

def main():
    numbers = read_numbers_from_file('indata.txt')
    print_sum_with_comma_separator(numbers)

if __name__ == "__main__":
    main()