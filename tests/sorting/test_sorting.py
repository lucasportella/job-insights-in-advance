from src.sorting import sort_by
import pytest


def test_sort_by_criteria():
    criteria_keys = ["date_posted", "max_salary", "min_salary"]
    invalid_criteria_key = "abc"
    # job data imported from here https://github1s.com/tryber/sd-09-project-job-insights/pull/1
    job_1 = {
        "job_name": "Diesel Mechanic",
        "min_salary": 46298,
        "max_salary": 55893,
        "date_posted": "2021-09-09",
    }

    job_2 = {
        "job_name": "Ultrasound Technologist",
        "min_salary": 55069,
        "max_salary": 74745,
        "date_posted": "2021-02-02",
    }

    jobs = [job_1, job_2]

    with pytest.raises(
        ValueError, match=f"invalid sorting criteria: {invalid_criteria_key}"
    ):
        sort_by(jobs, invalid_criteria_key)
