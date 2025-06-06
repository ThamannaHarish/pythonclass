#arithmetic operators

a=int(input("Enter the first operand:"))
b=int(input("Enter the second operand:"))

add = a + b
print("Addition:",a,"+",b,"=",add) 

sub = a - b
print("Subtraction:",a,"-",b,"=",sub)  

mul = a * b
print("Multiplication:",a,"*",b,"=",mul) 

div = a / b
print("Division:",a,"/",b,"=",div) 

floor_div = a // b
print("Floor Division:",a,"//",b,"=",floor_div)  #(removes decimal part)

mod = a % b
print("Modulus:",a,"%",b,"=",mod) #(remainder)

exp = a ** b
print("Exponentiation:",a,"**",b,"=",exp)
