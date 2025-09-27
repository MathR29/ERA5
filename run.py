import funcs

if __name__ == "__main__":
    tasks = funcs.get_era5(
        start_month=1,
        end_month=12,
        start_year=2022,
        end_year=2025,
        bbox=[40.613687151061505,
              -95.76804054400543,
              35.99538225441254,
              -89.09913230512305
              ],
        variables=["2m_temperature"],
        time_zone="utc-06:00",
        user_key = "9530b858-ba68-430c-8a18-3d3112b45ace"
    )


