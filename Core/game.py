import pygame
from Core.menu import *

class Game():
  def __init__(self):
    pygame.init()
    self.running, self.playing = True, False
    self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
    self.DISPLAY_W, self.DISPLAY_H = 1200, 495
    self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
    self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
    self.font_name = pygame.font.get_default_font()
    self.BLACK, self.WHITE, self.RED, self.GREEN, self.ORANGE = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (255, 165, 0)
    self.main_menu = MainMenu(self)
    self.rules = RulesMenu(self)
    self.credits = CreditsMenu(self)
    self.quit = QuitMenu(self)
    self.curr_menu = self.main_menu

  def game_loop(self):
    while self.playing:
      self.check_events()
      self.display.fill(self.BLACK)
      self.draw_text('Merci pour avoir jouer', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
      self.window.blit(self.display, (0, 0))
      pygame.display.update()
      self.reset_keys()

  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running, self.playing = False, False
        self.curr_menu.run_display = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          self.START_KEY = True
        if event.key == pygame.K_BACKSPACE:
          self.BACK_KEY = True
        if event.key == pygame.K_DOWN:
          self.DOWN_KEY = True
        if event.key == pygame.K_UP:
          self.UP_KEY = True

  def reset_keys(self):
    self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

  def draw_text(self, text, size, x, y):
    font = pygame.font.Font(self.font_name, size)
    text_surface = font.render(text, True, self.ORANGE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    self.display.blit(text_surface, text_rect)