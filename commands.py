from data_structures import Commands
from mappers import mst_mapper

no_mapper = lambda response: response

commands_0520: dict[str, Commands] = {  # Commands for the Easy-Driver 0520.
    "MST": Commands(
        description = "Read module internal status register",
        is_read = True,
        is_write = False,
        response_mapper = mst_mapper,
    ),
    "reboot": Commands(
        description = (
            "Reboot module. This command is different from the other commands"
            " as the text 'reboot' is not actually sent to the PSU, but rather"
            " a sequence of 9-byte commands via UDP as defined in the"
            " 'reboot_psu' function."
        ),
        is_read = False,
        is_write = True,
        response_mapper = no_mapper,
    ),
    "MON": Commands(
        description = "Turn on output driver",
        is_read = False,
        is_write = True,
        response_mapper = no_mapper,
    ),
    "MOFF": Commands(
        description = "Turn off output driver",
        is_read = False,
        is_write = True,
        response_mapper = no_mapper,
    ),
}