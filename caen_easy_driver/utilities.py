import numpy as np

def response_stripper(response: bytes) -> bytes:
    """
    Strip the response of the metadata and keep only the two-digit hex
    response.
    ```
    >>> b'#MST:00\r'.split(b':')[-1][:-1]
    b'00'
    ```
    """
    return response.split(b':')[-1][:-1]

def access_bit(
    data: bytearray,
    num: None | int = None,
    fmt: str = "byte"
):
    """
    Access the bits in a bytearray. If num is None, return a list of
    lists of the bits in the bytearray. If num is an integer, return the
    bit at that index. If fmt is "bcd", then the bits are returned in
    groups of 4.

    Parameters
    ----------
    data : bytearray
        The data to access.

    num : int, optional
        The index of the bit to access. If None, return a list of lists
        of the bits in the bytearray.

    fmt : str
        The fmt of the data. If "bcd", then the bits are returned in
        groups of 4. If "byte", then the bits are returned in groups of
        8. If None, then the bits are returned as a single array.
    """
    if num is None:
        n_bytes = len(data)
        n_bits = n_bytes*8
        bit_array = np.zeros(n_bits, dtype=int)
        
        for bit in range(n_bits):
            base = int(bit//8)
            shift = int(bit%8)
            bit_array[bit] = (data[base] >> shift) & 0b1
        
        if fmt == "bcd":
            """
            For BCD, split the bit array into groups of 4.
            """
            return np.split(bit_array, n_bytes*2)
        elif fmt == "byte":
            """
            For byte, split the bit array into groups of 8.
            """
            return np.split(bit_array, n_bytes)
        else:
            return bit_array

    else:
        base = int(num//8)
        shift = int(num % 8)
        return (data[base] >> shift) & 0b1