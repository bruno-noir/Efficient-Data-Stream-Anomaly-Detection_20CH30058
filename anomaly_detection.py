import numpy as np
from collections import deque

def detect_anomaly(stream, window_size=50, threshold=2, alpha=0.3):
    """
    Detect anomalies in a data stream using a Z-score based method.
    
    Parameters:
    - stream: A generator yielding data points.
    - window_size: The number of previous values to consider for Z-score calculation.
    - threshold: The Z-score threshold above which points are considered anomalies.
    - alpha: Smoothing factor for Exponential Moving Average.
    
    Yields:
    - Tuple of (value, anomalies) where anomalies is a list of flagged anomalies.
    """
    values = deque(maxlen=window_size)  # Initialize a deque to hold the most recent values for Z-score calculation
    ema = None  # Initialize Exponential Moving Average (EMA) to None
    detected_anomalies = []  # List to store detected anomalies

    for value in stream:  # Iterate over each value yielded by the data stream
        values.append(value)  # Add the current value to the deque

        # Calculate the Exponential Moving Average (EMA)
        if ema is None:
            ema = value  # Set the first value as EMA if it is None
        else:
            ema = alpha * value + (1 - alpha) * ema  # Update EMA using the smoothing factor
        
        if len(values) == window_size:  # Check if the deque is full
            rolling_mean = np.mean(values)  # Calculate the rolling mean of the values
            rolling_std = np.std(values)  # Calculate the rolling standard deviation

            # Avoid division by zero in Z-score calculation
            if rolling_std != 0:
                z_score = (value - rolling_mean) / rolling_std  # Calculate the Z-score
            else:
                z_score = 0  # Set Z-score to 0 if standard deviation is 0
            
            # Check for anomaly based on Z-score
            if abs(z_score) > threshold:
                anomalies = [value]  # Flag the current value as an anomaly
                detected_anomalies.append(value)  # Log detected anomaly
                print(f"Anomaly Detected: Value: {value}, Z-score: {z_score}")  # Log value where anomaly is detected
            else:
                anomalies = []  # No anomalies detected
            
            yield value, anomalies  # Yield the current value and any detected anomalies
        else:
            yield value, []  # If not enough values, yield the current value with no anomalies
    
    # Optionally, return the detected anomalies at the end
    return detected_anomalies  # This return statement will not be reached during iteration
