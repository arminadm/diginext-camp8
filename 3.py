# Armin Darabi Mahboub

def main():
    str = input('Please enter your array: ')
    
    # convert given string(which is our array, but in string format) to the list of json
    value_index_list = []
    index = 0
    for str_num in str[1:-1].split(','):
        value_index_list.append({int(str_num): index})
        index += 1

    # sort this list of json by its keys(array values)
    # exp: ([{3: 0}, {7: 1}, {1: 2}] => [{1: 2}, {3: 0}, {7: 1}])
    value_index_list.sort(key=lambda x: list(x.keys())[0])
    
    # for each object, we need to check if it's previous_index(value) is equal to list index or not
    # exp: tmp = [{1: 2}, {3: 0}, {7: 1}], tmp[0] => {1:2}, 2 is the previous_index(value) and 0 is the list index
    list_index = 0
    swap_counter = 0
    while(list_index < len(value_index_list)):
        object = value_index_list[list_index]
        previous_index = list(object.values())[0]

        if previous_index == list_index:
            # increment list index and pass to the next object
            list_index += 1
            
        elif previous_index != list_index:
            # swap two cells, do not increment index
            swap_index = list(object.values())[0]
            swap_obj = value_index_list[swap_index]
            value_index_list[list_index] = swap_obj
            value_index_list[swap_index] = object
            swap_counter += 1
    
    print(swap_counter)
    
if __name__ == '__main__':
    main()