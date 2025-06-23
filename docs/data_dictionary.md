# Data Dictionary

| Column Name           | Type      | Description                                  |
|-----------------------|-----------|----------------------------------------------|
| structure_id          | string    | Unique identifier for bridge/road/pipe       |
| inspection_date       | date      | Date of most recent inspection               |
| last_maintenance_date | date      | Date of last maintenance                     |
| avg_daily_traffic     | int       | Average daily traffic (vehicles)             |
| bridge_condition      | string    | Condition rating by inspector                |
| cond_encoded          | int       | Numeric encoding of condition (0-4)          |
| latitude              | float     | Latitude coordinate                          |
| longitude             | float     | Longitude coordinate                         |
| precipitation         | float     | Precipitation (mm) at structure              |
| avg_temp              | float     | Average temperature (Celsius)                |
| corrosion_level       | float     | Measured corrosion (if available)            |
| previous_failures     | int       | Number of previous failures                  |
| soil_type             | string    | Type of soil (if available)                  |
| region_code           | string    | Administrative region                        |

## Feature Columns (engineered)
- traffic_condition_ratio
- maintenance_interval
- recent_maintenance
- weather_stress
- region_cluster

## Target
- failure_within_1yr: 0/1, whether structure failed within 1 year