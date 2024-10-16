import numpy as np

def generate_data_stream(length=1000, seasonality=True, noise_level=0.5):
    """
    Generates a simulated data stream with optional seasonality and noise.
    
    Parameters:
    - length: Number of data points in the stream.
    - seasonality: Boolean, if True, adds seasonal patterns to the data.
    - noise_level: Level of random noise to add to the data.
    
    Yields:
    - Data point (float) from the simulated stream.
    """
    # Create an array of time values from 0 to length-1
    time = np.arange(length)

    # Base sine wave for seasonality: creates a repeating pattern if seasonality is True
    seasonal_pattern = np.sin(time / 50) if seasonality else np.zeros(length)

    for t in range(length):
        # Introduce extreme anomalies every 100th value by adding a large positive value
        if t % 100 == 0:
            # Add an anomaly by introducing a high value (+10) along with normal noise
            value = seasonal_pattern[t] + np.random.normal(0, noise_level) + 10  # Introduce an anomaly
        else:
            # Regular data point with added noise
            value = seasonal_pattern[t] + np.random.normal(0, noise_level)
        
        yield value  # Yield the generated value to simulate a continuous data stream
