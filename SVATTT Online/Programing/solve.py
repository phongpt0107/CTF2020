from pwn import *
con = remote("34.87.30.195", 7331)
while(True):
    x = ""
    while "x+---" not in x:
        x = con.recv()
        print(x)
    prematrix = (x.split("x+---")[1]).split("\n")
    size = len(prematrix[1]) - 2
    matrix = []
    for i in range(size):
        matrix.append(list(prematrix[i + 1])[2:])
    print(matrix)
    queue = []
    count = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != "?":
                queue.append([i, j])
    while(len(queue) != 0):
        check = queue[0]
        queue.pop(0)
        x1, y1 = check[0], check[1]
        if (x1 + 2 < size):
            if matrix[x1 + 2][y1] == "?":
                con.sendline(str(x1 + 1) + " " + str(y1+1) + " " + str(x1 + 3) + " " + str(y1 + 1))
                count += 1
                l = ""
                while True:
                    l = con.recv()
                    if "Yes" in l or "bad" in l: 
                        break 
                if "Yes" in l:
                    matrix[x1 + 2][y1] = matrix[x1][y1]
                else:
                    if matrix[x1][y1] == "b":
                        matrix[x1 + 2][y1] = "g"
                    else:
                        matrix[x1 + 2][y1] = "b"
                queue.append([x1 + 2, y1])
        if (x1 + 1 < size and y1 + 1 < size):                                        
            if matrix[x1 + 1][y1 + 1] == "?":
                con.sendline(str(x1 + 1) + " " + str(y1+1) + " " + str(x1 + 2) + " " + str(y1 + 2))
                count += 1
                l = ""
                while True:
                    l = con.recv()
                    if "Yes" in l or "bad" in l: 
                        break 
                if "Yes" in l:
                    matrix[x1 + 1][y1 + 1] = matrix[x1][y1]
                else:
                    if matrix[x1][y1] == "b":
                        matrix[x1 + 1][y1 + 1] = "g"
                    else:
                        matrix[x1 + 1][y1 + 1] = "b"
                queue.append([x1 + 1, y1 + 1])
        if (y1 + 2 < size):
            if matrix[x1][y1+2] == "?":
                con.sendline(str(x1 + 1) + " " + str(y1+1) + " " + str(x1 + 1) + " " + str(y1 + 3))
                count += 1
                l = ""
                while True:
                    l = con.recv()
                    if "Yes" in l or "bad" in l: 
                        break 
                if "Yes" in l:
                    matrix[x1][y1+2] = matrix[x1][y1]
                else:
                    if matrix[x1][y1] == "b":
                        matrix[x1][y1+2] = "g"
                    else:
                        matrix[x1][y1+2] = "b"
                queue.append([x1, y1 + 2])
    ####################################################
        if (x1 - 2 >= 0):
            if matrix[x1 - 2][y1] == "?":
                con.sendline(str(x1 - 1) + " " + str(y1+1) + " " + str(x1 + 1) + " " + str(y1 + 1))
                count += 1
                l = ""
                while True:
                    l = con.recv()
                    if "Yes" in l or "bad" in l: 
                        break 
                if "Yes" in l:
                    matrix[x1 - 2][y1] = matrix[x1][y1]
                else:
                    if matrix[x1][y1] == "b":
                        matrix[x1 - 2][y1] = "g"
                    else:
                        matrix[x1 - 2][y1] = "b"
                queue.append([x1 - 2, y1])
        if (x1 - 1 >= 0 and y1 - 1 >= 0):
            if matrix[x1 - 1][y1 - 1] == "?":
                con.sendline(str(x1 ) + " " + str(y1) + " " + str(x1+1) + " " + str(y1+1))
                count += 1
                l = ""
                while True:
                    l = con.recv()
                    if "Yes" in l or "bad" in l: 
                        break 
                if "Yes" in l:
                    matrix[x1 - 1][y1 - 1] = matrix[x1][y1]
                else:
                    if matrix[x1][y1] == "b":
                        matrix[x1 - 1][y1 - 1] = "g"
                    else:
                        matrix[x1 - 1][y1 - 1] = "b"
                queue.append([x1 - 1, y1 - 1])
        if (y1 - 2 >= 0):
            if matrix[x1][y1-2] == "?":
                con.sendline(str(x1 + 1) + " " + str(y1-1) + " " + str(x1 + 1) + " " + str(y1 + 1))
                count += 1
                l = ""
                while True:
                    l = con.recv()
                    if "Yes" in l or "bad" in l: 
                        break 
                if "Yes" in l:
                    matrix[x1][y1-2] = matrix[x1][y1]
                else:
                    if matrix[x1][y1] == "b":
                        matrix[x1][y1-2] = "g"
                    else:
                        matrix[x1][y1-2] = "b"
                queue.append([x1, y1 - 2])

    S = ""
    for i in matrix:
        for j in i:
            S += j
    print(S)
    while count < size * size:
        con.sendline("1 1 2 2")
        print(con.recv())
        count += 1
    if(count == size * size):
        print("done")
    con.sendline(S)
#You got this far! Flag is ASCIS{y0u_c4n_b3_4nyth1ng_y0u_w4nt_t0_b3}
