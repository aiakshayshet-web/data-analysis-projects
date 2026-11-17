# Weather analysis: three Australian stations

Daily weather for Wollongong, Hobart, and Uluru: 296 usable days (2008-2020). Source: `weather_australia` (a sub-sample of the BoM data in the R `rattle` package, via the R `bayesrules` package). See `SOURCE.md`.

Only about 100 days per station are included, so treat monthly patterns as indicative.

## Station summary

| location | days | avg_max_c | avg_min_c | mean_rain_mm | rainy_day_pct |
| --- | --- | --- | --- | --- | --- |
| Uluru | 97 | 31.2 | 14.6 | 0.52 | 12.4 |
| Wollongong | 100 | 21.2 | 14.4 | 1.71 | 24.0 |
| Hobart | 99 | 17.5 | 9.0 | 1.94 | 44.4 |

Rainy day = any recorded rainfall above 0 mm.

## Highlights

- Warmest station on average (max temp): **Uluru** (31.2°C)
- Hottest sampled day: **Uluru**, 45.4°C (year 2019, month 1)
- Wettest sampled day: **Wollongong**, 36.2 mm (year 2018, month 2)

See `weather_temps.png` and `weather_rain.png`.
