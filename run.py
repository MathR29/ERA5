import os
import main
from functools import partial
from multiprocessing import Pool, pool

if __name__ == "__main__":
    tasks = main.create_requests(
        start_month=1,
        end_month=12,
        start_year=2022,
        end_year=2025,
        bbox=[90,90,90,90],
        variables=["2m_temperature"],
        time_zone="utc-06:00"
    )

    worker = partial(main.download_worker,user_key = "9530b858-ba68-430c-8a18-3d3112b45ace")

    with Pool(processes=6) as pool:
        results = pool.map(worker,tasks)
