msg="Next,let's create a Redux store to hold our application's state.In the src directory, create a new file called store.js.Inside this file, import the configureStore function from @reduxjs/tooklit and your todoSlice reducer. Then, use configureStore to create the Redux store."
ms="HI"
print(msg[::-1])
count =0
ww=0
for i in msg:
       
    if (i.upper() in "AEIOU"):
        count +=1
 
    elif(i.isalpha()):
        ww += 1
        
print(i)
print(count)
print(ww)
A=msg.split( )
print("total",len(A))
