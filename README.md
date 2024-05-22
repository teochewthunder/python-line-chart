# Python Line Chart
This builds on the earlier [Python Bar Chart](https://github.com/teochewthunder/python-bar-chart). Differences are highlighted below.

## Data
- Same as Python Bar Chart.

## Script
- Display a numbered list of available players in the data, with a 0 for exiting.
- Iterate through `data`, adding player names to a list. After that, convert the list to a dictionary, which automatically removes all duplicates, then convert back to a list, and sort.
- Request for input to select a player.
  - Utilize a `Try-catch` to ensure only numerical data is entered.
  - If value is numerical but out of bounds, do-over.
  - If value is 0, end program.
- Use the selected player to generate the line chart.

## Chart
We use the `matplotlib` library to plot the line chart, and the `numpy` library to access aggregation functions.
- An average line can be drawn using the `axhline()` method from `matplotlib`, using as an an argument a value derived from using the `nanmean()` method of `numpy`.
- Goals and appearances are represented using different colors.
- Averages are represented using dashed lines.
- The labels for goals and appearances are placed above the average lines.
