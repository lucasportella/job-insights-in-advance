import src.jobs

# to run this file uncomment the line below and comment the line above
# import jobs


def get_unique_job_types(path):
    unique_job_types = []
    data = src.jobs.read(path)
    for job in data:
        if job["job_type"] not in unique_job_types:
            unique_job_types.append(job["job_type"])
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    data = src.jobs.read(path)
    unique_industries = []
    for industry in data:
        if (
            industry["industry"] not in unique_industries
            and industry["industry"] != ""
        ):
            unique_industries.append(industry["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    data = src.jobs.read(path)
    biggest_salary = 0
    for salary in data:
        try:
            possible_max_salary = int(salary["max_salary"])
        except Exception:
            continue
        else:
            if possible_max_salary > biggest_salary:
                biggest_salary = possible_max_salary
    return biggest_salary


def get_min_salary(path):
    data = src.jobs.read(path)
    lowest_salary = "not_initialized"
    for salary in data:
        try:
            possible_lowest_salary = int(salary["min_salary"])
        except Exception:
            continue
        else:
            if (
                lowest_salary == "not_initialized"
                or possible_lowest_salary < lowest_salary
            ):
                lowest_salary = possible_lowest_salary
    return lowest_salary


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError(
            'job["min_salary"] or job["max_salary"] doesn\'t exists'
        )
    if not isinstance(job["max_salary"], int) or not isinstance(
        job["min_salary"], int
    ):
        raise ValueError(
            'job["min_salary"] or job["max_salary"] aren\'t valid integers'
        )
    if job["min_salary"] > job["max_salary"]:
        raise ValueError(
            'job["min_salary"] is greather than job["max_salary"]'
        )
    if not isinstance(salary, int):
        raise ValueError('salary isn\'t a valid integer')
    if job["max_salary"] >= salary >= job["min_salary"]:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    filter_matches = []
    for job in jobs:
        try:
            salary_range_matched = matches_salary_range(job, salary)
        except Exception:
            continue
        else:
            if salary_range_matched:
                filter_matches.append(job)
    return filter_matches


filter_by_salary_range([
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 15000, "min_salary": 0},
        {"max_salary": 1500, "min_salary": 0},
        {"max_salary": -1, "min_salary": 10},
    ], 0)
