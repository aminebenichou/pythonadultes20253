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
    {'is_checked':False, 'start_coords':(0, 0), 'end_coords':(190, 190)},
    {'is_checked':False, 'start_coords':(200, 0), 'end_coords':(390, 190)},
    {'is_checked':False, 'start_coords':(400, 0), 'end_coords':(590, 190)},
    {'is_checked':False, 'start_coords':(0, 200), 'end_coords':(190, 390)},
    {'is_checked':False, 'start_coords':(200, 200), 'end_coords':(390, 390)},
    {'is_checked':False, 'start_coords':(400, 200), 'end_coords':(590, 390)},
    {'is_checked':False, 'start_coords':(0, 400), 'end_coords':(190, 600)},
    {'is_checked':False, 'start_coords':(200, 400), 'end_coords':(390, 600)},
    {'is_checked':False, 'start_coords':(400, 400), 'end_coords':(600, 600)},
]
first_checked = False
while running:
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False

        

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
                    square['is_checked']=True
                    print(squares)
            # for y in y_coords:
            #     x=0
            #     while x < 600:
            #         if x<pygame.mouse.get_pos()[0]<x+200 and y<pygame.mouse.get_pos()[1]<y+200:
            #             print("hello")
            #             # pygame.draw.line(screen, 'black', (x, y), (x+190, y+190), width=5)
            #             first_checked=True
            #         x += 200

    # if first_checked:
    #     pygame.draw.line(screen, 'black', (0, 0), (190,190), width=5)
    #     pygame.draw.line(screen, 'black', (190, 0), (0,190), width=5)
    
    for square in squares:
        if square['is_checked']:
            pygame.draw.line(screen, 'black', square['start_coords'], square['end_coords'], width=5)
            pygame.draw.line(screen, 'black', (square['end_coords'][0], square['start_coords'][1]), (square['start_coords'][0],square['end_coords'][1]), width=5)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)  

pygame.quit()