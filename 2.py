def is_binary(num):
    try:
        int(num, 2)
        return True
    except ValueError:
         return False
def main():
   bi = input("Enter a binary number: ")
   if is_binary(bi):
      D = 0
      for i in range(len(bi)):
          if bi[i] == '1':
             D = D + 2**(len(bi)-i-1)
      print("The decimal of the number is",D)
   else:
      print("The enterd number is invalid format,please enter a binary number")

main()

