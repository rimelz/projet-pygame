import pygame
from menu import menu

# Fonction pour afficher le message de Game Over:
def afficher_game_over(screen, HAUTEUR):
    font = pygame.font.SysFont(None, 50)
    texte = font.render("Game Over! Appuyez sur une touche pour recommencer", True, (255, 0, 0))
    screen.blit(texte, (50, HAUTEUR // 2 - 25))
    pygame.display.flip()

# Fonction pour gérer la fin du jeu et le redémarrage:
def game_over(screen, HAUTEUR):
    afficher_game_over(screen, HAUTEUR)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return
