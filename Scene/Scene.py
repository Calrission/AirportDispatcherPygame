import pygame
from const import screen_width, screen_height
class Scene:
    def __init__(self, screen: pygame.Surface):
        self.sc = screen
        # self.back = pygame.image.load('Scene/_0007_Background.png').convert_alpha()
        # self.back = pygame.transform.scale(self.back, (screen_width, screen_height))
        #
        # self.runWay = pygame.image.load('Scene/_0006_Runway.png').convert_alpha()
        # self.runWay = pygame.transform.scale(self.runWay, (screen_width // 1.5, screen_height // 2.5))
        #
        # self.frame = pygame.image.load('Scene/_0005_Frame.png').convert_alpha()
        # self.frame = pygame.transform.scale(self.frame, (screen_width, screen_height * 0.71))
        #
        # self.backText = pygame.image.load('Scene/_0003_BackgroundText.png').convert_alpha()
        # self.backText = pygame.transform.scale(self.backText, (screen_width, screen_height * 0.3))
        #
        # self.text = pygame.image.load('Scene/_0002_Text.png').convert_alpha()
        # self.text = pygame.transform.scale(self.text, (screen_width, screen_height * 0.3))
        #
        # self.TVFrame = pygame.image.load('Scene/_0001_TVFrame.png').convert_alpha()
        # self.TVFrame = pygame.transform.scale(self.TVFrame, (screen_width, screen_height * 0.85))
        #
        # self.TV = pygame.image.load('Scene/_0000_TV.png').convert_alpha()
        # self.TV = pygame.transform.scale(self.TV, (screen_width, screen_height * 0.85))
        #
        # self.clock = pygame.image.load('Scene/Clock.png').convert_alpha()
        # self.clock = pygame.transform.scale(self.clock,
        #             (self.clock.get_width() // 1.8,self.clock.get_height() // 1.8))
        #
        #
        # self.scene = pygame.Surface(self.sc.get_size())
        # self.scene.blit(self.back, (0, 0))
        # self.scene.blit(self.runWay, (150, screen_height * 0.27))
        # self.scene.blit(self.frame, (0, 0))
        # self.scene.blit(self.backText, self.backText.get_rect(bottomright=(screen_width, screen_height)))
        # self.scene.blit(self.text, self.backText.get_rect(bottomright=(screen_width, screen_height)))
        # self.scene.blit(self.TVFrame, self.backText.get_rect(topright=(screen_width, 50)))
        # self.scene.blit(self.TV, self.backText.get_rect(topright=(screen_width - 25, 55)))
        # self.scene.blit(self.clock, self.clock.get_rect(topright=(screen_width, 30)))
        self.scene = pygame.Surface(self.sc.get_size())
        self.image = pygame.image.load('Scene/scene.png')
        self.image = pygame.transform.scale(self.image, (self.sc.get_size()))
        self.scene.blit(self.image, (0, 0))
    def ref(self):
        self.sc.blit(self.scene, (0, 0))


