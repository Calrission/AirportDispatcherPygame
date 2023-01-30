from Screens.Menu import Menu
import pygame
from const import screen_width, screen_height
from SoundController import SoundController


class AboutAs(Menu):
    def __init__(self, x: int, y: int, padding: int, surface: pygame.Surface, background: str, sound_Controller: SoundController):
        super().__init__(x, y, padding, surface, background, sound_Controller)
        texts = {
            'text_school': 'Проект "Диспетчер аэропорта" создан для Академии Яндекса',
            'text_autor': 'Авторы: Артемий Струков, Золотарёв Данил',
            'text_programmer': 'Разработчики: Артемий Струков, Золотарёв Данил',
            'text_design': 'Дизайн: Золотарёв Данил',
            'text_supervisor': 'Руководитель: Симонов Сергей Иванович',
            'text_phone': 'Телефон: 8(968)434-95-65',
            'test_email': 'e-mail: zolotarev_d_e@mail.ru',
        }

        self.rects = {}
        self.font1 = pygame.font.Font('Fonts/AmaticSC-Bold.ttf', 50)
        self.padding1 = 75

        for key, item in texts.items():
            self.rects[key] = self.font1.render(item, True, (0, 0, 0))





    def draw(self):
        super().draw()
        i = 0
        for key, item in self.rects.items():
            rect = item.get_rect()
            rect.center = (screen_width // 2 + 100, 50 + i * self.padding1)
            self.surface.blit(item, rect)
            i += 1

