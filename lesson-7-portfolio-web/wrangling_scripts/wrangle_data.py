import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    df=pd.read_csv('./data/Unicorn_Clean.csv')
    df['Date Joined Year']=df['Date Joined'].astype('datetime64[ns]').dt.year
    
    df_1=df[['Country','Valuation ($B)','Date Joined Year']]
    df_1=df_1[df['Country'].isin(['United States'])]
    df_1=df_1.groupby(['Country','Date Joined Year'])['Valuation ($B)'].sum().reset_index().sort_values(by='Date Joined Year',ascending=True)

    df_1.columns=['Country','Year','Valuation']
    df_1=df_1.tail(10)
    x_val=df_1.Year.tolist()
    y_val=df_1.Valuation.tolist()
    
    graph_one = []    
    graph_one.append(
      go.Scatter(
      x = x_val,
      y = y_val,
      mode = 'lines'
      )
    )

    layout_one = dict(title = 'Valuation of Unicorn in US by year',
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Valuation ($B)'),
                )

# second chart plots ararble land for 2015 as a bar chart    
    df_2=df[['Country','Valuation ($B)','Date Joined Year']]
    df_2=df_2[df['Date Joined Year'].isin([2021])]
    df_2=df_2.groupby(['Country','Date Joined Year'])['Valuation ($B)'].sum().reset_index().sort_values(by='Valuation ($B)',ascending=False)
    df_2=df_2.head(10)
    df_2.columns=['Country','Year','Valuation']
    x_val=df_2.Country.tolist()
    y_val=df_2.Valuation.tolist()
    graph_two = []

    graph_two.append(
      go.Bar(
      x = x_val,
      y = y_val,
      )
    )

    layout_two = dict(title = 'Valation ($B) by Country',
                xaxis = dict(title = 'Country',),
                yaxis = dict(title = 'Valuation ($B)'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    
    df_3=df[(df['Country']=='United States')&(df['Date Joined Year']==2021)]
    df_3=df_3[['City','Valuation ($B)','Date Joined Year']]

    df_3=df_3.groupby(['City','Date Joined Year'])['Valuation ($B)'].sum().reset_index().sort_values(by='Valuation ($B)',ascending=False)

    df_3.columns=['City','Year','Valuation']
    df_3=df_3.head(10)
    graph_three = []
    x_val=df_3.City.tolist()
    y_val=df_3.Valuation.tolist()
    graph_three.append(
      go.Scatter(
      x = x_val,
      y = y_val,
      mode = 'lines'
      )
    )

    layout_three = dict(title = 'Valation of top 10 City in US in 2021',
                xaxis = dict(title = 'City'),
                yaxis = dict(title = 'Valuation ($B)')
                       )
    
# fourth chart shows rural population vs arable land
    top_5=['Fintech','Internet software & services','Artificial intelligence','E-commerce & direct-to-consumer','Health']
    df_4=df[df['Industry'].isin(top_5)]
    df_4=df_4[['Industry','Valuation ($B)','Date Joined Year']]

    df_4=df_4.groupby(['Industry','Date Joined Year'])['Valuation ($B)'].sum().reset_index().sort_values(by='Valuation ($B)',ascending=False)

    df_4.columns=['Industry','Year','Valuation']
    graph_four = []
    for ind in top_5:
        x_val=df_4[df_4['Industry']==ind].Year.tolist()
        y_val=df_4[df_4['Industry']==ind].Valuation.tolist()
        graph_four.append(
      go.Scatter(
      x = x_val,
      y = y_val,
      mode = 'lines',
      name=ind
      )
    )

    layout_four = dict(title = 'Valuation of Industry by Year',
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Valuation ($B)'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures