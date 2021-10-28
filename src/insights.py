import src.jobs

# "src/jobs.csv"


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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
