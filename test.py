import os
import main
from multiprocessing import Pool

a = main.create_requests(start_month = 1,
                  end_month = 12,
                  start_year = 2022 ,
                  end_year = 2025,
                  bbox = [90,90,90,90],
                  variables = ["2m_temperature"],
                  time_zone = "utc-06:00")

print(a)

