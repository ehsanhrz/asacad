
# sorted_number takes a number in string format and finds the last match to the solution.
# like : input = 132 then  output = 129

def sorted_number(number):
    _number = int(number)
    while _number > 0:
        next = 1
        digits = [x for x in str(_number)]
        for  i in digits:
            try:
                compare = int(digits[next])
            except IndexError:
                return _number
            if int(i) > compare:
                _number -= 1
                break
            else:
                next += 1
                
            
def main():
    num = sorted_number(input("Enter The Number Here:"))
    print(num)



if __name__ == "__main__":
    main()



