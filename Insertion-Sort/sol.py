import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def sol():
    with open('data.txt') as f:
        content = f.read().split(" ")
        content = [6, 10, 4, 5, 1, 2]
        count = 0
        for i in range(2, 6):
            k = i
            while k > 0 and content[k] < content[k-2]:
                count += 1
                content[k], content[k-2] = content[k-2], content[k]
                k -= 2


        print(count)


def graph():

    # Generate sample data for sinusoidal waves
    wavelengths = np.linspace(400, 700, 1000)  # Visible light spectrum (400-700 nm)
    intensities1 = 0.5 * np.sin(2 * np.pi * wavelengths / 100) + 0.5
    intensities2 = 0.3 * np.sin(2 * np.pi * wavelengths / 50) + 0.5

    # Create the wavelength graph
    plt.figure(figsize=(10, 6), facecolor='black')
    plt.style.use('dark_background')
    plt.plot(wavelengths, intensities1, label='Wave 1', color='#00ff00')
    plt.plot(wavelengths, intensities2, label='Wave 2', color='#00ff00')
    plt.title('Sinusoidal Waves', color='#00ff00')
    plt.xlabel('Wavelength (nm)', color='#00ff00')
    plt.ylabel('Intensity', color='#00ff00')
    plt.grid(True, color='#003300')

    # Add some visual enhancements
    plt.fill_between(wavelengths, intensities1, alpha=0.1, color='#00ff00')
    plt.fill_between(wavelengths, intensities2, alpha=0.1, color='#00ff00')

    plt.legend(facecolor='black', edgecolor='#00ff00', labelcolor='#00ff00')
    plt.tick_params(colors='#00ff00')
    plt.tight_layout()
    plt.show()


def plot_spherical_waves():


    # Generate sample data for spherical waves
    r = np.linspace(0, 10, 100)
    theta = np.linspace(0, 2*np.pi, 100)
    r, theta = np.meshgrid(r, theta)

    # Calculate intensity (assuming 1/r^2 falloff)
    intensity = 1 / (r**2 + 1)  # Adding 1 to avoid division by zero

    # Create the spherical wave plot
    fig, ax = plt.subplots(subplot_kw=dict(projection='polar'), figsize=(10, 8), facecolor='black')
    plt.style.use('dark_background')

    # Plot the intensity as a heatmap
    c = ax.pcolormesh(theta, r, intensity, cmap='viridis', shading='auto')
    
    # Customize the plot
    ax.set_title('Spherical Wave Intensity', color='#00ff00')
    ax.set_rticks([2, 4, 6, 8])  # Less radial ticks for clarity
    ax.tick_params(colors='#00ff00')
    
    # Add a colorbar
    cbar = fig.colorbar(c, ax=ax, pad=0.1)
    cbar.set_label('Intensity', color='#00ff00')
    cbar.ax.yaxis.set_tick_params(color='#00ff00')
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#00ff00')

    plt.tight_layout()
    plt.show()




def plot_3d_altitude_model():
   

    # Generate random data for altitude model
    x = np.random.uniform(-5, 5, (100, 100))
    y = np.random.uniform(-5, 5, (100, 100))
    
    # Create a random altitude model
    z = np.random.uniform(-1, 1, (100, 100))

    # Create the 3D plot
    fig = plt.figure(figsize=(10, 8), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the surface
    surf = ax.plot_surface(x, y, z, cmap='terrain', edgecolor='none', alpha=0.8)
    
    # Customize the plot
    ax.set_title('Random 3D Altitude Model', color='#00ff00')
    ax.set_xlabel('X', color='#00ff00')
    ax.set_ylabel('Y', color='#00ff00')
    ax.set_zlabel('Altitude', color='#00ff00')
    
    # Set background color
    ax.set_facecolor('black')
    
    # Customize tick colors
    ax.tick_params(axis='x', colors='#00ff00')
    ax.tick_params(axis='y', colors='#00ff00')
    ax.tick_params(axis='z', colors='#00ff00')
    
    # Add a color bar
    cbar = fig.colorbar(surf, ax=ax, pad=0.1)
    cbar.set_label('Altitude', color='#00ff00')
    cbar.ax.yaxis.set_tick_params(color='#00ff00')
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#00ff00')

    plt.tight_layout()
    plt.show()

# Call the function to display the 3D altitude model
graph()
