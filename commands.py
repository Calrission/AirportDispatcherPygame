from Commands.CommandClear import CommandClear
from Commands.CommandTakeOff import CommandTakeOff
from Commands.CommandLand import CommandLand

commands = [
    CommandLand, CommandTakeOff, CommandClear
]
prefix_commands = {i.get_command_prefix(): i for i in commands}