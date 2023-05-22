from data_structures import Commands
from mappers import mst_mapper

no_mapper = lambda response: response

commands_0520: dict[str, Commands] = {  # Commands for the Easy-Driver 0520.
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
    "MST": Commands(
        description = "Read module internal status register",
        is_read = True,
        is_write = False,
        response_mapper = mst_mapper,
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
    "FDB": Commands(
        description = "Feedback command",
        is_read = False,
        is_write = True,
        response_mapper = no_mapper,
    ),
    "MRESET": Commands(
        description = "Reset the module status register",
        is_read = False,
        is_write = True,
        response_mapper = no_mapper,
    ),
    "MRG": Commands(
        description = "Read selected EEPROM 'value' cell",
        is_read = True,
        is_write = False,
        response_mapper = no_mapper,
    ),
    "MRI": Commands(
        description = "Read output current value",
        is_read = True,
        is_write = False,
        response_mapper = no_mapper,
    ),
    "MRID": Commands(
        description = "Read module identification",
        is_read = True,
        is_write = False,
        response_mapper = no_mapper,
    ),
    "MRM": Commands(
        description = "Set output current value (ramp)",
        is_read = False,
        is_write = True,
        response_mapper = no_mapper,
    ),
    "MRP": Commands(
        description = "Read DC-Link voltage value",
        is_read = True,
        is_write = False,
        response_mapper = no_mapper,
    ),
    "MRSR": Commands(
        description = "Read current Slew Rate",
        is_read = True,
        is_write = False,
        response_mapper = no_mapper,
    ),
    "MRT": Commands(
        description = "Read output stage heatsink temperature",
        is_read = True,
        is_write = False,
        response_mapper = no_mapper,
    ),
    "MRTS": Commands(
        description = "Read regulation shunt temperature",
        is_read = True,
        is_write = False,
        response_mapper = no_mapper,
    ),
    "MRV": Commands(
        description = "Read output voltage value",
        is_read = True,
        is_write = False,
        response_mapper = no_mapper,
    ),
    "MVER": Commands(
        description = "Power Supply firmware version",
        is_read = True,
        is_write = False,
        response_mapper = no_mapper,
    ),
    "MWG": Commands(
        description = "Write selected EEPROM 'value' cell",
        is_read = False,
        is_write = True,
        response_mapper = no_mapper,
    ),
    "MPUP": Commands(
        description = "Reload EEPROM values in DSP",
        is_read = False,
        is_write = True,
        response_mapper = no_mapper,
    ),
    "MWSR": Commands(
        description = "Write current Slew Rate",
        is_read = False,
        is_write = True,
        response_mapper = no_mapper,
    ),
    "MWI": Commands(
        description = "Set output current value (no ramp)",
        is_read = False,
        is_write = True,
        response_mapper = no_mapper,
    ),
}
