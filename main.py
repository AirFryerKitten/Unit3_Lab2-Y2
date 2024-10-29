#Jonas York
#U3 L2
#n factorial

def for_factorial(num):
  n = 1
  for i in range(1, num+1):
    n *= i
  return n
    
  return n
def while_factorial(num):
  n = 1
  while num != 0:
    n *= num 
    num -= 1 
  return n


def recursion_factorial(num):
  if num == 1:
    return num
  else:
    return recursion_factorial(num-1)* num

def main():
  num = 1000
  for_answer=for_factorial(num)
  print(for_answer)
  while_answer=while_factorial(num)
  print(while_answer) 
  recursion_answer=recursion_factorial(num)
  print(recursion_answer)
if __name__ == "__main__":
  main()

