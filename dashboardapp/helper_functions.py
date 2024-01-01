import matplotlib.pyplot as plt
import base64
from io import BytesIO
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend

def generate_time_series_chart(cleaned_data, title='Time Series Data', x_label='Time', y_label='Value'):
    # Create a figure and axis to plot on
    fig, ax = plt.subplots(figsize=(10,6))
    
    # Plotting the time series data
    ax.plot(cleaned_data['Year'], cleaned_data['Value'], label=y_label, color='blue', marker='o')
    
    # Adding titles and labels
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend()
    
    # Return the figure object
    return fig

def get_image(fig):
    """Converts a matplotlib figure to HTML compatible format"""
    buffer = BytesIO()
    fig.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    return graphic
