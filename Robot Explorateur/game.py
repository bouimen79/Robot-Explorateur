
import pygame
import threading
import sys
import random
import time
from threading import Thread
pygame.init()
fen=pygame.display.set_mode((600,700))
fen.fill(color='black')
pygame.display.set_caption('Robot Explorateur')
mur=pygame.image.load('mur.png').convert()
robot=pygame.image.load('antt.png').convert()
food=pygame.image.load('pizza.png').convert()
fond=pygame.image.load('fond.jpg').convert()
depart=pygame.image.load('depart.png').convert()
matrice =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 10, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
          [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
matrice_trace=[]
for i in range(len(matrice)):
    a=[]
    for j in range(len(matrice)):
        a.append(0)
    matrice_trace.append(a)
class minerai_source:
    def __init__(self,x,y,source):
        self.pos_x=x
        self.pos_y=y
        self.source=source
        matrice[x][y]=5
case_vide = []
for i in range(len(matrice)):
    for j in range(len(matrice)):
        if matrice[i][j] == 0:
            case_vide.append([i, j])
list = []
list = random.sample(case_vide, 20)
print(list)
min_list = []
for i in range(len(list)):
    min_list.append(minerai_source(list[i][0], list[i][1], 5))
list_trace=[]
class Signal:
    rows = 0
    colums = 0
    M = []
    def __init__(self, Rows, Colums, matrice):
        self.rows = Rows
        self.colums = Colums
        matrix = []
        for i in range(Rows):  # A for loop for row entries
            a = []
            for j in range(Colums):  # A for loop for column entries
                if j == 0 or j + 1 == Colums:
                    a.append(500)
                elif i == 0 or i + 1 == Rows:
                    a.append(500)
                elif matrice[i][j] == 5:
                    a.append(500)
                elif matrice[i][j] == 1:
                    a.append(500)
                elif matrice[i][j] == 10:
                    a.append(0)
                else:
                    a.append(100)
            matrix.append(a)
        self.M = matrix

    def calculateSignal(self, x, y):
        if x + 1 < self.rows and y + 1 < self.colums and x - 1 > 0 and y - 1 > 0:
            if self.M[x + 1][y] == 100 or self.M[x + 1][y] > self.M[x][y] + 1:
                if self.M[x + 1][y] < 400:
                    self.M[x + 1][y] = self.M[x][y] + 1
                    self.calculateSignal(x + 1, y)
            if self.M[x][y + 1] == 100 or self.M[x][y + 1] > self.M[x][y] + 1:
                if self.M[x][y + 1] < 400:
                    self.M[x][y + 1] = self.M[x][y] + 1
                    self.calculateSignal(x, y + 1)

            if self.M[x - 1][y] == 100 or self.M[x - 1][y] > self.M[x][y] + 1:
                if self.M[x - 1][y] < 400:
                    self.M[x - 1][y] = self.M[x][y] + 1
                    self.calculateSignal(x - 1, y)

            if self.M[x][y - 1] == 100 or self.M[x][y - 1] > self.M[x][y] + 1:
                if self.M[x][y - 1] < 400:
                    self.M[x][y - 1] = self.M[x][y] + 1
                    self.calculateSignal(x, y - 1)
        else:
            pass  # print("end calculating")
    def afficherMatrix(self):
        for i in range(self.rows):
            for j in range(self.colums):
                print('%s%s' % (self.M[j][i], " " * max(4 - len(str(self.M[j][i])), 0)), end=" | ")
            print()
class agent(Thread):
    find = False
    trace_nbr=100
    def __init__(self,x,y):
        Thread.__init__(self,)
        self.posx=x
        self.posy=y
        matrice[x][y]=3
    def run(self):
        done = False
        print("run thread")
        while not done:
            time.sleep(0.3)
            if not self.find:
                self.deplace()
                if matrice_trace[self.posx][self.posy]>0:
                    self.move_to_minerai()
                self.detecter_minerai()
            else :
                self.backtoBase()
                if self.signal_m[self.posx][self.posy]==1:
                    self.find=False
                    self.trace_nbr=100

    def move_to_minerai(self):
        if matrice_trace[self.posx+1][self.posy]> matrice_trace[self.posx][self.posy] and matrice[self.posx+1][self.posy]==0:
            matrice[self.posx][self.posy]=0
            self.posx+= 1
            matrice[self.posx][self.posy] = 3
        elif matrice_trace[self.posx-1][self.posy]> matrice_trace[self.posx][self.posy] and matrice[self.posx-1][self.posy]==0:
            matrice[self.posx][self.posy]=0
            self.posx-= 1
            matrice[self.posx][self.posy] = 3
        elif  matrice_trace[self.posx][self.posy+1]> matrice_trace[self.posx][self.posy] and matrice[self.posx][self.posy+1]==0:
            matrice[self.posx][self.posy]=0
            self.posy+= 1
            matrice[self.posx][self.posy] = 3
        elif  matrice_trace[self.posx][self.posy-1]> matrice_trace[self.posx][self.posy] and matrice[self.posx][self.posy-1]==0:
            matrice[self.posx][self.posy]=0
            self.posy-= 1
            matrice[self.posx][self.posy] = 3


    def read_signal(self,m):
        self.signal_m=m


    def backtoBase(self):
        if self.signal_m[self.posx+1][self.posy]<self.signal_m[self.posx][self.posy] and matrice[self.posx+1][self.posy]==0:
            matrice[self.posx][self.posy]=0
            self.posx+= 1
            matrice[self.posx][self.posy] = 3
            #list_trace.append([self.posx,self.posy])
            matrice_trace[self.posx][self.posy]=self.trace_nbr
            self.trace_nbr-=1
            evapor.trace_ajout(self.posx,self.posy)

        elif self.signal_m[self.posx-1][self.posy]<self.signal_m[self.posx][self.posy]and matrice[self.posx-1][self.posy]==0:
            matrice[self.posx][self.posy] = 0
            self.posx-= 1
            matrice[self.posx][self.posy] = 3
            #list_trace.append([self.posx,self.posy])
            matrice_trace[self.posx][self.posy] = self.trace_nbr
            self.trace_nbr -= 1
            evapor.trace_ajout(self.posx, self.posy)

        elif self.signal_m[self.posx][self.posy+1]<self.signal_m[self.posx][self.posy]and matrice[self.posx][self.posy+1]==0:
            matrice[self.posx][self.posy] = 0
            self.posy+= 1
            matrice[self.posx][self.posy] = 3
            #list_trace.append([self.posx,self.posy])
            matrice_trace[self.posx][self.posy] = self.trace_nbr
            self.trace_nbr -= 1
            evapor.trace_ajout(self.posx, self.posy)

        elif self.signal_m[self.posx][self.posy-1]<self.signal_m[self.posx][self.posy]and matrice[self.posx][self.posy-1]==0:
            matrice[self.posx][self.posy] = 0
            self.posy -= 1
            matrice[self.posx][self.posy] = 3
            #list_trace.append([self.posx,self.posy])
            matrice_trace[self.posx][self.posy] = self.trace_nbr
            self.trace_nbr -= 1
            evapor.trace_ajout(self.posx, self.posy)



    def collecter(self,x,y):
        for i in range(len(min_list)):
            if min_list[i].pos_x==x and min_list[i].pos_y==y:
                min_list[i].source-=1
                self.find=True
                print(min_list[i].source)
                if min_list[i].source==0:
                    matrice[x][y]=0

    def detecter_minerai(self):
        if matrice[self.posx+1][self.posy]==5:
            self.collecter(self.posx+1,self.posy)
            print("detecter_detecter_minerai")
        elif matrice[self.posx - 1][self.posy] == 5:
            self.collecter(self.posx - 1, self.posy)
            print("detecter_detecter_minerai")
        elif matrice[self.posx ][self.posy+1] == 5:
            self.collecter(self.posx , self.posy+1)
            print("detecter_detecter_minerai")
        elif matrice[self.posx ][self.posy-1] == 5:
            self.collecter(self.posx , self.posy-1)
            print("detecter_detecter_minerai")

    def deplace(self):
        #list_vist=[]
        ran_direction=random.randint(0,3)
        if ran_direction==0:
            if matrice[self.posx-1][self.posy] == 0:
                matrice[self.posx][self.posy] = 0
                self.posx = self.posx - 1
                matrice[self.posx][self.posy] = 3
                #list_vist.append((self.posx,self.posy))
        elif ran_direction==1:
            if matrice[self.posx + 1][self.posy] == 0:
                matrice[self.posx][self.posy] = 0
                self.posx = self.posx + 1
                matrice[self.posx][self.posy] = 3
                #list_vist.append((self.posx, self.posy))
        elif ran_direction==2:
            if matrice[self.posx ][self.posy - 1] == 0:
                matrice[self.posx][self.posy] = 0
                self.posy = self.posy - 1
                matrice[self.posx][self.posy] = 3
                #list_vist.append((self.posx, self.posy))
        elif ran_direction==3:
            if matrice[self.posx][self.posy + 1] == 0:
                matrice[self.posx][self.posy] = 0
                self.posy = self.posy + 1
                matrice[self.posx][self.posy] = 3
                #list_vist.append((self.posx, self.posy))
        #print(list_vist)
class evaporate(Thread):
    done = False
    def __init__(self):
        Thread.__init__(self)
        self.list_temp = []
        self.list_trace1 = []
    def trace_ajout(self, posx, posy):
        self.list_trace1.append([posx, posy])
        #print("dakhl la matrice",self.list_trace1)
        #print("ana lawla",self.list_trace1[0][0])
        self.list_temp.append(time.time())

    def run(self):
        while not self.done:
            #print("run",self.list_trace1)
            time.sleep(0.01)
            if len( self.list_trace1)>0:
                i=self.list_trace1[0][0]
                j=self.list_trace1[0][1]
                #print("i j",i,j)
                if len(self.list_trace1):
                    # print(time.time() - self.list_trace_[0][0])
                    if (time.time() - self.list_temp[0] >= 15):
                        self.list_temp = self.list_temp[1:]
                        matrice_trace[i][j]=0
                        print("case jdida ta3 lmatrice",matrice_trace[i][j])
                        self.list_trace1.pop(0)
            #print(self.list_trace1)

evapor =evaporate()
evapor.start()
matrice_sign = Signal(20, 20 ,matrice)
matrice_sign.calculateSignal(3,3)
matrice_sign.afficherMatrix()
for k in range(3):
    t = agent(1, 1)
    t.read_signal(matrice_sign.M)
    t.start()
list=[]
running=True
while running:
    time.sleep(0.01)
    fen.fill((0,0,0))
    for k in range(len(matrice_trace)):
        for j in range(len(matrice_trace)):
            print(matrice_trace[k][j])
            if matrice_trace[k][j]>0:
                fen.blit(pygame.transform.scale(food, (20, 20)), (matrice_trace[k][j] * 30, matrice_trace[k][j] * 30))
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == 3:
                fen.blit(pygame.transform.scale(robot, (30, 30)), (i * 30, j * 30))
            if matrice[i][j] == 1:
                fen.blit(pygame.transform.scale(mur,(30, 30)), (i * 30, j * 30))
            if matrice[i][j] == 5:
                fen.blit(food, (i * 30, j * 30))
            if matrice[i][j]==10:
                fen.blit(pygame.transform.scale(depart,(30, 30)), (i * 30, j * 30))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

