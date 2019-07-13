Expose the sample dataset through a single generic HTTP API endpoint, which is capable of filtering, grouping and sorting. Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system. It is expected to be stored and processed in a relational database of your choice.

Sample dataset: sample_data.csv

Client of this API should be able to:
1) filter by time range (date_from / date_to is enough), channels, countries, operating systems
2) group by one or more columns: date, channel, country, operating system
2) sort by any column in ascending or descending order

Please make sure that the client can use filtering, grouping, sorting at the same time. 

Common API use cases:
1) Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order. Hint:
```
=> select channel, country, sum(impressions) as impressions, sum(clicks) as clicks from sampledataset where date <= '2017-06-01' group by channel, country order by clicks desc;
     channel      | country | impressions | clicks 
------------------+---------+-------------+--------
 adcolony         | US      |      532608 |  13089
 apple_search_ads | US      |      369993 |  11457
 vungle           | GB      |      266470 |   9430
 vungle           | US      |      266976 |   7937
 ...
```
2) Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
3) Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

On top of that, implement CPI (cost per install) metric which is calculated as cpi = spend / installs. Use case: show CPI values for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.

Please make sure you have single API endpoint that is compliant with all use-cases described above and similar.

We expect it to be written in the way so that it could go in production and be maintained by your teammates - please have in mind that we use Python 3 and Django. Don't spend too much time on Docker (if any), that's not what we pay attention to.

Feel free to ask me a question on skype vitaliy.kotik. 

When ready, please share your private repository with https://github.com/kotik