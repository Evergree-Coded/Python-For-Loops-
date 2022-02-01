## For Loops 
Repeats a set of statements a specific number of times 

### Formula 
```python 
for LCV in Sequence: 
  Body 
```

### Loop Control Variable (LCV)
An ordinary integer variable that is initialized, tested, and changed as the loop executes 

### Sequence 
An iteration statement 
- range (#) 
- list, tuple, or dictionary 

*Ex.* 
```python

for x in range(3): 
  print(x)

x = 0 
while(x < 3): 
  print(x)
  x += 1
```
> 0 
> 1
> 2 

### range () function 
Generates a list of integers 
- 1 argument; range(stop)
- 2 arguments; range(start, stop)
- 3 arguments; range(start, stop, step)

*Ex.* 
```python 
range(4)  # 0, 1, 2, 3, 
range(3,8) # 3, 4, 5, 6, 7 
range(1, 13, 3) # 1, 4, 7, 10
``` 


