from data_stream import generate_data_stream  # Import the function to generate a simulated data stream
from anomaly_detection import detect_anomaly  # Import the anomaly detection function
from visualization import plot_real_time  # Import the real-time plotting function

if __name__ == "__main__":  # Ensure this block runs only if the script is executed directly
    # Create a data stream with seasonal patterns and noise
    stream = generate_data_stream(seasonality=True, noise_level=0.5)
    
    # Detect anomalies with a window size of 50, threshold of 2, and alpha for EMA at 0.5
    detector = detect_anomaly(stream, window_size=50, threshold=2, alpha=0.5)

    # Plot real-time data with anomalies highlighted, and optionally save the plot
    plot_real_time(stream, detector, save_plot=True, output_file="final_anomaly_plot.png")