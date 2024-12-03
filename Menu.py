"Code du Menu Principal du jeu"

import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_x, self.mid_y = self.game.DISPLAY_X / 2, self.game.DISPLAY_Y / 2  # Calcul des positions centrales de l'écran.
        self.run_display = True
        self.curseur_rect = pygame.Rect(0, 0, 20, 20)  # Rectangle pour représenter le curseur.
        self.offset = -100  # Décalage horizontal pour positionner le curseur.

    # Dessine le curseur sous la forme de '>>>'.
    def draw_curseur(self):
        self.game.draw_text('>>>', 25, self.curseur_rect.x - 20, self.curseur_rect.y - 4)

    # Met à jour l'affichage en copiant l'écran de jeu dans la fenêtre.
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0)) 
        pygame.display.update()  # Met à jour l'affichage de la fenêtre.
        self.game.reset_keys()  # Réinitialise les touches appuyées.

# Classe pour le menu principal.
class MenuPrincipal(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)  # Appelle du constructeur.
        self.state = "Commencer Jeu"  # État actuel du menu.
        # Coordonnées pour chaque option du menu.
        self.startx, self.starty = self.mid_x, self.x
        self.rulesx, self.rulesy = self.mid_x, self.x + 35
        self.creditsx, self.creditsy = self.mid_x, self.x + 70
        self.quitx, self.quity = self.mid_x, self.x + 105
        # Position initiale du curseur.
        self.curseur_rect.midtop = (self.startx + self.offset, self.starty)

    # Affiche le menu principal.
    def afficher_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()  # Vérifie les événements du joueur.
            self.check_input()  # Gère les entrées utilisateur.
            self.game.display.fill(self.game.BLACK)  # Remplit l'écran de noir.
            # Texte du titre et des options.
            self.game.draw_text('JUMPEL QUEST', 50, self.game.DISPLAY_X / 2, self.game.DISPLAY_Y / 2 - 80)
            self.game.draw_text("Commencer Jeu", 30, self.startx, self.starty)
            self.game.draw_text("REGLES", 30, self.rulesx, self.rulesy)
            self.game.draw_text("CREDITS", 30, self.creditsx, self.creditsy)
            self.game.draw_text("Quitter", 30, self.quitx, self.quity)
            self.draw_curseur()  # Dessine le curseur.
            self.blit_screen()  # Met à jour l'écran.

    # Déplace le curseur entre les options du menu.
    def deplacer_curseur(self):
        if self.game.DOWN_KEY:  # Si la touche "Bas" est pressée.
            # Change l'état et positionne le curseur pour chaque option.
            if self.state == 'Commencer Jeu':
                self.curseur_rect.midtop = (self.rulesx + self.offset, self.rulesy)
                self.state = 'REGLES'
            elif self.state == 'REGLES':
                self.curseur_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'CREDITS'
            elif self.state == 'CREDITS':
                self.curseur_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quitter'
            elif self.state == 'Quitter':
                self.curseur_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Commencer Jeu'
        elif self.game.UP_KEY:  # Si la touche "Haut" est pressée.
            # Change l'état dans l'ordre inverse.
            if self.state == 'Commencer Jeu':
                self.curseur_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = 'Quitter'
            elif self.state == 'Quitter':
                self.curseur_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'CREDITS'
            elif self.state == 'CREDITS':
                self.curseur_rect.midtop = (self.rulesx + self.offset, self.rulesy)
                self.state = 'REGLES'
            elif self.state == 'REGLES':
                self.curseur_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Commencer Jeu'

    # Vérifie les entrées utilisateur et agit en conséquence.
    def check_input(self):
        self.move_cursor()  # Gère le déplacement du curseur.
        if self.game.START_KEY:  # Si la touche "START" est pressée.
            if self.state == 'Commencer Jeu':
                MainMenu.display_menu.run_display = False
            elif self.state == 'REGLES':
                self.game.curr_menu = self.game.REGLES
            elif self.state == 'CREDITS':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Quitter':
                self.game.curr_menu = self.game.Quitter
            self.run_display = False
        if self.game.BACK_KEY:  # Si la touche "BACK" est pressée.
            quit()  # Quitte le jeu.

# Classe pour le menu des règles.
class MenuRegles(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    # Affiche les règles du jeu.
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('REGLES', 50, self.game.DISPLAY_W / 2, self.game.Y / 2 - 80)
            self.game.draw_text('Vous devez atteindre la fin de chaque niveau pour finir le jeu', 30, self.game.DISPLAY_W / 2, self.game.Y / 2)
            self.game.draw_text('Uttiliser les flèche directionelle et la touche espace pour vous déplacer.', 30, self.game.DISPLAY_W / 2, self.game.Y / 2 + 40)
            self.blit_screen()


# Classe pour afficher les crédits du jeu.
class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)  # Appelle le constructeur de la classe parente.

    # Affiche le menu des crédits.
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()  # Vérifie les événements utilisateur.
            # Si la touche "START" ou "BACK" est pressée, retourne au menu principal.
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            # Remplit l'écran de noir et affiche les crédits.
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('CREDITS', 50, self.game.DISPLAY_W / 2, self.game.Y / 2 - 80)
            self.game.draw_text('Fait par Yassine Aouane', 30, self.game.DISPLAY_W / 2, self.game.Y / 2)
            self.blit_screen()  # Met à jour l'affichage.

# Classe pour gérer le menu de confirmation de sortie.
class QuitMenu(Menu): 
    def __init__(self, game):
        Menu.__init__(self, game)  # Appelle le constructeur de la classe parente.
        self.state = 'YES'  # État initial du menu ("YES" sélectionné).
        # Coordonnées des options "YES" et "NO".
        self.yesx, self.yesy = self.mid_w, self.x
        self.nox, self.noy = self.mid_w, self.x + 35
        # Position initiale du curseur.
        self.curseur_rect.midtop = (self.yesx + self.offset, self.yesy)

    # Affiche le menu de confirmation.
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()  # Vérifie les événements utilisateur.
            self.check_input()  # Gère les entrées utilisateur.
            self.game.display.fill((0, 0, 0))  # Remplit l'écran de noir.
            # Affiche le message de confirmation et les options.
            self.game.draw_text('ETES VOUS SUR DE VOULOIR?', 50, self.game.DISPLAY_W / 2, self.game.Y / 2 - 80)
            self.game.draw_text('YES', 30, self.yesx, self.yesy)
            self.game.draw_text('NO', 30, self.nox, self.noy)
            self.draw_curseur()  # Dessine le curseur.
            self.blit_screen()  # Met à jour l'écran.

    # Gère les entrées utilisateur dans le menu de confirmation.
    def check_input(self):
        # Si la touche "BACK" est pressée, retourne au menu principal.
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        # Si une touche "UP" ou "DOWN" est pressée, alterne entre "YES" et "NO".
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'YES':
                self.state = 'NO'
                self.curseur_rect.midtop = (self.nox + self.offset, self.noy)
            elif self.state == 'NO':
                self.state = 'YES'
                self.curseur_rect.midtop = (self.yesx + self.offset, self.yesy)
        # Si la touche "START" est pressée.
        elif self.game.START_KEY:
            if self.state == 'YES':  # Quitte le jeu si "YES" est sélectionné.
                Quitter()
            if self.state == 'NO':  # Retourne au menu principal si "NO" est sélectionné.
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

