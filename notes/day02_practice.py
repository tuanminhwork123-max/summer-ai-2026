class JobRecord:
    def __init__(self, title: str, company: str, location: str) :
        self.title = title
        self.company = company
        self.location = location

    def to_dict(self) -> dict:
        return{
            "title": self.title,
            "company": self.company,
            "location": self.location,
        }

if __name__ == "__main__" :
    job = JobRecord("Backend dev", "ABC Corp", "Remote")
    print(job.to_dict())