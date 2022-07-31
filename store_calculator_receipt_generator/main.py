# python program which will keep adding a stream of numbers inputted by the user .The adding stos as soon as user press Q key on the keyboard

sum=0
while(True):
  user_input = input ("Enter the item price or press q to quit : \n")
  if (user_input != 'q'):
    sum = sum+int(user_input)
    print(f"Order total so far : {sum}")
  else:
    print(f"your bill total is {sum}.\nThanks for shopping with us")
    break