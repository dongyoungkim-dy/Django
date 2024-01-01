# import pandas as pd
# import seaborn as sns
# import plotly.express as px
# from django.shortcuts import render

# def home(request):
#     # Load an example dataset from seaborn
#     df = sns.load_dataset('flights')

#     # Use Plotly to create a simple visualization
#     fig = px.bar(df, x='year', y='passengers', color='month', title='Monthly Passenger Numbers Over Years')

#     # Convert the figure to HTML and send it to the template
#     graph = fig.to_html(full_html=False)
#     context = {'graph': graph}
#     return render(request, 'dashboardapp/home.html', context)


from django.shortcuts import render
from .data_fetcher import fetch_gdp, fetch_inflation, merge_data  # replace with actual function names
from .helper_functions import generate_time_series_chart, get_image

# ... (rest of your imports and the generate_chart and get_image functions)

def home(request):
    # Getting country code from the request, default to 'ALL'
    country_code = request.GET.get('country', 'ALL')

    # Fetch and clean data
    gdp_data = fetch_gdp(country_code)
    inflation_data = fetch_inflation(country_code)
    cleaned_data = merge_data(gdp_data, inflation_data)

    # Assuming you want separate charts for GDP and Inflation
    gdp_chart = generate_time_series_chart(gdp_data, title='GDP Over Time', x_label='Year', y_label='GDP')
    inflation_chart = generate_time_series_chart(inflation_data, title='Inflation Rate Over Time', x_label='Year', y_label='Inflation')

    # Convert the figures to images
    gdp_graphic = get_image(gdp_chart)
    inflation_graphic = get_image(inflation_chart)

    context = {
        'gdp_graphic': gdp_graphic,
        'inflation_graphic': inflation_graphic,
        # Include other context variables you might need, like country options for dropdown
    }
    return render(request, 'dashboardapp/home.html', context)


