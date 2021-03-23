def triangle(size): 
    m = (2 * size) - 2
    for i in range(0, size):
        for j in range(0, m): #front spaces
            print(end=" ")
        m = m - 1  # decrementing m after each loop
        for j in range(0, i + 1):
            print(chr(64 + size - j), end=' ') 
        print(" ")

n = 7
triangle(n) 