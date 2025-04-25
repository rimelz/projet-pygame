import pygame

# Fonction pour jouer la musique de fond:
def jouer_musique():
    pygame.mixer.music.load("musique.mp3")  
    pygame.mixer.music.play(-1, 0.0)  

# Fonction pour jouer un son de collision:
def jouer_son_collision():
    pygame.mixer.music.stop()
    collision_sound = pygame.mixer.Sound("Game Over Sound Effects High Quality.mp3")  
    collision_sound.play()

# Fonction pour jouer un son de score:
def jouer_son_score():
    score_sound = pygame.mixer.Sound("Score - Sound Effect for editing.mp3")  
    score_sound.play()
