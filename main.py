import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        screen.fill((0, 0, 0))
        screen.fill(000, rect=None, special_flags=0)
        updateable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for sprite in asteroids:
            for shot in shots:
                if shot.collide(sprite):
                    shot.kill()
                    sprite.split()
            if sprite.collide(player):
                print("Game Over!")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()