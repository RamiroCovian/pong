import pygame

ANCHO = 800
ALTO = 600


class Pong:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO, ALTO))

    def jugar(self):  # Contiene el bucle principal
        exit = False
        while not exit:
            for event in pygame.event.get():  # Lista de eventos con objeto
                if event.type == pygame.QUIT:  # QUIT es una constante de pygame
                    exit = True

            # Renderizar nuestro objeto

            # Mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    print("Has llamado a pong.py directamente desde la linea de comandos")
    print("El nombre del paquete ahora es", __name__)
    juego = Pong()
    juego.jugar()
else:
    print("Has llamado a pong.py desde la sentencia import")
    print("El nombre del paquete ahora es", __name__)
