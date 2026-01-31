import pygame
import math

# -------------------- INITIAL SETUP --------------------

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
GREY = (80, 78, 81)
ORANGE = (255, 165, 0)

# Physics constants
AU = 149.6e6 * 1000       # Astronomical Unit in meters
G = 6.67428e-11           # Gravitational constant
SCALE = 250 / AU          # 1 AU = 250 pixels
TIMESTEP = 3600 * 24      # 1 day per frame


# -------------------- PLANET CLASS --------------------

class Planet:
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * SCALE + WIDTH / 2
        y = self.y * SCALE + HEIGHT / 2

        # Draw orbit path
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                px = point[0] * SCALE + WIDTH / 2
                py = point[1] * SCALE + HEIGHT / 2
                updated_points.append((px, py))

            pygame.draw.lines(win, self.color, False, updated_points, 1)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

    def attraction(self, other):
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        total_fx = 0
        total_fy = 0

        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        # F = m * a  ->  a = F / m
        self.x_vel += total_fx / self.mass * TIMESTEP
        self.y_vel += total_fy / self.mass * TIMESTEP

        self.x += self.x_vel * TIMESTEP
        self.y += self.y_vel * TIMESTEP

        self.orbit.append((self.x, self.y))


# -------------------- MAIN LOOP --------------------

def main():
    run = True
    clock = pygame.time.Clock()

    # Sun
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    # Mercury
    mercury = Planet(0.387 * AU, 0, 8, GREY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000

    # Venus
    venus = Planet(0.723 * AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    # Earth
    earth = Planet(-1 * AU, 0, 16, BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000

    # Mars
    mars = Planet(-1.524 * AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000

    planets = [sun, mercury, venus, earth, mars]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()


main()
