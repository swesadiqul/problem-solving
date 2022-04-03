mylist = [1,2,3,4,5,6]

even = 0
odd = 0
for single_item in mylist:
  if single_item % 2 == 0 :
    even += single_item
  else:
    odd += single_item

print('Sum of all even,odd number in the list: ', even, odd, end=' ')