def ajuster_difficulte(score, obstacle_vitesse, intervalle_obstacle):
    if score % 5 == 0 and score != 0:
        obstacle_vitesse += 1
        intervalle_obstacle = max(500, intervalle_obstacle - 100)
    return obstacle_vitesse, intervalle_obstacle
