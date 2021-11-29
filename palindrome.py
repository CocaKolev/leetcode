def isPalindrome(x: int) -> bool:
    i:int =0
    reversedX:int=0
    y:int= 0
    
    originalNum=x
    while x!=0:
        modulusX= int(x%10) #find the remainder for the 1s place
     #   reversedX=reversedX+modulusX
        x=int(x/10)
        y= y*10+modulusX
    if (y==originalNum):
        return True
    else:
        return False

isPalindrome(-121)