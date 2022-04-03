#problem_four

'''
Take two name inputs, then print gmail address with a dot between
the first name and last name, all lower case letters
'''

def give_fullname(fname,lname):
  return fname.lower() + '.' + lname.lower() + '@gmail.com'


mail_address1 = give_fullname('John','Snow')
mail_address2 = give_fullname('John','Kabir')

print(mail_address1+ '\n' +mail_address2)
