#the function
def swap():
 #opening the files in read mode
  #opening file with text 'PES'   
   with open('PES.txt', 'r') as a:
      #saving the text in var. 
       data_a=a.read()
      #making sure data is saved in var. 
       print(data_a)
  #opening file with text 'FIFA'
   with open('FIFA.txt', 'r') as b:
      #saving the text in var. 
       data_b=b.read()
      #making sure data is saved in var.  
       print(data_b)

 #swapping data in files by opening in read mode
  #opening PES file in write mode   
   with open('PES.txt', 'w') as a:
      #writing data from FIFA file in PES file 
       a.write(data_b)
  #opening FIFA file in write mode
   with open('FIFA.txt', 'w') as b:
      #writing data from PES file to FIFA file 
       b.write(data_a)                    

#calling function
swap()