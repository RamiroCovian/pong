import pygame

ANCHO = 800
ALTO = 600
COLOR_OBJETOS = (255, 255, 255)
COLOR_FONDO = (100, 100, 100)
ANCHO_PALA = 20
ALTO_PALA = 60
MARGEN_X = 10
COLOR_PELOTA = (239, 242, 29)
ANCHO_PELOTA = 50
ALTO_PELOTA = 50


class Pong:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        self.title = pygame.display.set_caption("Pong")

    def jugar(self):  # Contiene el bucle principal
        pos_alto_inicial = (ALTO / 2) - (ALTO_PALA / 2)
        centro_vectores_pelota = (ANCHO / 2, ALTO / 2)
        radio_pelota = 10
        ancho_linea_media = 5
        exit = False

        while not exit:
            for event in pygame.event.get():  # Lista de eventos con objeto
                if event.type == pygame.QUIT:  # QUIT es una constante de pygame
                    exit = True

            # Renderizar nuestro objeto
            pygame.draw.rect(self.screen, COLOR_FONDO, ((0, 0), (ANCHO, ALTO)))

            jugador1 = pygame.Rect(MARGEN_X, pos_alto_inicial, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.screen, COLOR_OBJETOS, jugador1)

            jugador2 = pygame.Rect(
                ANCHO - MARGEN_X - ANCHO_PALA, pos_alto_inicial, ANCHO_PALA, ALTO_PALA
            )
            pygame.draw.rect(self.screen, COLOR_OBJETOS, jugador2)

            # Linea media
            pygame.draw.line(
                self.screen,
                COLOR_OBJETOS,
                (ANCHO / 2, 0),
                (ANCHO / 2, ALTO),
                ancho_linea_media,
            )

            # Pelota
            pygame.draw.circle(
                self.screen, COLOR_PELOTA, centro_vectores_pelota, radio_pelota
            )

            # Marcador

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
