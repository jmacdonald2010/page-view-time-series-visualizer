import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

# Clean data
df = df[df['value'] > df['value'].quantile(0.025)]
df = df[df['value'] < df['value'].quantile(.975)]


def draw_line_plot():
    # Draw line plot
    fig = df.plot(y='value', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.reset_index()
    df_bar['date'] = pd.to_datetime(df_bar['date'], format='%Y-%m')
    df_bar = df_bar.groupby(pd.Grouper(key='date', freq='M')).sum()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = pd.pivot_table(df_bar, values='value', index=['year', 'month'])

    # Draw bar plot
    fig = df_bar.unstack().plot(kind='bar', xlabel='Years', ylabel='Average Page Views')  # this may require additional work for the yticks
    fig.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['date'] = pd.to_datetime(df_box['date'], format='%Y-%m') # adding this line b/c their's doesn't work
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
