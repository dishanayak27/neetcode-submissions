from typing import List

def read_integers() -> List[int]:
    input_string = input()
    input_list = input_string.split(',')
    num_list = []
    for num in input_list:
        num_list.append(int(num))
    return num_list
    pass

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
