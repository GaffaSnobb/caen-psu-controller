def mst_mapper(response: bytes):
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
    return response