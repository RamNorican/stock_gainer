from dataclasses import dataclass
from typing import Optional, List


@dataclass
class CharacterSchema:
    """
    The schema for the response from the scrapper
    Sample Response:
    {
        'Symbol': 'BABA',
        'Name': 'Alibaba Group Holding Limited',
        'Change': 4.12,
        'Volume': '35.043M',
        'Price': 90.06,
        'Change_Per': 4.79,
        'Volume_Avg': '24.663M',
        'Market_Cap': '240.693B',
        'PE_Ratio': '112.57',
        '52_Week_Range': None
    }
    """
    Symbol: str
    Name: str
    Volume: str
    Price: float
    Change: float
    Change_Per: float
    Volume_Avg: str
    Market_Cap: str
    PE_Ratio: str
    Week_Range_52: Optional[str]


@dataclass
class ApiResponse:
    results: List[CharacterSchema]

    def __post_init__(self):
        if self.results is not None:
            self.results = [
                CharacterSchema(**schema) for schema in self.results
            ]
