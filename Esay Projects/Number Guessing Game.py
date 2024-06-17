import random

#random.randrange(start,stop)
top_range = input("type a number :")

if top_range.isdigit():
   top_range = int(top_range)
   
   if top_range <= 0 :
          print ('Please type a number larger than 0 next time.')
          quit()
          
else :
       
   print('Add a number next time please.')
   quit()       
   
   
random_number=random.randint(0,top_range)
guesses = 0 


while True :
   guesses += 1
   user_guesses=input("Inter your guesse :")
   
   if user_guesses.isdigit() :
      user_guesses = int(user_guesses)
      
   else:
        print('Please type a number next time.')
        continue
   
   if user_guesses == random_number:
      print ('your guesse is correct !')
      break
   elif user_guesses > random_number:
          
      print("You were above the number!")
      
   else:
          
        print("You were below the number!")

print("You got it in", guesses, "guesses")