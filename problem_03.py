# mydict = {'s_01': 10, 's_04': 9}

# if mydict['s_01'] > mydict['s_04']:
#   print('Maximum number has got: '+ 's_01 -', mydict['s_01'])
# else:
#   print('Maximum number has got: '+ 's_04 -', mydict['s_04'])


mydict = {'st-01': 78, 'st-02': 56, 'st-03': 79, 'st-04': 77}

if mydict['st-01'] > mydict['st-02'] and mydict['st-01'] > mydict['st-03'] and mydict['st-01'] > mydict['st-04']:
  print('Maximum number has got: ' + 'st-01-', mydict['st-01'])

elif mydict['st-02'] > mydict['st-03'] and mydict['st-02'] > mydict['st-04']:
  print('Maximum number has got: ' + 'st-02-', mydict['st-02'])

elif mydict['st-03'] > mydict['st-04']:
  print('Maximum number has got: ' + 'st-03-', mydict['st-03'])

else:
  print('Maximum number has got: ' + 'st-04', mydict['st-04'])