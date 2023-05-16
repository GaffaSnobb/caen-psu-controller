from dataclasses import dataclass
from typing import Callable

@dataclass
class Commands:
    # command: str
    description: str
    is_read: bool
    is_write: bool
    response_mapper: Callable