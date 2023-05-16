from dataclasses import dataclass

@dataclass
class Commands:
    # command: str
    description: str
    is_read: bool
    is_write: bool