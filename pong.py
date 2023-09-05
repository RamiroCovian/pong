from random import randint
import pygame

ANCHO = 1080
ALTO = 720
FPS = 60

COLOR_OBJETOS = (255, 255, 255)
COLOR_FONDO = (100, 100, 100)

ANCHO_PALA = 20
ALTO_PALA = 60
VEL_JUGADOR = 10
ARRIBA = True
ABAJO = False

MARGEN_X = 10
TAM_PELOTA = 20
VEL_MAXIMA = 10
VARIACION_VEL_PELOTA = 5


class Jugador(pygame.Rect):
    def __init__(self, x, y):
        super(Jugador, self).__init__(x, y, ANCHO_PALA, ALTO_PALA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, COLOR_OBJETOS, self)

    def mover(self, direccion):
        """
        Que necesito para que un jugador se mueva:
        - Posicion: nos basta con la y ---> self.y
        - Velocidad: es una constante global ---> VEL_JUGADOR
        - Direccion: argumento del metodo ---> True: arriba, False: abajo
        """
        if direccion == ARRIBA:
            if self.y <= 0:
                self.y = 0
            else:
                self.y -= VEL_JUGADOR
        if direccion == ABAJO:
            if self.y >= (ALTO - ALTO_PALA):
                self.y = ALTO - ALTO_PALA
            else:
                self.y += VEL_JUGADOR


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

        # Sse sale por la izquierda
        if self.right <= 0:
            print("Punto para el jugador 2")
            self.center = (ANCHO / 2, ALTO / 2)
            self.velocidad_y = randint(-VEL_MAXIMA, VEL_MAXIMA)
            self.velocidad_x = randint(-VEL_MAXIMA, -1)
            return 2
        # se sale por la derecha
        if self.left >= ANCHO:
            print("Punto para el jugador 1")
            self.center = (ANCHO / 2, ALTO / 2)
            self.velocidad_y = randint(-VEL_MAXIMA, VEL_MAXIMA)
            self.velocidad_x = randint(1, VEL_MAXIMA)
            return 1
        return 0


class Pong:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO, ALTO))
        self.reloj = pygame.time.Clock()
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

            # Doy movimiento al jugadoor
            self.comprobar_teclas()

            # Bloque 2: Renderizar nuestro objeto
            # pygame.draw.rect(self.screen, COLOR_FONDO, ((0, 0), (ANCHO, ALTO)))
            self.screen.fill(COLOR_FONDO)

            self.pintar_red()
            self.jugador1.pintame(self.screen)
            self.jugador2.pintame(self.screen)

            self.pintar_pelota()
            self.pelota.comprobar_punto()

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
            self.reloj.tick(FPS)

        pygame.quit()

    def comprobar_teclas(self):
        estado_teclas = pygame.key.get_pressed()
        if estado_teclas[pygame.K_a]:
            self.jugador1.mover(True)
        if estado_teclas[pygame.K_z]:
            self.jugador1.mover(False)
        if estado_teclas[pygame.K_UP]:
            self.jugador2.mover(True)
        if estado_teclas[pygame.K_DOWN]:
            self.jugador2.mover(False)

    def pintar_pelota(self):
        self.pelota.mover()
        # Comprobamos si hay rebote en las paletas (colliderect)
        # if self.pelota.colliderect(self.jugador1) or self.pelota.colliderect(
        #     self.jugador2
        # ):
        #     self.pelota.velocidad_x = -self.pelota.velocidad_x + randint(
        #         -VARIACION_VEL_PELOTA, VARIACION_VEL_PELOTA
        #     )
        #     self.pelota.velocidad_y = randint(-VEL_MAXIMA, VEL_MAXIMA)
        #     if self.pelota.velocidad_x < -VEL_MAXIMA:
        #         self.pelota.velocidad_x = -VEL_MAXIMA
        #     if self.pelota.velocidad_x > VEL_MAXIMA:
        #         self.pelota.velocidad_x = VEL_MAXIMA

        # ALTERNATIVA
        if self.pelota.colliderect(self.jugador1):
            self.pelota.velocidad_x = randint(1, VEL_MAXIMA)
            self.pelota.velocidad_y = randint(-VEL_MAXIMA, VEL_MAXIMA)
        if self.pelota.colliderect(self.jugador2):
            self.pelota.velocidad_x = randint(-VEL_MAXIMA, -1)
            self.pelota.velocidad_y = randint(-VEL_MAXIMA, VEL_MAXIMA)

        self.pelota.pintame(self.screen)

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
