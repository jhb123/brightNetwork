# Introduction

Jobs and people have very similar properties
- location
- experience
- domain/field/industry

There is an abstract base class that represents both jobs and people, and their concrete implementations differ in how they convert inputted data an `entity` object.

The core principles behind this alogirthm is are:
- be a permissive as possible. I don't want to make too many assumptions about the user. If they don't specify e.g. an experience level, then all a job's experience level should not affect the calculation
- a job and person can be parameterised into 3 dimensions. I calculate somthing akin to the Euclidean distance between each person.

I saw two main challenges:
- processing the natural language from the JSON data. 
- determining a good set of methods and classes

I focussed on the final point. 

The first point can be solved with a large language model which converts unstructured user biographies and job descriptions into a structure format. Parsing this data is technically challenging, e.g. how do you distinguish something semantically equivalent to "not london" from "London" robustly, and premade solutions do exist for this.
I was happy to have my algorithm not work on cases which were any harder to parse that "check if city is in their bio"

Optimising the algorithm would take quite a bit of time (its time complexity is O(NM), when N and M the lengths of the lists), but avenues of interest are
- caching results. there are times when a load of people and a load of jobs are described by the same set of parameters.
- maybe some sorting by experience could prevent you needing to compare jobs unnecessarily and reduce your search space.

Getting a good set of classes and methods was the most important thing to get right. I used
- Enums for the type of job. This might break down eventually, but I thought you could put jobs into categories this way.
- a float for the experience. I thought there may be times when "x number of years" experience might show up in job adds. Having a function which maps text onto a scale from 0 to 1 means we can robustly compare entities.
- a list of coordinates (Tuples) for a location. I imagined you'd ultimately want a 2d array i.e. map of places you'd able to commute to and you can check if the job's coordinates are in that map.




