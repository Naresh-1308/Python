num = int(input("enter the value of n: "))
r=1
i=1

if num<0:
  print("factorial does not exist")
elif num==0:
  print("factorial  of 0 is 1")
else:
  while(i<=num):
    r = r*i
    i=i+1
    print(r)
  
  Link to Google Colab
  
  https://colab.research.google.com/drive/1EiN8JNdpmtU5-rd34-PhPBK-7rE4-2wS#scrollTo=TKTI1lwZQjOr
