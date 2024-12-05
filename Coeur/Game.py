#Code Princiapale Du jeu"

import pygame
from Coeur.menu import *


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_X, self.DISPLAY_Y = 1200, 495 # Dimensions de l'écran.
        self.display = pygame.Surface((self.DISPLAY_X, self.DISPLAY_Y)) # Surface d'affichage principale.
        self.window = pygame.display.set_mode(((self.DISPLAY_X, self.DISPLAY_Y))) # Fenêtre principale.
        self.font_name = pygame.font.get_default_font()  # Police par défaut de Pygame.
        self.BLACK, self.WHITE, self.RED, self.GREEN, self.ORANGE = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (255, 165, 0) # Définition des couleurs principales.
        # Initialisation des menus.
        self.main_menu = MenuPrincipal(self)
        self.rules = MenuRegles(self)
        self.credits = CreditsMenu(self)
        self.quit = QuitterMenu(self)
        self.curr_menu = self.main_menu 

    # Boucle principale du jeu.
    def game_loop(self):
        while self.playing:
            self.check_events()
            self.display.fill(self.BLACK)
            self.draw_text('FIN DU JEU', 20, self.DISPLAY_X / 2, self.DISPLAY_Y / 2)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()

    # Gère les événements utilisateur (clavier et fermeture de la fenêtre).
    def check_events(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:  # Si l'utilisateur ferme la fenêtre.
                self.running, self.playing = False, False  # Arrête le jeu et la boucle principale.
                self.curr_menu.run_display = True  # Retourne au menu en cours.
            if event.type == pygame.KEYDOWN:  # Si une touche est pressée.
                if event.key == pygame.K_RETURN:  # Touche Entrée.
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:  # Touche Retour.
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:  # Flèche Bas.
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:  # Flèche Haut.
                    self.UP_KEY = True

    # Réinitialise les variables liées aux touches après chaque action.
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.ORANGE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y) 
        self.display.blit(text_surface, text_rect)
