from .utilities import response_stripper

def mst_mapper(
    response: bytes,
    is_enabled: bool = False
):
    """
    TODO: Map the 2 digit hex status register response to the correct
    meaning. The bits represent the following:
    7: reserved
    6: reserved
    5: external interlock
    4: sunt temperature
    3: mosfet temperature
    2: dc undervoltage
    1: fault
    0: module on
    """
    if is_enabled:
        return response & 0b00000001
    
    response = response_stripper(response=response)
    response = int(response, 16)
    return response
    # else:
    #     print("The module is disabled.")
    # if response & 0b00000010:
    #     print("The module has experienced a fault.")
    # else:
    #     print("No fault.")
    # if response & 0b00000100:
    #     print("A DC-Link under-voltage condition has been recognized.")
    # else:
    #     print("No under-voltage")
    # if response & 0b00001000:
    #     print("A MOSFET over-temperature condition has been experienced.")
    # else:
    #     print("MOSFET temperature OK.")
    # if response & 0b00010000:
    #     print("A shunt case over-temperature condition has been experienced.")
    # else:
    #     print("Shunt case temperature OK")
    # if response & 0b00100000:
    #     print("The corresponding external interlock trips.")
    # else:
    #     print("No external interlock.")

    return response