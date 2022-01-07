import random
import time
from os import system, name
from random_word import RandomWords

getRandomWord = RandomWords()
hangman = (

'''
  |````|
  |   
  |  
  |   
  | 
````````````````` 
  
''',

'''   
  |````|
  |   "o"
  |  
  |   
  | 
````````````````` 
 ''',

 '''   
  |````|
  |   "o"
  |  / | \\
  |   
  | 
````````````````` 
 ''',

'''   
,,,,,,,,,,,,,,,,,,,,,,,,,,,,
|                          |
      G`a`m`e` `O`v`e`r
         |````|
         |   "o"
         |  / | \\
         |   | |
         | 
   ````````````````` 
  PRESS (n) <<<PLAY AGAIN>>>
|                            |     
`````````````````````````````

 '''
 )

def clear():  
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    print("Screen Cleared")
  
            
score=0
while True:
    clear()
    print("I am going to guessing a word....")
    guessWord = getRandomWord.get_random_word()    
    guessList = list((len(guessWord)) * "_")
    trial = 0
    gameOver = False
    died=False
    playAain = 'c'
    wordGuess = False
    print(guessWord)   

    while True :
       guesscorrect=False
       #  prints guesslist hangman and lives 
       for char in guessList :
             print(char, end=" ")
     
       print("\n\n"+hangman[trial])
       print("Lives remained: "+str(3-trial))

       # takes input from the user
       char = input("Guess a character or (/q)uit : \n")
       if(char == "/q") :
           playAain='/q'
           break


       for i in range(0, len(guessWord)) :
            if guessWord[i] == char :
               guessList[i] =char
               guesscorrect = True
    
       if guesscorrect != True :        
            trial=trial+1
      
       # guessed all letters in a word
       if guessList.count('_') == 0 :
          gameOver=True
          guessWord=True
     
       #  trail comples 
       if trial>2 :
           gameOver = True
           died = True


       time.sleep(1)
       clear()
      
       #  inner while fails
       if(gameOver == True) :
           break

   
   
    if died == True :
          print(hangman[3])
          
       
    if guessWord==True :
         print(
          '''
 
             |```````````````````````````````````|  
     
                  C`O`N`G`R`A`T`U`L`A`T`I`O`N`S  
                         >>(n)EXT>>
                           (q)UIT

             |,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,|


            '''
               )

    if playAain !='/q':
       playAain=input()
   
    if playAain!='n':
           break

  

print("Thanks for playing")
    
