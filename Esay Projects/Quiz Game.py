print ("Welcome to my Quize Game!")

play=input("Do you want to play with me ? (Y/N)")

if play == 'Y':
      print ("YES!,let's play")
      score=0
      
else:
      print ("Maybe another time then D:")
      
      
answer=input("The term 'Computer' is derived from ..?")  

if answer == "Latin" :
      print ("Correct!")
      score += 1
else:
    print ("Incorrect!") 
    
    
answer=input("Who is the inventor of 'Difference Engine' ? ") 

if answer == "Charles Babbage":
        print ("Correct!")
        score += 1
else:
    print ("Incorrect!") 
      
      
answer=input("Who is the father of Computer?") 

if answer == "Charles Babbage":
        print ("Correct!")
        score += 1
else:
    print ("Incorrect!") 
    
    
answer=input("Who is the father of Computer science ?") 

if answer == "Allen Turing":
        print ("Correct!")
        score += 1
else:
    print ("Incorrect!") 
    
    

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")  