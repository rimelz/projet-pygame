import pygame
from musique_et_sons import jouer_musique

# Fonction pour afficher le menu:
def afficher_menu(screen, HAUTEUR):
    screen.fill((255, 255, 255))  
    menu_font = pygame.font.SysFont(None, 50)
    texte = menu_font.render("Appuyez sur une touche pour commencer", True, (0, 0, 0))
    screen.blit(texte, (100, HAUTEUR // 2 - 25))  
    pygame.display.flip()  

# Fonction pour gérer le menu de démarrage:
def menu(screen, HAUTEUR):
    afficher_menu(screen, HAUTEUR)
    jouer_musique()  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return 
