"""
https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true
"""

SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION; 

"""
https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
"""

SELECT CITY AS C, LENGTH(CITY) AS LENGTH_CITY
FROM STATION
ORDER BY LENGTH_CITY ASC, C ASC
LIMIT 1;

SELECT CITY AS C, LENGTH(CITY) AS LENGTH_CITY 
FROM STATION
ORDER BY LENGTH_CITY DESC, CITY ASC 
LIMIT 1;