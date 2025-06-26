from dataclasses import dataclass

@dataclass
class Province:
    """Represents a Zambian province."""
    name: str
    capital: str
    area_km2: float
    population: int

@dataclass
class City:
    """Represents a Zambian city or town."""
    name: str
    province: str
    is_capital: bool
    population: int = None