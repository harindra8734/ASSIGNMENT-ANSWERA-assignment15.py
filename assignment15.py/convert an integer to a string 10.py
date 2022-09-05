#rite a python script to convert an integer to a string. 
num = 10
  
# check  and print type of num variable
print("Type before convertion : ",type(num)) 
  
# convert the num into string 
converted_num = num.__str__()
  
# print type of converted_num
print("Type after convetion : ", type(converted_num))