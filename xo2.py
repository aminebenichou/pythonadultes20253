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
        if event.type == pygame.MOUSEBUTTONDOWN:
            for y in y_coords:
                x=0
                while x < 600:
                    if x<pygame.mouse.get_pos()[0]<x+200 and y<pygame.mouse.get_pos()[1]<y+200:
                        print("hello")
                        # pygame.draw.line(screen, 'black', (x, y), (x+190, y+190), width=5)
                        first_checked=True
                    x += 200

    if first_checked:
        pygame.draw.line(screen, 'black', (0, 0), (190,190), width=5)
        pygame.draw.line(screen, 'black', (190, 0), (0,190), width=5)

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)  

pygame.quit()