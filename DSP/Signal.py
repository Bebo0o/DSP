import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def plot_signals(frequency,start_time,End_time):
    
    # Parameters for the signals
    # frequency = 5  # Frequency in Hz
    # start_time = 0  # Minimum time value
    # End_time = 1  # Maximum time value
    sample_rate = 1000  # Continuous sample rate (high)
    discrete_sample_rate = 10  # Discrete sample rate (low)

    # Generate time values for continuous signal
    t_continuous = np.linspace(start_time, End_time, sample_rate)
    
    # Generate time values for discrete signal
    t_discrete = np.linspace(start_time, End_time, discrete_sample_rate)

    # Generate continuous signal (sin wave)
    continuous_signal = np.sin(2 * np.pi * frequency * t_continuous)

    # Generate discrete signal (sampled sin wave)
    discrete_signal = np.sin(2 * np.pi * frequency * t_discrete)

    # Plot the continuous signal
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)  # 2 rows, 1 column, plot 1
    plt.plot(t_continuous, continuous_signal, label='Continuous Signal (Sin Wave)')
    plt.title('Continuous Signal')
    plt.xlabel('Time [sec]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend(loc='upper right')

    # Plot the discrete signal
    plt.subplot(2, 1, 2)  # 2 rows, 1 column, plot 2
    plt.stem(t_discrete, discrete_signal, label='Discrete Signal (Sampled Sin Wave)')
    plt.title('Discrete Signal')
    plt.xlabel('Time [sec]')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()

    # Show the plots
    plt.tight_layout()
    plt.show()


def sin(frequency,amplitude,start_time,End_time):
    # Parameters
    #frequency = 2  # Frequency of the sine wave
    #amplitude = 1  # Amplitude of the sine wave
    time = np.linspace(start_time, End_time, 1000)  # Time array from 0 to 2 seconds

    # Signal: sine wave
    signal = amplitude * np.sin( 2 * np.pi * frequency * time)
    
    # Plot the signal
    plt.plot(time, signal)
    plt.title("Sin Wave Signal")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()
    



def Squere_wave(frequency,amplitude,start_time,End_time):
    # Parameters
    #frequency = 2  # Frequency of the sine wave
    #amplitude = 1  # Amplitude of the sine wave
    time = np.linspace(start_time, End_time, 1000)  # Time array from 0 to 2 seconds
   
    # Signal: square wave
    wave = amplitude * signal.square(2 * np.pi * frequency * time)

    # Plot the signal
    plt.plot(time, wave)
    plt.title("Squere Wave Signal")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

def read_from_file(filename):
    # Lists to store the x and y values
    x_values = []
    y_values = []

    # Open and read the file
    with open(filename, 'r') as file:
        for line in file:
            # Split the line by the comma to get x and y values
            x, y = map(float, line.strip().split(','))
            x_values.append(x)
            y_values.append(y)

    # Plot the points
    plt.plot(x_values, y_values, 'o-', label="Data Points")

    # Add labels and title
    plt.title(f"Graph of Points from file")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

def Given_an_equation():
   
    # Get the equation from the user
    #equation_str = input("Enter an equation in terms of x : ")
    equation_str='x**2 - 4'
    # Define the equation function using eval
    def equation(x):
        return eval(equation_str)

    # Set the range for x values
    x_min = -10
    x_max = 10 
    num_points = 400  # Number of points to plot

    # Generate x values
    x = np.linspace(x_min, x_max, num_points)

    # Calculate y values based on the equation
    try:
        y = equation(x)
    except Exception as e:
        print(f"Error evaluating the equation: {e}")
        return

    # Plot the graph
    plt.plot(x, y, label=f"y = {equation_str}")

    # Add labels and title
    plt.title(f"Graph of y = {equation_str}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()


#####################################################################################################################################


#defolat valieo 
start_time=0
End_time=2
frequency=5
amplitude = 1

#draw output

plot_signals(frequency,start_time,End_time)

sin(frequency,amplitude,start_time,End_time)   

Squere_wave(frequency,amplitude,start_time,End_time) 

read_from_file("D:\DSP\points.txt.txt")

