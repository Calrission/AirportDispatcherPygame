import pygame.font
from pygame import Surface


class MultiLineText:
    def __init__(self, x, y, w, h, color="white", size=24, font=pygame.font.get_default_font(), text="", save_len=-1, save_index_start=None):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.size = size
        self.color = color
        self.text_lines = []
        if len(text) != 0:
            self.text_lines.append(text)
        self.font = pygame.font.Font(font, self.size)
        self.save_len = save_len
        self.save_index = save_index_start

    def change_text(self, text: str):
        if "\n" in text:
            text_lines = text.split("\n")
        else:
            text_lines = [text]
        self.text_lines = text_lines

    def add_text(self, text: str):
        self.text_lines.append(text)

    def add_all_text(self, texts: list[str]):
        for text in texts:
            self.add_text(text)

    def add_last(self, text: str):
        index_new_last = len(self.text_lines[-1])
        self.text_lines[-1] += text
        return index_new_last

    def remove_last(self):
        if len(self.text_lines[-1]) > self.save_len:
            self.text_lines[-1] = self.text_lines[-1][:-1]

    def insert_last(self, text, index):
        self.text_lines[-1] = self.text_lines[-1][:index] + text + self.text_lines[-1][index:]

    def remove_last_index(self, start, end):
        if start > self.save_index:
            self.text_lines[-1] = self.text_lines[-1].replace(self.get_from_last_index(start, end), "")

    def get_from_last_index(self, start, end):
        return self.text_lines[-1][start:end]

    def new_line(self):
        self.text_lines.append("")

    def get_last(self):
        return self.text_lines[-1]

    def refresh(self, screen: Surface):
        self.__render_multi_line(screen)

    def clear(self):
        self.text_lines = []

    def __create_text_surface(self, text: str):
        return self.font.render(text, True, self.color)

    def __render_multi_line(self, screen: Surface):
        surfaces = []
        for i in self.text_lines:
            surfaces += self.__generate_line_surfaces(i)
        for i, s in enumerate(surfaces):
            rect = s.get_rect()
            height_text, width_text = rect.height, rect.width
            screen.blit(s, (self.x, self.y + (height_text + 10) * i))

    def __generate_line_surfaces(self, line: str) -> list[Surface]:
        surfaces = []
        now_surface = None
        now_text = ""
        while len(line) != 0:
            if now_surface is None:
                now_surface = self.__create_text_surface(line[0])
                now_text = line[0]
                line = line[1:]
            else:
                sim_w = self.font.size(line[0])[0]
                if now_surface.get_rect().width + sim_w > self.w:
                    surfaces.append(now_surface)
                    now_text = ""
                    now_surface = None
                else:
                    now_text += line[0]
                    now_surface = self.__create_text_surface(now_text)
                    line = line[1:]
        if now_text != "" and now_surface is not None:
            surfaces.append(now_surface)

        return surfaces
