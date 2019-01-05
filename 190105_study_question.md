### 4-2(modify)

```python
def crossBridge(steps):
    cnt = 0
    current = 0
    n = len(steps)
    while(current<n):
        current+=steps[current]
        cnt+=1
    return cnt

print(crossBridge([1, 1, 2, 3, 5]))
```

### 4-5

```python
def star(a):
    for i in range(3):
        print("*",end="")
        print(" "*a,end="")
    print("\n",end="")
    print(" "*int(a/1.5),end="")
    for i in range(2):    
        if(a%2==0):
            print("*",end="")
            print(" "*(a-1),end="")
        else:
            print("*",end="")
            print(" "*a,end="")
            
a = int(input("두 별사이의 거리를 입력하세요 :"))
star(a)
```

