# This is a sample Python script.
import json
import uuid
from math import sqrt, log
from typing import Optional

from entity import Entity
from job import Job
from locations import max_distance
from memberbio import MemberBio


def member_data_ingestion():
    with open('members.json') as member_file:
        member_json = json.load(member_file)

    members = dict()

    for member in member_json:
        members[uuid.uuid4()] = (member["name"], MemberBio.parse(member["bio"]))

    return members


def job_data_ingestion():
    with open('jobs.json') as jobs_file:
        job_json = json.load(jobs_file)

    jobs = dict()

    for job in job_json:
        jobs[job["title"]] = Job.parse(job)

    return jobs


def calculate_location_factor(p0: Entity, p1: Entity) -> Optional[float]:
    location_factor = None
    if len(p0.locations)  > 0 and len(p1.locations) > 0:
        location_factor = 1-(sqrt((p0.locations[0][0] - p0.locations[0][0]) ** 2 \
                                               + (p1.locations[0][1] - p1.locations[0][1]) ** 2)) / max_distance
    return location_factor


def calculate_domain_factor(p0: Entity, p1: Entity) -> Optional[float]:
    domain_factor = None

    if p0.domain is not None and p1.domain is not None:
        if p0.domain == p1.domain:
            domain_factor = 1
        else:
            domain_factor = 0
    return domain_factor


def calculate_experience_factor(p0: Entity, p1: Entity) -> Optional[float]:
    experience_factor = None

    if p0.experience is not None and p1.experience is not None:
        experience_factor = 1 - abs(p0.experience-p0.experience)
    return experience_factor


def evalutate_compatibility(p0: Entity, p1: Entity):

    location_factor = calculate_location_factor(p0, p1)
    domain_factor = calculate_domain_factor(p0, p1)
    experience_factor = calculate_experience_factor(p0, p1)

    total = 0
    for factor in [location_factor,domain_factor,experience_factor]:
        if factor:
            total += factor**2

    normalised = sqrt(total)/3
    return normalised


if __name__ == '__main__':
    members = member_data_ingestion()
    jobs = job_data_ingestion()

    for job in jobs:
        print(jobs[job])

    for member in members:
        print(f"{members[member][0]}'s match data")
        for job in jobs:
            compatibility = evalutate_compatibility(members[member][1], jobs[job])
            print(f"{job}::{compatibility:.3f}")
