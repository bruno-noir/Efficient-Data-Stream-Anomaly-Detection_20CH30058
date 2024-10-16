import matplotlib.pyplot as plt
import numpy as np

def plot_real_time(stream, detector, save_plot=False, output_file="anomaly_plot.png"):
    """
    Plots the data stream and highlights anomalies in real-time.
    
    Parameters:
    - stream: The data stream generator.
    - detector: The anomaly detection generator.
    - save_plot: Boolean to save the plot as an image.
    - output_file: Filename to save the plot if save_plot is True.
    """
    plt.ion()  # Enable interactive mode for real-time plotting
    fig, ax = plt.subplots(figsize=(12, 6))  # Create a new figure and axis for plotting with specified size
    x_data, y_data = [], []  # Initialize lists to hold x and y data points
    anomaly_count = 0  # Initialize anomaly count

    # Use detector directly without passing stream again
    for i, (value, anomalies) in enumerate(detector):
        x_data.append(i)  # Append the index as x value
        y_data.append(value)  # Append the current data point as y value

        ax.clear()  # Clear the plot to update with new data
        
        # Set plot title and labels
        ax.set_title("Real-Time Data Stream with Anomaly Detection", fontsize=16, fontweight='bold')
        ax.set_xlabel("Time Step", fontsize=14)
        ax.set_ylabel("Data Value", fontsize=14)
        
        # Plot the data stream
        ax.plot(x_data, y_data, label='Data Stream', color='blue', linewidth=2)  # Set line width for clarity
        ax.grid(True, linestyle='--', alpha=0.5)  # Add grid lines for better readability

        # Highlight anomalies if any are detected
        if anomalies:  # Check if any anomalies were detected
            ax.scatter([i] * len(anomalies), anomalies, color='red', label='Anomalies', s=80, edgecolor='black', zorder=5)  # Highlight anomalies
            anomaly_count += len(anomalies)  # Increment the anomaly count

        # Display the number of detected anomalies in the upper right corner
        ax.text(0.98, 0.95, f"Anomalies Detected: {anomaly_count}", transform=ax.transAxes,
                fontsize=12, verticalalignment='top', horizontalalignment='right', 
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray'))  # Position text in upper right corner
        
        # Customize ticks
        ax.tick_params(axis='both', which='major', labelsize=12)  # Set tick label size

        ax.legend(loc='upper left', fontsize=12)  # Show the legend on the plot

        plt.draw()  # Draw the updated plot
        plt.pause(0.01)  # Short pause to create a real-time effect

    plt.ioff()  # Turn off interactive mode when finished
    plt.show()  # Display the final plot

    # Option to save the plot
    if save_plot:  # Check if saving the plot is requested
        fig.savefig(output_file, bbox_inches='tight')  # Save the figure to the specified output file
        print(f"Plot saved as {output_file}")  # Print confirmation of saving the plot
