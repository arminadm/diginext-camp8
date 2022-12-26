# Armin Darabi Mahboub

def main():
    str = input("Please enter your string: ")
    counter = how_many_removes_required(str)
    print(counter)

def how_many_removes_required(str):
    counter = 0
    # checking if the character is the same as the next character
    for i in range(len(str) - 1):
        # if so, then increment the counter
        if str[i] == str[i + 1]:
            counter += 1
        # else, do nothing
        else:
            pass
        
    return counter

if __name__ == '__main__':
    main()