import pygame
import random
import sys
from musique_et_sons import jouer_musique, jouer_son_collision, jouer_son_score
from menu import menu
from niveau import ajuster_difficulte
from game_over import game_over

# Initialisation de Pygame:
pygame.init()

# Constantes:
LARGEUR, HAUTEUR = 1000, 600
FPS = 60
BLANC = (255, 255, 255)

# Fenêtre:
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("rimel Fuyante")
clock = pygame.time.Clock()

# Chargement des images:
image_joueur = pygame.image.load("projet pygame/joueur.jpg") 
image_obstacle = pygame.image.load("projet pygame/obstacle.jpg")  
image_fond = pygame.image.load("projet pygame/fond.jpg")  



# Ajustement des tailles des images :
image_joueur = pygame.transform.scale(image_joueur, (60, 60))  
image_obstacle = pygame.transform.scale(image_obstacle, (60, 60))  
image_fond = pygame.transform.scale(image_fond, (1000, 600))
# Joueur:
carre_x = 50
carre_y = HAUTEUR // 2 - 40 // 2
carre_vitesse = 5

# Obstacles:
obstacles = []
obstacle_vitesse = 5
obstacle_timer = 0
intervalle_obstacle = 1500  

# Score:
score = 0
font = pygame.font.SysFont(None, 36)

# Fonction pour afficher le score:
def afficher_score():
    texte = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(texte, (10, 10))

# Boucle principale:
def jouer():
    print("La fonction jouer() a été appelée")
    
    global score, carre_y, obstacles, obstacle_vitesse, obstacle_timer, intervalle_obstacle
    
    score = 0
    carre_y = HAUTEUR // 2 - 40 // 2
    obstacles = []
    obstacle_vitesse = 5

    running = True
    while running:
        dt = clock.tick(FPS)
       

        # Affiche l'image de fond:
        screen.blit(image_fond, (0, 0)) 

        # Événements:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Touches:
        touches = pygame.key.get_pressed()
        if touches[pygame.K_UP] and carre_y > 0:
            carre_y -= carre_vitesse
        if touches[pygame.K_DOWN] and carre_y < HAUTEUR - 40:
            carre_y += carre_vitesse

        # Génération d'obstacles:
        obstacle_timer += dt
        if obstacle_timer > intervalle_obstacle:
            obstacle_timer = 0
            y_pos = random.randint(0, HAUTEUR - 60)
            obstacles.append(pygame.Rect(LARGEUR, y_pos, 20, 60))

        # Mise à jour et affichage des obstacles:
        for obstacle in obstacles[:]:
            obstacle.x -= obstacle_vitesse
            screen.blit(image_obstacle, (obstacle.x, obstacle.y))  
            if obstacle.right < 0:
                obstacles.remove(obstacle)
                score += 1
                jouer_son_score()  

            # Collision:
            joueur_rect = pygame.Rect(carre_x, carre_y, 40, 40)
            if joueur_rect.colliderect(obstacle):
                jouer_son_collision()  
                print("Game Over!")
                running = False

        # Affichage du joueur:
        screen.blit(image_joueur, (carre_x, carre_y)) 

        # Affichage du score:
        afficher_score()

        # Affichage du jeu:
        pygame.display.flip()

        # Augmenter la vitesse des obstacles :
        obstacle_vitesse, intervalle_obstacle = ajuster_difficulte(score, obstacle_vitesse, intervalle_obstacle)

    game_over(screen, HAUTEUR)  

# Lancer le jeu:
def main():
    menu(screen, HAUTEUR) 
    jouer()

main()
