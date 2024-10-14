input_data = open('input.txt', 'r') 
data= input_data.read() 
#-------------------------------------------------------------------------
n = bin(int(data))
m =  n.count('1')
#-------------------------------------------------------------------------
output_data = open('output.txt', 'w') 
output_data.write(str(m)) 

input_data.close() 
output_data.close()