import pygame
import shooter

def draw_text(self, text, size, x, y ):
    font = pygame.font.Font(self.font_name,size)
    text_surface = font.render(text, True, self.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    self.display.blit(text_surface,text_rect)

class Menu():
    def __init__(self, shooter):
        self.shooter = shooter
        self.width, self.height = shooter.WIDTH / 2, shooter.HEIGHT / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        shooter.display.blit(shooter.screen, (0, 0))
        pygame.display.update()
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

class MainMenu():
    def __init__(self):
        Menu.__init__(self, shooter)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
            
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            shooter.display.fill(shooter.BLACK)
            draw_text('Main Menu', 20, shooter.WIDTH / 2, shooter.HEIGHT / 2 - 20)
            draw_text("Start Game", 20, self.startx, self.starty)
            draw_text("Options", 20, self.optionsx, self.optionsy)
            draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'