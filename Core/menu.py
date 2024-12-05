import pygame
from Core.game import *

class Menu():
  def __init__(self, game):
    self.game = game
    self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
    self.run_display = True
    self.cursor_rect = pygame.Rect(0, 0, 20, 20)
    self.offset = -100
  
  def draw_cursor(self):
    self.game.draw_text('>>>', 25, self.cursor_rect.x - 20, self.cursor_rect.y - 4)

  def blit_screen(self):
    self.game.window.blit(self.game.display, (0, 0))
    pygame.display.update()
    self.game.reset_keys()

class MainMenu(Menu):
  def __init__(self, game):
    Menu.__init__(self, game)
    self.state = "START GAME"
    self.startx, self.starty = self.mid_w, self.mid_h
    self.rulesx, self.rulesy = self.mid_w, self.mid_h + 35
    self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
    self.quitx, self.quity = self.mid_w, self.mid_h + 105
    self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

  def display_menu(self):
    self.run_display = True
    while self.run_display:
      self.game.check_events()
      self.check_input()
      self.game.display.fill(self.game.BLACK)
      self.game.draw_text('Jumpel Quest', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 80)
      self.game.draw_text("JOUER", 30, self.startx, self.starty)
      self.game.draw_text("REGLE", 30, self.rulesx, self.rulesy)
      self.game.draw_text("CREDITS", 30, self.creditsx, self.creditsy)
      self.game.draw_text("QUITTER", 30, self.quitx, self.quity)
      self.draw_cursor()
      self.blit_screen()
      
  def move_cursor(self):
    if self.game.DOWN_KEY:
      if self.state == 'START GAME':
        self.cursor_rect.midtop = (self.rulesx + self.offset, self.rulesy)
        self.state = 'RULES'
      elif self.state == 'RULES':
        self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
        self.state = 'CREDITS'
      elif self.state == 'CREDITS':
        self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
        self.state = 'QUIT'
      elif self.state == 'QUIT':
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.state = 'START GAME'
    elif self.game.UP_KEY:
      if self.state == 'START GAME':
        self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
        self.state = 'QUIT'
      elif self.state == 'QUIT':
        self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
        self.state = 'CREDITS'
      elif self.state == 'CREDITS':
        self.cursor_rect.midtop = (self.rulesx + self.offset, self.rulesy)
        self.state = 'RULES'
      elif self.state == 'RULES':
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.state = 'START GAME'
  
  def check_input(self):
    self.move_cursor()
    if self.game.START_KEY:
      if self.state == 'START GAME':
        MainMenu.display_menu.run_display = True
      elif self.state == 'RULES':
        self.game.curr_menu = self.game.rules
      elif self.state == 'CREDITS':
        self.game.curr_menu = self.game.credits
      elif self.state == 'QUIT':
        self.game.curr_menu = self.game.quit
      self.run_display = False
    if self.game.BACK_KEY:
      quit()

class RulesMenu(Menu):
  def __init__(self, game):
    Menu.__init__(self, game)

  def display_menu(self):
    self.run_display = True
    while self.run_display:
      self.game.check_events()
      if self.game.START_KEY or self.game.BACK_KEY:
        self.game.curr_menu = self.game.main_menu
        self.run_display = False
      self.game.display.fill(self.game.BLACK)
      self.game.draw_text('REGLES', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 80)
      self.game.draw_text('Vous devez atteindre la fin de chaque niveau le plus rapidement posible.', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
      self.game.draw_text('Utiliser les fleches du clavier et la touche espace pour vous déplacer.', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 40)
      self.game.draw_text('Vous pouver acheter des pouvoir aupres du marchant que vous pouvez croiser', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 80)
      self.game.draw_text('Faite attention au ennemis et au pikes', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 120)
      self.blit_screen()

class CreditsMenu(Menu):
  def __init__(self, game):
    Menu.__init__(self, game)

  def display_menu(self):
    self.run_display = True
    while self.run_display:
      self.game.check_events()
      if self.game.START_KEY or self.game.BACK_KEY:
        self.game.curr_menu = self.game.main_menu
        self.run_display = False
      self.game.display.fill(self.game.BLACK)
      self.game.draw_text('CREDITS', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 80)
      self.game.draw_text('Fait par Yassine Aouane', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
      self.blit_screen()

class QuitMenu(Menu): 
  def __init__(self, game):
    Menu.__init__(self, game)
    self.state = 'OUI'
    self.yesx, self.yesy = self.mid_w, self.mid_h
    self.nox, self.noy = self.mid_w, self.mid_h + 35
    self.cursor_rect.midtop = (self.yesx + self.offset, self.yesy)

  def display_menu(self):
    self.run_display = True
    while self.run_display:
      self.game.check_events()
      self.check_input()
      self.game.display.fill((0, 0, 0))
      self.game.draw_text('ETES VOUS SUR DE VOULOIR QUITTER?', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 80)
      self.game.draw_text('OUI', 30, self.yesx, self.yesy)
      self.game.draw_text('NON', 30, self.nox, self.noy)
      self.draw_cursor()
      self.blit_screen()
      
  def check_input(self):
    if self.game.BACK_KEY:
      self.game.curr_menu = self.game.main_menu
      self.run_display = False
    elif self.game.UP_KEY or self.game.DOWN_KEY:
      if self.state == 'OUI':
        self.state = 'NON'
        self.cursor_rect.midtop = (self.nox + self.offset, self.noy)
      elif self.state == 'NON':
        self.state = 'OUI'
        self.cursor_rect.midtop = (self.yesx + self.offset, self.yesy)
    elif self.game.START_KEY:
      if self.state == 'OUI':
        quit()
      if self.state == 'NON':
        self.game.curr_menu = self.game.main_menu
        self.run_display = False
