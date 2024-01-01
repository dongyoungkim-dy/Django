
import pandas as pd
import seaborn as sns
import plotly.express as px
from django.shortcuts import render

def home(request):
    # Load an example dataset from seaborn
    df = sns.load_dataset('flights')

    # Use Plotly to create a simple visualization
    fig = px.bar(df, x='year', y='passengers', color='month', title='Monthly Passenger Numbers Over Years')

    # Convert the figure to HTML and send it to the template
    graph = fig.to_html(full_html=False)
    context = {'graph': graph}
    return render(request, 'dashboardapp/home.html', context)

