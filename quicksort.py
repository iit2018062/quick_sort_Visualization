# Python implementation for visualizing merge sort. 
import pygame 
import random 
pygame.font.init() 
# Total window 
screen = pygame.display.set_mode((900, 650)) 
pygame.display.set_caption("SORTING VISUALISER")

# Generate new Array 
def generate_arr(arr_clr,clr):
    #intializing the array with size of array as 20
    array =[0]*20
    for i in range(1, 20):
        #filling color of each of box that represents each element of the array
        arr_clr[i]= clr[2]
        #filing the value in each index of the array
        array[i]= random.randrange(1, 100)
    return array


def refill(arr_clr,clr,array): 
	screen.fill((255, 255, 255)) 
	draw(arr_clr,clr,array) 
	pygame.display.update() 
	pygame.time.delay(20) 

# Sorting Algo:Merge sort 
def quicksort(array, l, r,arr_clr,clr): 
    if l<r: 
        pi = partition(array, l, r,arr_clr,clr) 
        quicksort(array, l, pi-1,arr_clr,clr) 
        refill(arr_clr,clr,array) 
        for i in range(0, pi + 1): 
            arr_clr[i]= clr[3] 
        quicksort(array, pi + 1, r,arr_clr,clr) 
          
# Function to partition the array 
def partition(array, low, high,arr_clr,clr): 
    pygame.event.pump()  
    pivot = array[high] 
    arr_clr[high]= clr[2] 
    i = low-1
    for j in range(low, high): 
        arr_clr[j]= clr[1] 
        refill(arr_clr,clr,array) 
        arr_clr[high]= clr[2] 
        arr_clr[j]= clr[0] 
        arr_clr[i]= clr[0] 
        if array[j]<pivot: 
            i = i + 1
            arr_clr[i]= clr[1] 
            array[i], array[j]= array[j], array[i] 
    refill(arr_clr,clr,array) 
    arr_clr[i]= clr[0] 
    arr_clr[high]= clr[0] 
    array[i + 1], array[high] = array[high], array[i + 1]  
      
    return ( i + 1 ) 
# Draw the array values 
def draw(arr_clr,clr,array):
    width = 900
	# Text should be rendered 
    fnt = pygame.font.SysFont("comicsans", 30) 
    fnt1 = pygame.font.SysFont("comicsans", 20)
    txt = fnt.render("PRESS"
	" 'ENTER' TO PERFORM SORTING.", 1, (0, 0, 0))
    # Position where text is placed
    screen.blit(txt, (20, 20))
    txt1 = fnt.render("PRESS 'R' FOR NEW ARRAY.", 
					1, (0, 0, 0))
    screen.blit(txt1, (20, 40))
    txt2 = fnt1.render("ALGORITHM USED: "
					"QUICK SORT", 1, (0, 0, 0))
    screen.blit(txt2, (600, 60))
    #width of the bars that represent elements
    WidthBar =(width-150)//40
    ##this helps in making gaps between those vertical bars in screen smaller it is smaller the gap will be
    gapbetweenbars = 900 / 20
    ##this makes the height of the bars in the screen
    barheight = 550 / 100
    pygame.draw.line(screen, (0, 0, 0), 
					(0, 95), (900, 95), 6)
    #this for loop is only for making stripped page as seen the screen if u remove it there will be a white background
    for i in range(1, 100):
        pygame.draw.line(screen, 
						(224, 224, 224), 
						(0, barheight * i + 100), 
						(900, barheight * i + 100), 1)
    # Drawing the array values as lines
    #pygame.draw.line(sceen,color,(start of the bars from left,starting edge of bar from top margine),(,gaps),element with means width of each bars
    for i in range(1, 20):
        pygame.draw.line(screen, arr_clr[i],
			(gapbetweenbars * i-3, 100),
			(gapbetweenbars * i-3, array[i]*barheight + 100),
			WidthBar)

# Infinite loop to keep the window open 

def main():
    # Window size
    run = True
    array =[0]*20
    
    #color for each of the array index
    ArrayColor =[(0, 204, 102)]*20
    color =[(0, 204, 102), (255, 0, 0), 
    (0, 0, 153), (255, 102, 0)] 
    
    array=generate_arr(ArrayColor,color) 
    while run:
        # background 
        screen.fill((255, 255, 255))
        # Event handler stores all event 
        for e in pygame.event.get(): 
            # If we click Close button in window 
            if e.type == pygame.QUIT: 
                run = False
            if e.type == pygame.KEYDOWN: 
                if e.key == pygame.K_r:
                    array=generate_arr(ArrayColor,color) 
                if e.key == pygame.K_RETURN: 
                    quicksort(array, 1, len(array)-1,ArrayColor,color)	 
        draw(ArrayColor,color,array) 
        pygame.display.update() 
    pygame.quit() 
if __name__=="__main__":
    main()
