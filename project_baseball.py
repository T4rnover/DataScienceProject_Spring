# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 17:18:45 2023

@author: Tarnover
"""

import pybaseball
from pybaseball import statcast_running_splits
from pybaseball import statcast_sprint_speed
from pybaseball import statcast
import numpy as np
import pandas as pd
from pathlib import Path  
filepath = Path('N:/out.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  

#statcast(start_dt="2019-06-24", end_dt="2019-06-25").columns

# Raw split times for players with at least 50 opportunities in 2022
data = statcast_running_splits(2022, 50)

# Percentiles for players with at least 100 opportunities in 2022
data2 = statcast_sprint_speed(2022, 100)

# Raw split times for players with at least 50 opportunities in 2021
data3 = statcast_running_splits(2021, 50)

# Percentiles for players with at least 100 opportunities in 2021
data4 = statcast_sprint_speed(2021, 100)

# Raw split times for players with at least 50 opportunities in 2020
data5 = statcast_running_splits(2020, 50)

# Percentiles for players with at least 100 opportunities in 2020
data6 = statcast_sprint_speed(2020, 100)

# Raw split times for players with at least 50 opportunities in 2019
data7 = statcast_running_splits(2019, 50)

# Percentiles for players with at least 100 opportunities in 2019
data8 = statcast_sprint_speed(2019, 100)

# Raw split times for players with at least 50 opportunities in 2018
data9 = statcast_running_splits(2018, 50)

# Percentiles for players with at least 100 opportunities in 2018
data10 = statcast_sprint_speed(2018, 100)

# Raw split times for players with at least 50 opportunities in 2017
data11 = statcast_running_splits(2017, 50)

# Percentiles for players with at least 100 opportunities in 2017
data12 = statcast_sprint_speed(2017, 100)

running_splits_2017_2022 = data.append([data3,data5,data7,data9,data11])
running_splits_2017_2022.to_csv(filepath)


