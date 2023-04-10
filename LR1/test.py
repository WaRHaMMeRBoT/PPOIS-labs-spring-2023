A = []
for i in range(5):
    A.append([0]* 5)
for row in A: 
    for elem in row:
        elem += 1 
        print(elem, end=' ') 
    print()
    
print()
for i in range(5): 
    for j in range(5):
        print(A[i][j], end=' ')
    print()



{
    "line": "sunny",
    "numbers": [
        5,
        5,
        50,
        50
    ],
    "line_list": [
        ["corn","corn","corn","corn","corn"],
        ["corn","corn","corn","corn","corn"],
        ["corn","corn","corn","corn","corn"],
        ["corn","corn","corn","corn","corn"],
        ["corn","corn","corn","corn","corn"]
    ],
    "number_list":[
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
}