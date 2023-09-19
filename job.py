from typing import TypeVar, Type, Optional, List, Tuple

from entity import Entity
from enums import Domain
from locations import example_locations

T = TypeVar('T', bound='Job')


class Job(Entity):
    @classmethod
    def parse(cls: Type[T], entity_data: dict) -> T:
        experience = cls._extract_experience(entity_data["title"])
        locations = cls._extract_locations(entity_data["location"])
        domain = cls._extract_domain(entity_data["title"])
        return cls(locations=locations, experience=experience, domain=domain)

    @classmethod
    def _extract_experience(cls, raw_text: str) -> float:
        lower_case = raw_text.lower()
        # some semi-arbitrary mapping.
        if any(experience in lower_case for experience in ["intern", "internship"]):
            return 0.1
        elif "junior" in lower_case:
            return 0.5
        elif "senior" in lower_case:
            return 1
        else:
            return None

    @classmethod
    def _extract_locations(cls, raw_text: str) -> Optional[List[Tuple[float, float]]]:
        lower_case = raw_text.lower()
        return [example_locations[lower_case]]


    @classmethod
    def _extract_domain(cls, raw_text: str) -> Domain:
        # doing some sort of word stem analysis would make this cleaner
        # i.e. there wouldn't need to be a hard coded list of phrases
        lower_case = raw_text.lower()
        if "software" in lower_case:
            return Domain.SOFTWARE
        elif "marketing" in lower_case:
            return Domain.MARKETING
        elif "data" in lower_case:
            return Domain.DATASCIENCE
        elif "manager" in lower_case:
            return Domain.MANAGEMENT
        elif "sales" in lower_case:
            return Domain.SALES
        elif "designer" in lower_case:
            return Domain.DESIGN
        else:
            return None
