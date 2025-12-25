from circleshape import CircleShape
from pygame import draw
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH ) # Super position might go wrong
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        print("split")
        angle = random.uniform(20, 50)

        first_vector = self.velocity.rotate(angle)
        second_vector = self.velocity.rotate(-angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        a = Asteroid(self.position.x, self.position.y, new_radius)
        b = Asteroid(self.position.x, self.position.y, new_radius)
        
        a.velocity = 1.2 * first_vector
        b.velocity = 1.2 * second_vector