import dataclasses


@dataclasses.dataclass
class Model:
    """Core model data class"""
    pass


@dataclasses.dataclass
class Member(Model):
    """Data class to represent members"""
    name: str
    bio: str

    def __str__(self) -> str:
        return self.name


@dataclasses.dataclass
class Job(Model):
    """Data class to represent jobs"""
    title: str
    location: str

    def __str__(self) -> str:
        return f"{self.title} in {self.location}"


class JobsManager:
    """Manager for `Job` objects"""
    def __init__(self, jobs: list[Job]):
        self.jobs = jobs

    def to_str(self) -> list[str]:
        return [str(j) for j in self.jobs]

    def search_by_location(self, member: Member) -> "JobsManager":
        suitable_jobs: list[Job] = []

        for job in self.jobs:
            if job.location in member.bio:
                suitable_jobs.append(job)
        
        return self.__class__(suitable_jobs)

    def search_by_role(self, member) -> "JobsManager":
        suitable_roles: list[Job] = []

        for job in self.jobs:
            for word in job.title.split(" "):
                if word.lower() in member.bio.lower():
                    suitable_roles.append(job)
                    break
        
        return self.__class__(suitable_roles)
