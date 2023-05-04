






def fibonacci(n):
  '''
  this is a function to find fibonacci number of n parameter 
  param n: intger
  return: intger
  '''  
    
  if type(n) != int : 
   return 'please enter a number'
  if n == 0 or n==1 :
      return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)






def lucas(n):
   '''
   this is a function to find lucas number of n parameter 
   param n: intger
   return: intger
   '''
   if type(n) != int : 
    return 'please enter a number' 
   if n == 0:
      return 2
   elif n==1:
    return 1
   else:
    return lucas(n-1)+lucas(n-2)
      
      
      
def sum_series(n,x=0,y=1):
    """
    this function take three parameters (n,x,y) as integer and will calculate a with a same rule of fibonacci but 
    with different first two numbers  if you input n only this function will calculate a fibonacci for n parameter
    param n,x,y: intgers
    return : intger
    """
    if type(n) != int : 
      return 'please enter a number'
    if x==2 and y==1 : 
     return lucas(n)
    else: 
       
     if type(n) != int : 
      return 'please enter a number'
     if n==0 :
        return x
     elif n==1:
        return y
     else :
        return sum_series(n-1,x,y) + sum_series(n-2,x,y)