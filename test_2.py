import copy

# this function takes an array from 1-10 
# and looks wich number is not present.

def who_is_not_present(array):
    players = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in players:
        if i not in array:
            print(f"{i} is not here")
        else:
            pass

# who_is_late function takes an array from 1-10 
# and looks wich number is late to match by comparing itself by 
# players after him

def who_is_late(array):
    for i in range(len(array)):
        # deepcopy pervents modifying the array     
        new_array = copy.deepcopy(array[i:])
        compare = array[i]
        for j in new_array:
            if j < compare:
                print(f"{j} is late to match")
            else:
                pass


def main():
    array = [1,2,3,4,9,8]
    who_is_not_present(array)
    who_is_late(array)
    

if __name__ == '__main__':
    main()