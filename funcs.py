import os
import cdsapi
from functools import partial
from multiprocessing import Pool


def create_request(variable,bbox,time_zone,month,year):
    request = {}
    if variable != "2m_temperature":
        stat = "daily_mean"
        request[f"{year}_{month}_{variable}_{stat}"] = {
            "product_type": "reanalysis",
            "variable": variable,                               
            "year": year,                                       
            "month": month,                        
            "day": [str(i).zfill(2) for i in range(1, 32)],                            
            "daily_statistic": stat,                             
            "time_zone": time_zone,                              
            "frequency": "1_hourly",                            
            "area": bbox
        }

    else:
        stats = ["daily_mean","daily_maximum","daily_minimum"]
        for stat in stats:
            request[f"{year}_{month}_{variable}_{stat}"] = {
                    "product_type": "reanalysis",                  
                    "variable": variable,                          
                    "year": str(year),                                      
                    "month": "{month:02d}".format(month=month),                               
                    "day": [str(i).zfill(2) for i in range(1, 32)],
                    "daily_statistic": stat,                      
                    "time_zone": time_zone,                        
                    "frequency": "1_hourly",                       
                    "area": bbox
                }

    return request.items()


def create_all_request(variables,bbox,time_zone,
                       start_month,end_month,
                       start_year,end_year):
    requests = {}
    files = os.listdir("output")
    for var in variables:
        for year in range(start_year,end_year + 1):
            for month in range(start_month,end_month + 1):
                for req_name, req in create_request(var,bbox,time_zone,month,year):
                    if f"{req_name}.nc" in files:
                        print(f"{req_name} already downloaded.")
                        continue
                    else:
                        requests[req_name] = req



    return requests.items()


def download_request(req,user_key):
    req_name,req_body = req
    dataset = "derived-era5-single-levels-daily-statistics"
    client = cdsapi.Client(
            url = "https://cds.climate.copernicus.eu/api",
            key = user_key
    )

    client.retrieve(dataset, req_body, target=f"output/{req_name}.nc")
    return f"{req_name} done"


def get_era5 (variables,bbox,time_zone,
              start_month,end_month,
              start_year,end_year,user_key):

    requests = create_all_request(variables,bbox,time_zone,
                                  start_month,end_month,
                                  start_year,end_year)

    worker = partial(download_request,user_key = user_key)

    with Pool(processes=4) as pool:
        results = pool.map(worker,requests)
        print(results)

