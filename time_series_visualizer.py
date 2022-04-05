import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    df_line = df.set_index('date')
    fig, ax = plt.subplots(figsize=(18,8))
    df_line['value'].plot(ax=ax, color= "red").get_figure()
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_ylabel("Page Views")
    ax.set_xlabel("Date")
  
    
      
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    df_bar = df.copy()
    df_bar['date'] = pd.to_datetime(df_bar['date'])
   # df_bar['month'] = pd.DatetimeIndex(df['date']).month_name()
    df_bar = df_bar.set_index('date')
    df_bar = df_bar.resample('D').mean()
    df_bar = df_bar.dropna()
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).month_name()
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
      

    fig,ax = plt.subplots(1,1,figsize=(20,10))
    sns.barplot(data=df_bar, x='year',y='value', hue='month', hue_order=months, ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    # Draw bar plot

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box = df.copy()
    df_box['year'] = pd.DatetimeIndex(df_box['date']).year
    df_box['month'] = pd.DatetimeIndex(df_box['date']).month_name().str[:3]
    df_box.reset_index(inplace=True)
    

    # Draw box plots (using Seaborn)
    fig,(ax1,ax2) = plt.subplots(1,2,figsize=(20,10))
    sns.boxplot(data=df_box, x='year',y='value', ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')
    sns.boxplot(data=df_box, x='month',y='value',order=months, ax=ax2) 
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
