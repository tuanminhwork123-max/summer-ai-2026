import json
import csv
from collections import Counter

def load_jobs(filename: str) -> list[dict]:
    with open ("jobs_sample.json", "r", encoding="utf-8") as f:
        return json.load(f)

def count_tags(jobs: list[dict]) -> Counter:
    all_tags = [tag for job in jobs for tag in job["tags"]]
    return Counter(all_tags)

def export_to_csv(jobs: list[dict], filename:str) -> None:
    with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
       writer = csv.DictWriter(f, fieldnames=["title","company","location","tags"])
       writer.writeheader()
       for job in jobs:
           writer.writerow({
               "title": job["title"],
               "company": job["company"],
               "location": job["location"],
               "tags": ", ".join(job["tags"]),
           })

if __name__ == "__main__":
    jobs = load_jobs("jobs_sample.json")
    print(f"Tổng số job: {len(jobs)}")

    tag_counts = count_tags(jobs)
    print("Top 5 tag phổ biến nhất:")
    for tag, count in tag_counts.most_common(5):
        print(f"  {tag}: {count}")

    export_to_csv(jobs, "jobs.csv")
    print("Đã xuất jobs.csv") 