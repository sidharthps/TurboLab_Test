input_string = input("Enter values:")
input_list=list(map(int,input_string.split(',')))
for i in range(len(input_list)):
  if sum(input_list[0:i])==sum(input_list[i:]):
    print(i-1,i)
  if sum(input_list[0:i])==sum(input_list[i+1:]):
    print(i+1)