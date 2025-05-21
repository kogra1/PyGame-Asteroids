import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            newVect1 = self.velocity.rotate(angle)
            newVect2 = self.velocity.rotate(-angle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            newAster1 = Asteroid(self.position.x, self.position.y, newRadius)
            newAster2 = Asteroid(self.position, self.position.y, newRadius)
            newAster1.velocity = newVect1 * 1.2
            newAster2.velocity = newVect2 * 1.2