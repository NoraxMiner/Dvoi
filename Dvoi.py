input_data = open('input.txt', 'r') 
data= input_data.read() 
#-------------------------------------------------------------------------
n = int(data[0])
d = bin(n)

#-------------------------------------------------------------------------
output_data = open('output.txt', 'w') 
output_data.write(str(d)) 

input_data.close() 
output_data.close()