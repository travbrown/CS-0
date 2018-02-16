def bubble_sort(l):
  
  count = len(l)
  
  for x in range(count-1,-1,-1):
    
    for i in  range(x):
      
      if l[i] > l[i+1]:
        
        hold = l[i]
        l[i] = l[i+1]
        l[i+1] = hold
    
    count -= 1
