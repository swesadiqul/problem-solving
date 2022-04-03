#Login system
#By@Sadiqul Islam




#problem solve


phone = str()
password = str()
while phone != '06711482':
  phone = input('enter your phone number: ')
  if phone == '01706711482':
      print('Hello,sir.')
  else:
      print('Sorry sir,Wrong number!')
      password = input('enter your password: ')

  while password != 'sadiq82':
    password = input('enter your fassword: ')
    if password == 'sadiq82':
      print('Hello,sir.')
    else:
      print('Sorry sir,Wrong password!')
      password = input('enter your password: ')

print('Welcome,please come in!')
