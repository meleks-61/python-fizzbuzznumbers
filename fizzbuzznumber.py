# -*- coding: utf-8 -*-
"""fizzbuzznumber

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1237YKnvUFQDT9LlN20N8Iel5XY7nXiNF
"""

for i in range(1,101):
  if (i%3==0 and i%5!=0):
    print("Fizz")
  elif (i%5==0 and i%3!=0):
    print("Buzz")
  elif (i%15==0):
    print("FizzBuzz")
  else:
   print(i)