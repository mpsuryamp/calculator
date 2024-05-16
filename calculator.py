def sum(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def multi(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def calc():
   a=int(input("Enter the number:"))
   b=int(input("enter another number:"))
   print("n1=add/n2=sub/n3=multipy/n4=divi")
   c=int(input("Enter any operator:"))
   if c==1:
     sum(a,b)
   elif c==2:
      sub(a,b)
   elif c==3:
      div(a,b)
   elif c==4:
      multi(a,b)
calc()         
