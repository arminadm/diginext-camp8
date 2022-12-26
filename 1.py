# Armin Darabi Mahboub
from math import ceil

def main():
    input_str = input("Please enter your string: ")
    input_int = int(input("Please enter your integer number: "))
    a_counter = generate_new_string(input_str, input_int)
    print(a_counter)

def generate_new_string(str, n):
    # we have two scenarios
    # 1st scenario: string length is more than integer number
    if len(str) >= n:
        # just cut the string in the requested length
        new_str = str[0:n]

    # 2nd scenario: string length is less than integer number
    else:
        # multiple string length to round_up(n / str_length)
        # then cut the new length in the requested length
        round_up = ceil(n / len(str))
        new_str = (str * round_up)[0:n]

    # count the 'a's and return it
    a_counter = new_str.count('a')
    return a_counter

if __name__ == '__main__':
    main()