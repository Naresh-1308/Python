num = int(input("enter the value of num: "))
factorial = 1

if num<0:
  print("factorial does not exist")
elif num==0:
  print("factorial  of 0 is 1")
else:
  for i in range(1,num+1):
    factorial = factorial*i
    print(factorial)
    
    Link to Google Colab
    
    https://colab.research.google.com/drive/1EiN8JNdpmtU5-rd34-PhPBK-7rE4-2wS#scrollTo=GXOX1UGGbRHd
