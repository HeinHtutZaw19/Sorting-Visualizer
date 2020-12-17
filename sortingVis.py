import pygame
from numpy import random


BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,153)
GREY = (128,128,128)
GREEN = (0, 204, 102)
RED = (255,0,0)

class Visualizer:
    
    def __init__(self):
        pygame.init()
        print
        print("                               SORTING ALGORITHMS                              ")
        print("I for insertion sort, B for bubble sort, S for selection sort, M for merge sort")
        print
        self.__DISPLAY_X = 1000
        self.__DISPLAY_Y = 450+100
        self.__num = 0
        self.__height = []
        self.win = pygame.display.set_mode((self.__DISPLAY_X, self.__DISPLAY_Y))
        pygame.display.set_caption("SORTING ALGORITHMS")
        self.delay = 0
        self.setNewRandomArray(10)
        self.__width = (self.__DISPLAY_X-self.__num)/self.__num                     
        self.arr_clr =[BLACK]*self.__num
    
    def main_loop(self):
        run = True
        menu = ' '
        
        try:
            while run:
                pygame.time.delay(10) 
                keys = pygame.key.get_pressed()
                for event in pygame.event.get(): 
                    if event.type == pygame.QUIT: 
                        run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            self.selectionSort(self.__height)
                        if event.key == pygame.K_ESCAPE:
                            return 
                            pygame.quit()
                        if event.key == pygame.K_TAB:
                            for i in range(len(self.__height)):
                                self.arr_clr[i] = BLACK
                                self.__height = [random.randint(1,self.__DISPLAY_Y-100) for c in range(self.__num)]
                        if event.key == pygame.K_m:
                            self.mergeSort(self.__height,0,len(self.__height)-1)
                        if event.key == pygame.K_b:
                            self.bubbleSort(self.__height)
                        if event.key == pygame.K_i:
                            self.insertionSort(self.__height)
                        if event.key == pygame.K_q:
                            self.quickSort(self.__height,0,len(self.__height)-1)
                
                self.draw(self.__height,menu)
            pygame.quit()
        except KeyboardInterrupt:
            print
            print('Shutting down due to invalid key press')
        else:
            print ('No exception occurred')

        
    def setDelay(self,t):
        self.delay = t

    def quickSort(self,arr,l,r):
        if l<r:
            pivot = arr[r]
            p = self.partitionFunc(arr,l,r)
            self.quickSort(arr,l,p-1)
            self.quickSort(arr,p+1,r)
        else:
            return
    
    def partitionFunc(self,arr,left,right):
        pivot = arr[left]
        self.arr_clr[left]=BLUE
        low = left+1
        high = right
        self.draw(arr,'Qucik Sort')
        while True:
            while low<=high and arr[high] >= pivot:
                self.arr_clr[high]=RED
                self.arr_clr[low]=GREY
                self.draw(arr,'Qucik Sort')
                self.arr_clr[high]=BLACK
                self.arr_clr[high]=BLACK
                self.draw(arr,'Qucik Sort')
                high = high - 1
                
            while low<=high and arr[low] <= pivot:
                self.arr_clr[low]=GREY
                self.arr_clr[high]=RED
                self.draw(arr,'Qucik Sort')
                self.arr_clr[low]=BLACK
                self.arr_clr[high]=BLACK
                self.draw(arr,'Qucik Sort')
                low = low + 1


            if low<=high:
                self.arr_clr[low]=GREY
                self.arr_clr[high]=RED
                self.draw(arr,'Qucik Sort')
                arr[low],arr[high] = arr[high],arr[low]
                self.arr_clr[low]=GREEN
                self.arr_clr[high]=GREEN
                self.draw(arr,'Qucik Sort')
        
            else:
                self.arr_clr[left]=GREEN
                self.arr_clr[high]=GREEN
                
                self.arr_clr[low-1]=GREEN
                self.draw(arr,'Qucik Sort')
                break

        arr[left],arr[high] = arr[high],arr[left] 
        self.arr_clr[left]=GREEN
        self.arr_clr[high]=GREEN
        try:
            self.arr_clr[low]=GREEN
        except IndexError:
            self.arr_clr[low-1]=GREEN
                
        self.draw(arr,'Qucik Sort')
        return high        

    def selectionSort(self,arr):
        n = len(arr)
        for i in range(0,n):
            minIndex = i
            for j in range(i,n):
                if arr[j] < arr[minIndex]:
                    minIndex = j
                self.arr_clr[j] = BLUE

                self.draw(arr,'Selection Sort')
                if(j == minIndex):
                    self.arr_clr[j] = RED
                    for r in range(i,j):
                        self.arr_clr[r] = BLUE
            
            for d in range(i,n):
                self.arr_clr[d] = BLACK
        
            temp = arr[minIndex]
            arr[minIndex] = arr[i]
            arr[i] = temp
            self.arr_clr[i] = GREEN
        self.arr_clr[i-1] = GREEN

    def mergeSort(self,arr, l, r): 
        mid =(l + r)//2
        if l<r: 
            self.mergeSort(arr, l, mid) 
            self.mergeSort(arr, mid + 1, r) 
            self.merge(arr, l, mid, mid + 1, r) 

    def merge(self,arr, x1, y1, x2, y2): 
        i = x1 
        j = x2 
        temp =[] 
        while i<= y1 and j<= y2:
            self.arr_clr[i]= RED 
            self.arr_clr[j]= GREY
            self.draw(arr,'MergeSort') 
            self.arr_clr[i]= BLACK 
            self.arr_clr[j]= BLACK 
            if arr[i]<arr[j]: 
                temp.append(arr[i]) 
                i+= 1
            else: 
                temp.append(arr[j]) 
                j+= 1
        
        while i<= y1:
            self.arr_clr[i]= RED 
            self.draw(arr,'MergeSort') 
            self.arr_clr[i]= BLACK 
            temp.append(arr[i]) 
            i+= 1
        while j<= y2: 
            self.arr_clr[j]= GREY 
            self.draw(arr,'MergeSort') 
            self.arr_clr[j]= BLACK 
            temp.append(arr[j]) 
            j+= 1
        j=0
        for i in range(x1, y2 + 1):  
            arr[i]= temp[j] 
            j+= 1
            self.arr_clr[i]= BLUE
            self.draw(arr,'MergeSort')
            if y2-x1 == len(arr)-2: 
                self.arr_clr[i]= BLACK 
            else:  
                self.arr_clr[i]= GREEN 
    

    def bubbleSort(self,arr):
        n = len(arr) 
        for i in range(n): 
            for j in range(0, n-i-1): 
                if arr[j] > arr[j+1] : 
                    arr[j], arr[j+1] = arr[j+1], arr[j] 
                    for r in range(j+1):
                        self.arr_clr[r] = BLACK
                    self.arr_clr[j+1] = RED
                    self.draw(arr,'Bubble Sort')
                 
            for c in range(len(arr)-1):
                self.arr_clr[c] = BLACK
            for c in range(j,len(arr)-1):
                self.arr_clr[c+1] = GREEN
        self.arr_clr[0] = GREEN
    
    def insertionSort(self,arr):
        i = 1
        while i < len(arr):
            j = i
            while(j>0 and arr[j-1]>arr[j]):
                self.arr_clr[j] = GREEN
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                j=j-1
                for c in range(j+1):
                    if c==j:
                        self.arr_clr[c] = RED
                    else:
                        self.arr_clr[c] = GREEN
                self.draw(arr,'Insertion Sort')
            i += 1
        for i in range(len(arr)-1):
            self.arr_clr[i]  = GREEN

        
    def printList(self,arr): 
        for i in range(len(arr)):         
            print(arr[i]),
        print
            
    def addText(self,text):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(text, True, BLACK , WHITE)
        textRect = text.get_rect()  
        textRect.center = (self.__DISPLAY_X // 2, 50)
        self.win.blit(text,textRect)

    def draw(self,h,text):
        self.win.fill(WHITE)
        self.show(h)
        self.addText(text)
        pygame.time.delay(self.delay)
        pygame.display.update()

    def show(self,arr): 
        for i in range(0,len(arr)):
            pygame.draw.rect(self.win, self.arr_clr[i], ((self.__width+1)*i ,self.__DISPLAY_Y-arr[i], self.__width, arr[i]))

    def setNewArray(self,arr):
        self.__height = arr
        self.__num = len(arr)
        self.__width = (self.__DISPLAY_X-self.__num)/self.__num                     
        self.arr_clr =[BLACK]*self.__num

    def setNewRandomArray(self,n):
        self.__num = n
        self.__height = [random.randint(1,self.__DISPLAY_Y-100) for c in range(self.__num)]
        self.__width = (self.__DISPLAY_X-self.__num)/self.__num                     
        self.arr_clr =[BLACK]*self.__num


o1 = Visualizer()
#o1.setNewArray(arr)
o1.setNewRandomArray(100)
o1.main_loop()