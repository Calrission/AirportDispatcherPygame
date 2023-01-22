from Commands.Command import *
from Commands.CommandHelp import CommandHelp
from Commands.CommandPrint import CommandPrint

screen_width = 1280
screen_height = 720
screen_center = (screen_width // 2, screen_height // 2)


fps = 30

minute_length = 30
hour_length = 18

commands = [
    Command, CommandPrint, CommandHelp
]
prefix_commands = {i.get_command_prefix(): i for i in commands}
