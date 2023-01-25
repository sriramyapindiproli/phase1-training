import string
def validate(pas):
   val=True
   a=string.ascii_letters
   sp=['@','#','$','%']
   if len(pas)<8:
       val=False
   if len(pas)>16:
       val=False
   if not any(char.isupper() for char in pas):
       val=False
   if not any(char.islower() for char in pas):
       val=False
   if not any(char.isdigit() for char in pas):
       val=False
   if not any(char in sp for char in pas):
       val=False
   if not(pas.startswith(tuple(a))):
       val=False

n=int(input())
password=input()
for i in range(n):
    print(validate(password))

