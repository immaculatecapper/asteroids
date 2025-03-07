import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatables, drawables)
Asteroid.containers = (asteroids, updatables, drawables)
AsteroidField.containers = updatables
Shot.containers = (updatables, drawables, shots)

player1 = Player(x, y)
asteroidfield1 = AsteroidField()

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        
        for obj in drawables:
            obj.draw(screen)
        
        updatables.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides(player1):
                print("GAME over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()


        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()