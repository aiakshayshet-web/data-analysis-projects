# Sales analysis: avocados in California

**Dataset:** `169` weekly observations, 2015-01-04 to 2018-03-25, conventional avocados sold in California. Source: the `avocado` dataset (Hass Avocado Board data, via Kiggins 2018 and the R `causaldata` package). See `SOURCE.md`.

Revenue is estimated as weekly average price x total volume sold.

| Metric | Value |
| --- | ---: |
| Estimated total revenue | 1,079,637,731 |
| Total avocados sold | 1,003,596,841 |
| Average weekly price | 1.11 |

## By year

Note: 2018 is a partial year (data ends in March).

| year | weeks | revenue | avg_price | avg_weekly_volume |
| --- | --- | --- | --- | --- |
| 2015 | 52 | 299,775,329 | 1.02 | 5,681,498 |
| 2016 | 52 | 321,655,803 | 1.05 | 6,105,539 |
| 2017 | 53 | 371,831,533 | 1.25 | 5,834,479 |
| 2018 | 12 | 86,375,066 | 1.08 | 6,786,962 |

## Findings

- Best month for revenue: **2017-07** (40,093,810). Months contain 4 or 5 weeks, so this is a total, not a weekly average.
- Highest average price month: **2017-09** (1.71)
- Price and volume correlation across weeks: **-0.66**

See `sales_trend.png` and `sales_charts.png`.
