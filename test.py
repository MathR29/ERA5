import cdsapi

dataset = "derived-era5-single-levels-daily-statistics"
request = {
    "product_type": "reanalysis",
    "variable": ["10m_u_component_of_wind"],
    "year": "2021",
    "month": ["08"],
    "day": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12",
        "13", "14", "15",
        "16", "17", "18",
        "19", "20", "21",
        "22", "23", "24",
        "25", "26", "27",
        "28", "29", "30",
        "31"
    ],
    "daily_statistic": "daily_mean",
    "time_zone": "utc-06:00",
    "frequency": "1_hourly",
    "area": [90, -180, -90, 180]
}

client = cdsapi.Client("https://cds.climate.copernicus.eu/api","9530b858-ba68-430c-8a18-3d3112b45ace")
client.retrieve(dataset, request).download()
