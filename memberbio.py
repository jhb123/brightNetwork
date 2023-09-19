from typing import TypeVar, Type, Optional, Tuple, List

from entity import Entity
from enums import Domain
from locations import example_locations

T = TypeVar('T', bound='Member')


class MemberBio(Entity):

    @classmethod
    def parse(cls: Type[T], entity_data: str) -> T:
        experience = cls._extract_experience(entity_data)
        locations = cls._extract_locations(entity_data)
        domain = cls._extract_domain(entity_data)
        return cls(locations=locations, experience=experience, domain=domain)

    @classmethod
    def _extract_experience(cls, raw_text: str) -> Optional[float]:
        # doing some sort of word stem analysis would make this cleaner
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

    @staticmethod
    def check_positive_location_intention(location,user_input):
        # TODO: this should analyse the user's data
        return True

    @classmethod
    def _extract_locations(cls, raw_text: str) -> Optional[List[Tuple[float, float]]]:
        # try to get where the person wants to work
        valid_locations = list()
        lower_case = raw_text.lower()
        for location in example_locations:
            if location in lower_case and cls.check_positive_location_intention(location,lower_case):
                valid_locations.append(example_locations[location])

        return valid_locations

    @classmethod
    def _extract_domain(cls, raw_text: str) -> Optional[Domain]:
        # doing some sort of word stem analysis would make this cleaner
        # i.e. there wouldn't need to be a hard coded list of phrases
        lower_case = raw_text.lower()
        if any(domain in lower_case for domain in ["software", "developer"]):
            return Domain.SOFTWARE
        elif any(domain in lower_case for domain in ["design", "designer"]):
            return Domain.DESIGN
        elif any(domain in lower_case for domain in ["marketing"]):
            return Domain.MARKETING
        else:
            return None
