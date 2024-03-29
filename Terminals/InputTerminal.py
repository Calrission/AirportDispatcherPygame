import pygame.event
from pygame import Surface

from SoundController import SoundController
from Terminals.ScrollMultiLineText import ScrollMultiLineText


class InputTerminal:
    def __init__(self, x, y, w, h, sound: SoundController):
        self.text_view = ScrollMultiLineText(x, y, w, h, color="green", size=20, text="> ", font='Fonts/clacon2.ttf', save_len=2, save_index_start=1)
        self.active_input = True
        self.sound = sound
        self.rect = pygame.Rect((x, y, w, h))

        self.cursor_sim = "|"
        self.show_cursor = True
        self._cursor_index_text = None
        self.__now_showing_cursor = False
        self.__duration_animation_cursor = 15
        self.__lost_frame_count_duration_animation = self.__duration_animation_cursor

    def clear(self):
        self.text_view.change_text("")

    def refresh(self, screen: Surface):
        self.text_view.refresh(screen)

    def tick(self):
        if self.__lost_frame_count_duration_animation == 0:
            self.__lost_frame_count_duration_animation = self.__duration_animation_cursor
            self.refresh_cursor()
        else:
            self.__lost_frame_count_duration_animation -= 1

    def refresh_cursor(self):
        if not self.__now_showing_cursor:
            self._cursor_index_text = self.text_view.add_last(self.cursor_sim)
            self.__now_showing_cursor = True
        elif self.__now_showing_cursor:
            self.text_view.remove_last_index(self._cursor_index_text, self._cursor_index_text + 1)
            self.__now_showing_cursor = False

    def parse_event(self, event):
        if event.type == pygame.KEYDOWN and self.active_input:
            if event.key == pygame.K_RETURN:
                if self.__now_showing_cursor:
                    self.text_view.remove_last_index(self._cursor_index_text, self._cursor_index_text + 1)
                if len(self.text_view.text_lines) != 0:
                    user_line = self.text_view.get_last()[2:]
                    self._enter_user_line(user_line)
                self.text_view.new_line()
                self.text_view.add_last("> ")
                self.sound.play('Music/Button.wav')
            elif event.key == pygame.K_BACKSPACE:
                if (not self.__now_showing_cursor and len(self.text_view.get_last()) != 2) or \
                        (self.__now_showing_cursor and len(self.text_view.get_last()) != 3):
                    self.text_view.remove_last_index(self._cursor_index_text, self._cursor_index_text + 1)
                    self.text_view.remove_last()
                self.refresh_cursor()
                self.sound.play('Music/Button.wav')
            else:
                sim = event.unicode
                if sim != '':
                    self.sound.play('Music/Button.wav')
                    if len(self.text_view.text_lines) == 0:
                        self.text_view.add_text(sim)
                    else:
                        self.text_view.add_last(sim)
                        self.refresh_cursor()

    def _enter_user_line(self, text: str):
        pass
