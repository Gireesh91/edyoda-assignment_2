str1 = input("Please Enter Your String : ")

  
for i in str1:
    if(i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '&'
       or i == '*' ):
        print("string is not accepted")
        break
else:
    print("string is accepted")
  


