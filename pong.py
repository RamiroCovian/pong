import pygame

ANCHO = 800
ALTO = 600
COLOR_OBJETOS = (255, 255, 255)
COLOR_FONDO = (100, 100, 100)
ANCHO_PALA = 20
ALTO_PALA = 60
MARGEN_X = 10
TAM_PELOTA = 20


class Jugador:
    def __init__(self, x, y):
        self.rectangulo = pygame.Rect(x, y, ANCHO_PALA, ALTO_PALA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, COLOR_OBJETOS, self.rectangulo)


class Pelota:
    def __init__(self):
        # Definicion del rectangulo
        self.rectangulo = pygame.Rect(
            (
                ((ANCHO - TAM_PELOTA) / 2),
                ((ALTO - TAM_PELOTA) / 2),
                TAM_PELOTA,
                TAM_PELOTA,
            )
        )

    def pintame(self, pantalla):
        # Pintar el rectangulo
        pygame.draw.rect(pantalla, COLOR_OBJETOS, self.rectangulo)


class Pong:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        self.title = pygame.display.set_caption("Pong")
        self.icon_imagen = pygame.image.load("icono.png")
        self.logo = pygame.display.set_icon(self.icon_imagen)
        pos_y = (ALTO - ALTO_PALA) / 2
        self.pelota = Pelota()
        self.jugador1 = Jugador(MARGEN_X, pos_y)
        self.jugador2 = Jugador(ANCHO - MARGEN_X - ANCHO_PALA, pos_y)

    def jugar(self):  # Contiene el bucle principal
        punto_jugador1 = 0
        punto_jugador2 = 0
        fuente_marcador = pygame.font.SysFont("Arial", 40)
        exit = False

        while not exit:
            for event in pygame.event.get():  # Lista de eventos con objeto
                if event.type == pygame.QUIT:  # QUIT es una constante de pygame
                    exit = True

            # Renderizar nuestro objeto
            pygame.draw.rect(self.screen, COLOR_FONDO, ((0, 0), (ANCHO, ALTO)))

            self.pintar_red()
            self.jugador1.pintame(self.screen)
            self.jugador2.pintame(self.screen)
            self.pelota.pintame(self.screen)

            # Marcador
            texto_marcador1 = fuente_marcador.render(
                "Jugador 1: " + str(punto_jugador1), 0, COLOR_OBJETOS
            )
            texto_marcador2 = fuente_marcador.render(
                "Jugador 2: " + str(punto_jugador2), 0, COLOR_OBJETOS
            )
            self.screen.blit(texto_marcador1, (20, 20))
            self.screen.blit(texto_marcador2, (((ANCHO / 2) + 20), 20))

            # Mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()

    def pintar_red(self):
        tramo_pintado = 40
        tramo_vacio = 10
        ancho_linea_media = 5
        posicion_x = ANCHO / 2
        # Linea media
        for y in range(0, ALTO, tramo_pintado + tramo_vacio):
            pygame.draw.line(
                self.screen,
                COLOR_OBJETOS,
                (posicion_x, y),
                (posicion_x, y + tramo_pintado),
                ancho_linea_media,
            )


if __name__ == "__main__":
    print("Has llamado a pong.py directamente desde la linea de comandos")
    print("El nombre del paquete ahora es", __name__)
    juego = Pong()
    juego.jugar()
else:
    print("Has llamado a pong.py desde la sentencia import")
    print("El nombre del paquete ahora es", __name__)
