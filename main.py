import pygame
import Menu
import shooter

def game_loop():
    Menu()
    shooter.run_game()

def main():
    game_loop()

if __name__ == "__main__":
    main()
