#By@Sadiqul Islam
#Leap year


while 1==1:
    year = int(input('Please enter the value of year: '))

    if ((year%4==0 and year%100!=0) or (year%400==0)):
        print('This is a leap Year')

    else:
        print('This is not a leap year.')
        
