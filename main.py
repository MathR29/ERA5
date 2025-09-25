import os
import cdsapi

def temporal_interval(start_month, start_year, end_month, end_year):
    temp_interval = {}
    days_interval = [d.rjust(2,"0") for d in map(str,range(1,32))]
    years_interval = map(str,range(start_year,end_year + 1))
    months_interval = [m.rjust(2,"0") for m in map(str,range(start_month,end_month+1))]

    for year in years_interval:
        temp_interval[year] = {"months": months_interval,"days":days_interval}

    return(temp_interval)

def create_requests(start_month:int,start_year:int,end_month:int,end_year:int,
                    bbox:list ,variables:list,time_zone:str):
    temp_interval= temporal_interval(start_month,
                                     start_year,
                                     end_month,
                                     end_year)
    requests = {}

    for variable in variables:
        if variable == "2m_temperature":
            for stat in ["daily_mean","daily_maximum","daily_minimum"]:
                for year,month_day in temp_interval.items():
                    request_body = {
                    "product_type": "reanalysis",
                    "variable": variable,
                    "year": year,
                    "month":month_day["months"],
                    "day":month_day["days"],
                    "daily_statistic":stat,
                    "time_zone":time_zone,
                    "frequency": "1_hourly",
                    "area": bbox
                }
                    requests[f"{year}_{variable}_{stat}"] = request_body

        else:
            for year,month_day in temp_interval.items():
                request_body = {                                    
                    "product_type": "reanalysis",                       
                    "variable": variable,                               
                    "year": year,                                       
                    "month":month_day["months"],                        
                    "day":month_day["days"],                            
                    "daily_statistic":"daily_mean",                             
                    "time_zone":time_zone,                              
                    "frequency": "1_hourly",                            
                    "area": bbox
                }
                requests[f"{year}_{variable}"] = request_body

    return requests

def make_request(start_month:int,start_year:int,end_month:int,end_year:int,
                 bbox:list ,variables:list,time_zone:str):
    
    dataset = "derived-era5-single-levels-daily-statistics"
    requests = create_requests(start_month,
                            start_year,
                            end_month,
                            end_year,
                            bbox,
                            variables,
                            time_zone)

    for req_name,req in requests.items():
        client = cdsapi.Client(
            url = "https://cds.climate.copernicus.eu/api",
            key = "9530b858-ba68-430c-8a18-3d3112b45ace"
        )
        client.retrieve(
            dataset,
            req,
            target = f"{req_name}.nc"
        )

make_request(9,2025,10,2025,[90,90,90,90],["10m_u_component_of_wind"],"utc-06:00")
