from Commands.Command import Command
from Commands.CommandLand import CommandLand
from Commands.CommandPrint import CommandPrint

commands = [
    CommandLand
]
prefix_commands = {i.get_command_prefix(): i for i in commands}