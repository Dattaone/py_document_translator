from dataclasses import dataclass, field
from enum import Enum

class TextUnitType(Enum):
    PARAGRAPH   = "paragraph"
    HEADING     = "heading"     

@dataclass
class TextUnit:
    id      : int
    type    : TextUnitType
    text    : str
    metadata: dict = field(default_factory=dict)
