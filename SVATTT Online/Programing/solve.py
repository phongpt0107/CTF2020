from pwn import *
con = remote("34.87.30.195", 7331)
count = 0
matrix = []
queue = []
size = 0
def find(x1, y1, x2, y2):
    if x2 >= size or x2 < 0 or y2 >= size or y2 < 0:             #check available
        return False
    if matrix[x2][y2] != "?":                                    #checked?
        return False
    if x1 <= x2 and y1 <= y2:
        con.sendline(str(x1 + 1) + " " + str(y1+1) + " " + str(x2 + 1) + " " + str(y2 + 1))
    if x1 >= x2 and y1 >= y2:
        con.sendline(str(x2 + 1) + " " + str(y2+1) + " " + str(x1 + 1) + " " + str(y1 + 1))
    count += 1
    while True:
        recv = con.recv()
        if "bad" in recv or "Yes" in recv:
            break
    if "Yes" in recv:                      #symetric -> begin == end
        matrix[x2][y2] = matrix[x1][y1]
    else:                                  #not symetric -> begin != end
        if matrix[x1][y1] == "b":
            matrix[x2][y2] = "g"
        else:
            matrix[x2][y2] = "b"
    queue.append([x2, y2])                 #push node to end of queue
    return True
#################################################
while(True):                 #loop all question
    x = ""
    while "x+---" not in x:
        x = con.recv()
        print(x)
    prematrix = (x.split("x+---")[1]).split("\n")
    size = len(prematrix[1]) - 2
    matrix = []
    queue = []
    count = 0
    for i in range(size):
        matrix.append(list(prematrix[i + 1])[2:])
    print(matrix)                           #get garden in a two-dimension array
    
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != "?":
                queue.append([i, j])
    while(len(queue) != 0):                    #loop util all box is checked
        check = queue[0]
        queue.pop(0)
        x1, y1 = check[0], check[1]
################################################
        find(x1, y1, x1 + 2, y1)
        find(x1, y1, x1 + 1, y1 + 1)
        find(x1, y1, x1, y1 + 2)
################################################        
        find(x1, y1, x1 - 2, y1)
        find(x1, y1, x1 - 1, y1 - 1)
        find(x1, y1, x1, y1 - 2)
################################################        
    result = ""
    for i in matrix:
        for j in i:
            result += j
#    print(result)
    while count < size * size:
        con.sendline("1 1 2 2")
        print(con.recv())
        count += 1
    if(count == size * size):
        print("done")
    con.sendline(result)
#You got this far! Flag is ASCIS{y0u_c4n_b3_4nyth1ng_y0u_w4nt_t0_b3}
