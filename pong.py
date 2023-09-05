from random import randint
import pygame

ANCHO = 1080
ALTO = 820
COLOR_OBJETOS = (255, 255, 255)
COLOR_FONDO = (100, 100, 100)
ANCHO_PALA = 20
ALTO_PALA = 60
MARGEN_X = 10
TAM_PELOTA = 20
VEL_MAXIMA = 1


class Jugador(pygame.Rect):
    def __init__(self, x, y):
        super(Pelota, self).__init__(x, y, ANCHO_PALA, ALTO_PALA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, COLOR_OBJETOS, self)


class Pelota(pygame.Rect):
    def __init__(self):
        super(Pelota, self).__init__(
            (
                ((ANCHO - TAM_PELOTA) / 2),
                ((ALTO - TAM_PELOTA) / 2),
                TAM_PELOTA,
                TAM_PELOTA,
            )
        )
        # Definicion del rectangulo
        self.velocidad_y = randint(-VEL_MAXIMA, VEL_MAXIMA)

        # validas = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        # self.velocidad_x = validas[randint(0, len(validas)-1)]

        self.velocidad_x = 0
        while self.velocidad_x == 0:
            self.velocidad_x = randint(-VEL_MAXIMA, VEL_MAXIMA)

    def pintame(self, pantalla):
        # Pintar el rectangulo
        pygame.draw.rect(pantalla, COLOR_OBJETOS, self)

    def mover(self):
        # Direccion: incrementeo x, incremento y --> velocidad_x , velocidad_y
        # Posicion actual (x, y)
        self.x = self.x + self.velocidad_x
        self.y = self.y + self.velocidad_y

    def rebotar(self):
        if self.y <= 0:
            self.y = 0
            self.velocidad_y = -self.velocidad_y

        if self.y >= ALTO - TAM_PELOTA:
            self.y = ALTO - TAM_PELOTA
            self.velocidad_y = -self.velocidad_y

    def comprobar_punto(self):
        # comprobar si la pelota ha salido por uno de los extremos laterales
        # si ha salido:
        #    - sie es por la derecha, (suma punto para jugador 1) --- devolver 1
        #    - si esd por la izquierda, (suma punto para jugador 2) --- devolver  0
        #    - volver a situar la pelota en el centro
        #    - lanzarla hacia el perdedor
        # si no ha salido:
        #    - devolver '

        pass


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

        # Bloque 1: Captura de eventos
        while not exit:
            for event in pygame.event.get():  # Lista de eventos con objeto
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE
                ):  # QUIT es una constante de pygame
                    exit = True

            # Bloque 2: Renderizar nuestro objeto
            pygame.draw.rect(self.screen, COLOR_FONDO, ((0, 0), (ANCHO, ALTO)))

            self.pintar_red()
            self.jugador1.pintame(self.screen)
            self.jugador2.pintame(self.screen)
            self.pelota.mover()
            self.pelota.rebotar()
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

            # Bloque 3: Mostrar los cambios en la pantalla
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
