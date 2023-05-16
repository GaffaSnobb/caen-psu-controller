from data_structures import Commands

commands_0520: dict[str, Commands] = {  # Commands for the Easy-Driver 0520.
    "MST": Commands(
        description = "Read module internal status register",
        is_read = True,
        is_write = False,
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
    ),
}