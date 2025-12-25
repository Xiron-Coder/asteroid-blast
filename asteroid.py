from circleshape import CircleShape
from pygame import draw
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH ) # Super position might go wrong
    
    def update(self, dt):
        self.position += self.velocity * dt
