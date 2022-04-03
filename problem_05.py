str1 = input('Enter first string: ')
str2 = input('Enter second string: ')

s1 = set(str1)
s2 = set(str2)

if s1 & s2:
    common_letters = s1 & s2
    for letter in common_letters:
        print(letter, end=' ')
else:
    print('No Match.')
