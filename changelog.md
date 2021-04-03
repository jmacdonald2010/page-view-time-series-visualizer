# in-progress branch changelog

## 04/02/2021 20:57
Passed the last test, finished the assignment. Merging to main after copying the repl.it link to freeCodeCamp.

## 04/02/2021 19:54
Fixed another error: out of order months for the boxplot.

## 04/02/2021 19:21
Fixed one issue, now only two tests failed. Passed tests are for data cleaning and line plot.

## 04/01/2021 19:52
Ran the test, had four failures. Failures are detailed below:

- Bar Plot, Legend Labels
    - Error: Legend error, expected month names, got list of tuples for (value, 01) etc. for months. 
    - Fix: Not sure at this time.
- Box Plot Labels
    - Error: Box plot 2 secondary labels are incorrect. Expected month names in order.
    - Possible Fix: Convert months to Datetime values, three letter month abbreviations.
- Data Cleaning Test:
    - Error: Dataframe count after cleaning should be 1238, not 1239.
    - Fix: Look to see if there's a row w/ an error or if something else may be wrong here.
- Test line Quality Plot Data:
    - Error: number of datapoints should be 1238, found 1239.
    - Fix: Should fix itself when the data cleaning test is fixed.

## 04/01/2021 19:39
Got the other chart to work and got it to plot w/ a subplot. I think I have everything I need to run the test. Curious to see what's not right; got a feeling it probably won't like me using pandas built-in plotting methods for charts.

## 04/01/2021 18:43
Figured out how to chart the first chart for years (need to still add a title). Need to figure out how to get both charts on the same figure, but before that, I need to make sure I can plot the other chart.

## 04/01/2021 07:42
Added the second bar chart code to the .py file. I'm not sure if I'll need to adjust the yticks for this chart yet, but I guess I'll find out when I run the test. Starting the seaborn plot, but I know this will take a while since I really have no idea how to use seaborn.

## 03/31/2021 07:50
My changes contain what I think either is or is very close to the example two chart. Sketches contain the chart and other code cells required to manipulate/pivot the data accordingly.

## 03/26/2021 20:06
Working on creating the bar chart. Figured out how to sum values by month, now working on how to plot it so all months are grouped by year. 

## 03/25/2021 19:22
Created the line plot function.

## 03/23/2021 22:05
Started coding. Currently, the csv is read into a dataframe, and we remove the top and bottom 2.5% of values to clean the data. Last commit/push of the night.

## 03/23/2021 21:47
init. commit to new branch in-progress