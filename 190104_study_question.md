### 3-3(2)

```python
for i in range(1,6):
    for j in range(1,i+1):
        print(" ",end=" ")
    for j in range(1,7-i):
        print("*",end=" ")
    print("")
```

### 3-4(2)

```python
for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print("")

```

### 3-5(2)

```python
for i in range(1,6):
    for j in range(6,1,-1):
        if(i<j):
            print("",end=" ")
        else:
            print("*",end=" ")
    print("")

```

### 3-6(2)

```python
for i in range(6,1,-1):
    for j in range(6,1,-1):
        if(i<j):
            print("",end=" ")
        else:
            print("*",end=" ")
    print("")

```

### 3-7(2)

```python
for i in range(1,6):
    for j in range(6,1,-1):
        if(i<j):
            print("",end=" ")
        else:
            print("*",end=" ")
    print("")
    
for i in range(6,1,-1):
    for j in range(6,1,-1):
        if(i<j):
            print("",end=" ")
        else:
            print("*",end=" ")
    print("")
```



### 4-1

```python
a = list(input("문자를 입력해주세요 : "))

for i in range(len(a)):
    if(a[i] != " "):
        a[i] = '개굴'
    else:
        a[i] = " "

word=""
word=word.join(a)
print(word)
```

### 4-2

```python
def crossBridge(steps):
    cnt =0
    current=0
    for i in range(len(steps)-1):
        current += steps[i]
        cnt+=1
    return cnt

print(crossBridge([1,2,3,4,5,6,7]))
```



### 4-3

```python
def isPrince(list):
    for i in list:
        if(i[0] =="F"):
            return i
        
isPrince(['Alice', 'Bob', 'Frog'])
```

### 4-4

```python
def rest_time(a,b):
    i=1
    while i<= b:
        if(a%i==0 and b%i==0):
            time=i
        i+=1
    return int(a*b/time)
print(rest_time(3,5))
```

