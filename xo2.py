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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0<pygame.mouse.get_pos()[0]<200 and 0<pygame.mouse.get_pos()[1]<200:
                print("x")
    screen.fill("black")
    for y in y_coords:
        x=0
        while x<600:
            pygame.draw.rect(screen, "white", (x, y, 
                                       square_size, square_size))
            x += 200
    

    pygame.display.flip()

    clock.tick(60)  

pygame.quit()