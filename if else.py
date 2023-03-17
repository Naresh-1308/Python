x = input("enter the class of the student: ")
y = int(input("enter the attendance of the student: "))
c = int(input("enter 1 if there is any medical : "))
if y>=75:
  print("student is allowed")
elif y<75:
  if c==1:
    print("student is allowed")
else:
  print("student is not allowed")
    


Link to the Google Colab Notebook - 

https://colab.research.google.com/drive/1rkGx1VJAe3GFin_sDis7h6X-5tayCI21#scrollTo=GFSgSd2WOYoC
