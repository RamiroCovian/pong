import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

exit = False
while not exit:
    # bucle principal

    for event in pygame.event.get():  # Lista de eventos con objeto
        print("Se ha producido un evento de tipo", event.type)
        if event.type == pygame.QUIT:  # QUIT es una constante de pygame
            print("Se ha cerrado la ventana")
            exit = True

    # Renderizar nuestro objeto
    rectangulo = pygame.Rect(50, 100, 300, 150)
    pygame.draw.rect(screen, (255, 255, 255), rectangulo)
    # Mostrar los cambios en la pantalla
    pygame.display.flip()

pygame.quit()
