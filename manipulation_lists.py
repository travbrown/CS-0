
def sum_of_list_of_lists(LOL):
  sumLOL = 0
  for x in LOL:
    
    for y in x:
      sumLOL += y
   
  return sumLOL

def average_of_list_of_lists(LOL):
  sumLOL = 0
  count = 0
  
  for x in LOL:
    
    for y in x:
      sumLOL += y
      count += 1
  if count == 0:
    return 0
  else:
    return sumLOL/count

def weighted_sum_of_list_of_lists(nums, weights):
  Wsum,z = 0,0
  for x in nums:
    
    for y in x:
      Wsum += y * weights[z]
      z+= 1
      
  if z == 0:
    return 0
  return Wsum
 


LOL = [[1, 2, 3], [1], [1, 2]]
num = [[2], [8, 6]]
weights = [1, 1, 10]
print(sum_of_list_of_lists(LOL))
print(average_of_list_of_lists(LOL))
print(weighted_sum_of_list_of_lists(num, weights))