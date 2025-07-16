import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

square_size = 190
squarex, squarey = 0, 0


y_coords = [
    0,
    200,
    400
]
squares=[
    {'x_checked':False, 'o_checked':False, 'start_coords':(0, 0), 'end_coords':(190, 190)},
    {'x_checked':False, 'o_checked':False, 'start_coords':(200, 0), 'end_coords':(390, 190)},
    {'x_checked':False, 'o_checked':False, 'start_coords':(400, 0), 'end_coords':(590, 190)},
    {'x_checked':False, 'o_checked':False, 'start_coords':(0, 200), 'end_coords':(190, 390)},
    {'x_checked':False, 'o_checked':False, 'start_coords':(200, 200), 'end_coords':(390, 390)},
    {'x_checked':False, 'o_checked':False, 'start_coords':(400, 200), 'end_coords':(590, 390)},
    {'x_checked':False, 'o_checked':False, 'start_coords':(0, 400), 'end_coords':(190, 590)},
    {'x_checked':False, 'o_checked':False, 'start_coords':(200, 400), 'end_coords':(390, 590)},
    {'x_checked':False, 'o_checked':False, 'start_coords':(400, 400), 'end_coords':(590, 590)},
]
first_checked = False
winning_combos=[
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6],
]
def draw_x(square):
    pygame.draw.line(screen, 'black', square['start_coords'], square['end_coords'], width=5)
    pygame.draw.line(screen, 'black', (square['end_coords'][0], square['start_coords'][1]), (square['start_coords'][0],square['end_coords'][1]), width=5)

def draw_o(square):
    pygame.draw.circle(screen, 'black', (square['start_coords'][0]+square_size/2, square['start_coords'][1]+square_size/2), 50)
    pygame.draw.circle(screen, 'white', (square['start_coords'][0]+square_size/2, square['start_coords'][1]+square_size/2), 40)

def get_winner():
    for combo in winning_combos:
        if all(squares[i]['x_checked'] for i in combo):
            return True
        elif all(squares[i]['o_checked'] for i in combo):
            return True


turn=0

while running:
 
    screen.fill("black")
    for y in y_coords:
        x=0
        while x<600:
            pygame.draw.rect(screen, "white", (x, y, 
                                       square_size, square_size))
            x += 200
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for square in squares:
                if square['start_coords'][0]<pygame.mouse.get_pos()[0]<square['end_coords'][0] and square['start_coords'][1]<pygame.mouse.get_pos()[1]<square['end_coords'][1]:
                    if turn%2==0:
                        square['x_checked']=True
                    else:
                        square['o_checked']=True
                    print(squares)
                    turn += 1
            
    for square in squares:
        if square['x_checked']:
            draw_x(square)
        elif square['o_checked']:
            draw_o(square)
    if get_winner():
        print("You Won")
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)  
    
pygame.quit()