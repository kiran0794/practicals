# for i in range(1, 21, 2):   #for count down from 20 to 1
#   print(i, end=' ')
# print()

# for i in range(0, 101, 10):  #count in 10s from 0
#   print(i, end=' ')
# print()

# for i in range(20, 0, -1):  #for count down from 20 to 1
#   print(i, end=' ')
# print()

number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()

for i in range(1, number_of_stars + 1):  # for * output
    print('*' * i)
print()
