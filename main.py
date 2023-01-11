w=[]
b=[]

def draw():
    print("\n\n\n\n\n\n\n\n\n")
    print(" 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4")
    for i in range(15):
        print(i%10,end="")
        for j in range(15):
            if [i,j] in w:
                print("\033[37;41m[]\033[0m",end="")
            elif [i,j] in b:
                print("\033[37;44m[]\033[0m",end="")
            else:
                print("\033[0m[]\033[0m",end="")
        print("")

def move1():
    while True:
        x,y=(input("index? ").split())
        x=int(x)
        y=int(y)
        if not (x in range(15) and y in range(15) and not [x,y] in w and not [x,y] in b):
            print("Hey,",end="")
        else:
            b.append([x,y])
            break

def move2():
    score=[0]*1415
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[-1,0,1,-1,1,-1,0,1]
    addsc=[0,20,50,70,100]
    for i in range(15):
        for j in range(15):
            for f in range(8):
                if (i+dx[f]*4) in range(15) and (j+dy[f]*4) in range(15) and [i+dx[f]*0,j+dy[f]*0] in w and [i+dx[f]*1,j+dy[f]*1] in w and [i+dx[f]*2,j+dy[f]*2] in w and [i+dx[f]*3,j+dy[f]*3] in w and not([i+dx[f]*4,j+dy[f]*4] in w and [i+dx[f]*4,j+dy[f]*4] in b):
                    score[(i+dx[f]*4)*100+(j+dy[f]*4)]+=addsc[4]
                elif (i+dx[f]*3) in range(15) and (j+dy[f]*3) in range(15) and [i+dx[f]*0,j+dy[f]*0] in w and [i+dx[f]*1,j+dy[f]*1] in w and [i+dx[f]*2,j+dy[f]*2] in w and not([i+dx[f]*3,j+dy[f]*3] in w and [i+dx[f]*3,j+dy[f]*3] in b):
                    score[(i+dx[f]*3)*100+(j+dy[f]*3)]+=addsc[3]
                elif (i+dx[f]*2) in range(15) and (j+dy[f]*2) in range(15) and [i+dx[f]*0,j+dy[f]*0] in w and [i+dx[f]*1,j+dy[f]*1] in w and not([i+dx[f]*2,j+dy[f]*2] in w and [i+dx[f]*2,j+dy[f]*2] in b):
                    score[(i+dx[f]*2)*100+(j+dy[f]*2)]+=addsc[2]
                elif (i+dx[f]*1) in range(15) and (j+dy[f]*1) in range(15) and [i+dx[f]*0,j+dy[f]*0] in w and not([i+dx[f]*1,j+dy[f]*1] in w and [i+dx[f]*1,j+dy[f]*1] in b):
                    score[(i+dx[f]*1)*100+(j+dy[f]*1)]+=addsc[1]
                elif (i+dx[f]*0) in range(15) and (j+dy[f]*0) in range(15) and not([i+dx[f]*0,j+dy[f]*0] in w and [i+dx[f]*0,j+dy[f]*0] in b):
                    score[(i+dx[f]*0)*100+(j+dy[f]*0)]+=addsc[0]
                if (i+dx[f]*4) in range(15) and (j+dy[f]*4) in range(15) and [i+dx[f]*0,j+dy[f]*0] in b and [i+dx[f]*1,j+dy[f]*1] in b and [i+dx[f]*2,j+dy[f]*2] in b and [i+dx[f]*3,j+dy[f]*3] in b and not([i+dx[f]*4,j+dy[f]*4] in b and [i+dx[f]*4,j+dy[f]*4] in b):
                    score[(i+dx[f]*4)*100+(j+dy[f]*4)]+=addsc[4]
                elif (i+dx[f]*3) in range(15) and (j+dy[f]*3) in range(15) and [i+dx[f]*0,j+dy[f]*0] in b and [i+dx[f]*1,j+dy[f]*1] in b and [i+dx[f]*2,j+dy[f]*2] in b and not([i+dx[f]*3,j+dy[f]*3] in b and [i+dx[f]*3,j+dy[f]*3] in b):
                    score[(i+dx[f]*3)*100+(j+dy[f]*3)]+=addsc[3]
                elif (i+dx[f]*2) in range(15) and (j+dy[f]*2) in range(15) and [i+dx[f]*0,j+dy[f]*0] in b and [i+dx[f]*1,j+dy[f]*1] in b and not([i+dx[f]*2,j+dy[f]*2] in b and [i+dx[f]*2,j+dy[f]*2] in b):
                    score[(i+dx[f]*2)*100+(j+dy[f]*2)]+=addsc[2]
                elif (i+dx[f]*1) in range(15) and (j+dy[f]*1) in range(15) and [i+dx[f]*0,j+dy[f]*0] in b and not([i+dx[f]*1,j+dy[f]*1] in b and [i+dx[f]*1,j+dy[f]*1] in b):
                    score[(i+dx[f]*1)*100+(j+dy[f]*1)]+=addsc[1]
                elif (i+dx[f]*0) in range(15) and (j+dy[f]*0) in range(15) and not([i+dx[f]*0,j+dy[f]*0] in b and [i+dx[f]*0,j+dy[f]*0] in b):
                    score[(i+dx[f]*0)*100+(j+dy[f]*0)]+=addsc[0]
    mx=-99999
    rx=0
    ry=0
    for i in range(1415):
        if mx<score[i] and not [i//100,i%100] in w and not [i//100,i%100] in b:
            mx=score[i]
            rx=i//100
            ry=i%100
    w.append([rx,ry])

def judge():
    for i in range(15):
        for j in range(15):
            if [i,j] in w and [i+1,j] in w and [i+2,j] in w and [i+3,j] in w and [i+4,j] in w:
                print("AI wins...")
                return True
            if [i,j] in w and [i,j+1] in w and [i,j+2] in w and [i,j+3] in w and [i,j+4] in w:
                print("AI wins...")
                return True
            if [i,j] in w and [i-1,j+1] in w and [i-2,j+2] in w and [i-3,j+3] in w and [i-4,j+4] in w:
                print("AI wins...")
                return True
            if [i,j] in w and [i+1,j+1] in w and [i+2,j+2] in w and [i+3,j+3] in w and [i+4,j+4] in w:
                print("AI wins...")
                return True
            if [i,j] in b and [i+1,j] in b and [i+2,j] in b and [i+3,j] in b and [i+4,j] in b:
                print("You win!1")
                return True
            if [i,j] in b and [i,j+1] in b and [i,j+2] in b and [i,j+3] in b and [i,j+4] in b:
                print("You win!2")
                return True
            if [i,j] in b and [i-1,j+1] in b and [i-2,j+2] in b and [i-3,j+3] in b and [i-4,j+4] in b:
                print("You win!3")
                return True
            if [i,j] in b and [i+1,j+1] in b and [i+2,j+2] in b and [i+3,j+3] in b and [i+4,j+4] in b:
                print("You win!4")
                return True
    return False

print("Gobang!")
print("\033[34mYou play blue chess...\033[0m")
input("Let's go? ")
draw()
while not judge():
    move1()
    move2()
    draw()
