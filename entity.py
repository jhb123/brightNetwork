from abc import ABC, abstractmethod
from typing import Optional, TypeVar, Type, Tuple, List

from enums import Domain

T = TypeVar('T', bound='Member')


class Entity(ABC):

    def __init__(self, experience: float, locations: List[Tuple[float, float]], domain: Domain):
        self.experience = experience
        self.locations = locations
        self.domain = domain

    def __repr__(self):
        return f"{self.experience:}, {self.locations:}, {self.domain:}"

    @classmethod
    @abstractmethod
    def parse(cls: Type[T], entity_data) -> T:
        pass

    @classmethod
    @abstractmethod
    def _extract_experience(cls, raw_text: str) -> Optional[float]:
        pass

    @classmethod
    @abstractmethod
    def _extract_locations(cls, raw_text: str) -> Optional[List[Tuple[float, float]]]:
        pass

    @classmethod
    @abstractmethod
    def _extract_domain(cls, raw_text: str) -> Optional[Domain]:
        pass
