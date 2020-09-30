import random

def choose():
  words=["rainbow","computer","science","programming", "mathematics","player","condition","reverse","water","board", "apple", "queen", "hack", "october", "fest"]
  pick=random.choice(words)
  return pick

def jumble(word):
  jumbled="".join(random.sample(word,len(word)))
  return jumbled

def thank(p1n,p2n,p1,p2):
  print(p1n," Your Score is : ",p1)
  print(p2n," Your Score is : ",p2)


def play():
  p1name=input("Player 1 , Please Enter your name : ")
  p2name=input("Player 2 , Please Enter your name : ")
  pp1=0
  pp2=0
  turn=0
  while(1):
    #computer's Task
    picked_word=choose()
    #Create the Question
    qn=jumble(picked_word)
    print (qn)
    #Player 1
    if turn%2==0:
      print(p1name, " This is your Turn ")
      ans=input("What is on my mind ? ")
      if ans==picked_word:
        pp1=pp1 + 1
        print("Your Score is : ",pp1)

      else:
        print("Better Luck next time . I thought : ",picked_word)

      c=int(input("Press 1 to Continue and 0 to Quit : "))
      if c==0:
        thank(p1name,p2name,pp1,pp2)
        break

    else:

      print(p2name, " This is your Turn ")
      ans=input("What is on my mind ? ")
      if ans==picked_word:
        pp2 = pp2 + 1
        print("Your Score is : ",pp2)

      else:
        print("Better Luck next time . I thought : ",picked_word)

      c=int(input("Press 1 to Continue and 0 to Quit : "))
      if c==0:
        thank (p1name,p2name,pp1,pp2)
        break

    turn = turn + 1
 
play()
