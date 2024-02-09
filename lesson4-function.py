# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[3:6])

# def a(t, y, *args, j):
#     print(t, y, args, j)
#
# a(1, 2, i=19)

# def funk(count, *args):
#     if count == 0:
#         return ("none")
#     b = 0
#     for i in range(count):
#         # b.append(args[i] + count)
#         b += args[i]
#     return (b, args)
#
#
# print(funk(4, 1,2,3,4,5,6,7)) # -> 10
# print(funk(2, 100,200,300,1000)) # -> 300

# litcode

def roman_to_int(roman_number):
    velue = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
    sum = 0
    for i in range(len(roman_number)):
        sum = roman_number[i]
    return sum


print(roman_to_int("III")) # -> 3
