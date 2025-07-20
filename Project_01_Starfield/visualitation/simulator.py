import pygame
from modelFolder.starField import StarField

class StarfieldApp:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.starfield = StarField(width, height, star_count=200)
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.display.fill((0, 0, 0))
            self.starfield.update_and_draw(self.display)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


if __name__ == "__main__":
    app = StarfieldApp(800, 600)
    app.run()
