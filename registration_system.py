print('===============================')
print('     Registration System')
print('===============================')
registration= False
while registration == False:
  username = input('Enter username:')
  if username=='':
    print('Enter valid username:')
    continue
  password = input('Enter Password:')
  if len(password) < 6:
      print('password should be greater than six digit')
      continue
  pass_check = False
  for i in password:
    if i >='0' and i<='9':
      pass_check = True
      continue
  if pass_check == False:
    print('Password should contain atleast one number')    
    continue
  confirm_password = input('Renter password for confiramtion:')
  if password != confirm_password:
    print('Password doesnt match')
    continue
  else:
    print('Registration Successful!!')
    registration = True