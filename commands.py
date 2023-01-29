from Commands.CommandTakeOff import CommandTakeOff
from Commands.CommandLand import CommandLand

commands = [
    CommandLand, CommandTakeOff
]
prefix_commands = {i.get_command_prefix(): i for i in commands}