#!/usr/bin/env python
list = [0,0]
while True:
   print('Left/Right/Up/Down?')
   word=input()
   print('How much?')
   value=int(input())
   if word=='Left':
      list[0]-=value
      print(list)
   elif word=="Right":
        list[0]+=value
        print(list)
   elif word=="Up":
        list[1]+=value
        print(list)
   elif word=="Down":
        list[1]-=value
        print(list)
   
   print('Stop? (Yes/No)')
   stop=input()
   if stop=='Yes':
       break
