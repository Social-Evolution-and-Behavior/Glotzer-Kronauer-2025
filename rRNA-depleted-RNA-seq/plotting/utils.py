import matplotlib.pyplot as plt

def black_plotting():
    # Set figure and axis backgrounds to black
    plt.rcParams['figure.facecolor'] = 'black'
    plt.rcParams['axes.facecolor'] = 'black'
    plt.rcParams['savefig.facecolor'] = 'black'  # For saved figures

    # Set tick, label, and title colors to white
    plt.rcParams['axes.edgecolor'] = 'white'
    plt.rcParams['axes.labelcolor'] = 'white'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'
    plt.rcParams['axes.titlecolor'] = 'white'
    
    # Set general text color to white
    plt.rcParams['text.color'] = 'white'
    
    # Turn off grid lines by default
    plt.rcParams['axes.grid'] = False

    # Set legend background and text color
    plt.rcParams['legend.facecolor'] = 'black'
    plt.rcParams['legend.edgecolor'] = 'white'
    plt.rcParams['legend.labelcolor'] = 'white'
    plt.rcParams['legend.fontsize'] = 'medium'
    



def white_plotting():
    # Set figure and axis backgrounds to white
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['savefig.facecolor'] = 'white'  # For saved figures

    # Set tick, label, and title colors to black
    plt.rcParams['axes.edgecolor'] = 'black'
    plt.rcParams['axes.labelcolor'] = 'black'
    plt.rcParams['xtick.color'] = 'black'
    plt.rcParams['ytick.color'] = 'black'
    plt.rcParams['axes.titlecolor'] = 'black'
    
    # Set general text color to black
    plt.rcParams['text.color'] = 'black'
    
    # Turn off grid lines by default
    plt.rcParams['axes.grid'] = False

    # Set legend background and text color to fit light theme
    plt.rcParams['legend.facecolor'] = 'white'
    plt.rcParams['legend.edgecolor'] = 'black'
    plt.rcParams['legend.labelcolor'] = 'black'
    plt.rcParams['legend.fontsize'] = 'medium'
    

    