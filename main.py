def temporal_interval(start_month, start_year, end_month, end_year):
    temp_interval = {}
    days_interval = [d.rjust(2,"0") for d in map(str,range(1,32))]
    years_interval = map(str,range(start_year,end_year + 1))
    months_interval = [m.rjust(2,"0") for m in map(str,range(start_month,end_month+1))]

    for year in years_interval:
        temp_interval[year] = {"months": months_interval,"days":days_interval}

    return(temp_interval)





