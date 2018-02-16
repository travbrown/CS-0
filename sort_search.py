def is_sorted(LOI):
  if LOI == [] or len(LOI) == 1:
    return True
    
  num = LOI[0]
  
  for a in LOI:
    if a < num:
      return False
    num = a
  
  return True
    

def find(SLOI,search_val):
  
  start = 0
  end = len(SLOI)-1
  found = False
  
  while start <= end and not found:
    
    mid = (start + end) //2
    
    if SLOI[mid] == search_val:
      found = True
    elif search_val < SLOI[mid]:
      end = mid -1
    else: 
      start = mid + 1
  
  if found == True:
    return mid
  else:
    return -1


NS = [777,2,5,3,9]
S = [1,2,3,4,5,6,7]
print(is_sorted(NS))
print(is_sorted(S))
print(is_sorted([1]))


print(find(S,2))
print(find(S,8))