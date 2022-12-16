'''
Basic differance between break and continue

    break -> skips the loop in general.
    continue -> skips the iteration only.

'''

for i in range(12):
  if(i == 10):
    print("Skip the iteration")
    continue
  print("5 X", i, "=", 5 * i)
  
i = 0
while True: # infinite loop
  print(i)
  i = i + 1
  if(i%10 == 0):
    break
