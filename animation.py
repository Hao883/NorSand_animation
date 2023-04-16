import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load CSV file into a pandas dataframe
df = pd.read_csv('data.csv')

# Set x and y column names
x_col = 'D'
y_col = 'eta'

# Create figure and axis
fig, ax = plt.subplots()

# Define function to update plot for each frame of the animation
def update(i):
    ax.clear()
    ax.plot(df[x_col][:i], df[y_col][:i])
    ax.set_xlim([df[x_col].min(), df[x_col].max()])
    ax.set_ylim([df[y_col].min(), df[y_col].max()])
    plt.xlabel('Dilatancy')
    plt.ylabel("Stress ratio \u03B7")
# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(df), interval=100, blit=False)

# Save animation as GIF
ani.save('Eta-D.gif', writer='imagemagick')

# Set x and y column names
x_col2 = 'Axial strain'
y_col2 = 'q'

# Create figure and axis
fig, ax = plt.subplots()

# Define function to update plot for each frame of the animation
def update(i):
    ax.clear()
    ax.plot(df[x_col2][:i], df[y_col2][:i])
    ax.set_xlim([df[x_col2].min(), df[x_col2].max()])
    ax.set_ylim([df[y_col2].min(), df[y_col2].max()])
    plt.xlabel('Axial Strain (%)')
    plt.ylabel("Deviator Stress (kPa)")
# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(df), interval=100, blit=False)

# Save animation as GIF
ani.save('q-ep.gif', writer='imagemagick')

# Set x and y column names
x_col3 = 'psi'
y_col3 = 'q'

# Create figure and axis
fig, ax = plt.subplots()

# Define function to update plot for each frame of the animation
def update(i):
    ax.clear()
    ax.plot(df[x_col3][:i], df[y_col3][:i])
    ax.set_xlim([df[x_col3].min(), df[x_col3].max()])
    ax.set_ylim([df[y_col3].min(), df[y_col3].max()])
    plt.xlabel('State parameter')
    plt.ylabel("Deviator Stress (kPa)")
# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(df), interval=100, blit=False)

# Save animation as GIF
ani.save('psi-q.gif', writer='imagemagick')

# Set x and y column names
x_col4 = 'Axial strain'
y_col4 = 'Vol strain'

# Create figure and axis
fig, ax = plt.subplots()

# Define function to update plot for each frame of the animation
def update(i):
    ax.clear()
    ax.plot(df[x_col4][:i], df[y_col4][:i])
    ax.set_xlim([df[x_col4].min(), df[x_col4].max()])
    ax.set_ylim([df[y_col4].min(), df[y_col4].max()])
    plt.ylabel('Volumetric strain (%)')
    plt.xlabel("Axial Strain (%)")
# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(df), interval=100, blit=False)

# Save animation as GIF
ani.save('epV-epi.gif', writer='imagemagick')