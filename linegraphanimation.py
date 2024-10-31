import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Load the data from the CSV file
df = pd.read_csv('data.csv')
df['Time'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Months'])

# Drop Year and Months columns as they are now part of Time
df.drop(['Year', 'Months'], axis=1, inplace=True)
df.set_index('Time', inplace=True)

# Set up the figure and axis
fig, ax = plt.subplots()
lines = {col: ax.plot([], [], label=col)[0] for col in df.columns}

# Initialize the line plot
def init():
    ax.set_xlim(df.index.min(), df.index.max())
    ax.set_ylim(df.min().min() - 5, df.max().max() + 5)
    for line in lines.values():
        line.set_data([], [])
    ax.legend(loc='upper left')
    return lines.values()

# Update function for animation
def update(frame):
    for col, line in lines.items():
        line.set_data(df.index[:frame], df[col][:frame])
    return lines.values()

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=len(df), init_func=init, blit=True, interval=200
)

# Save the animation as a video file
ani.save('programming_languages_trend_animation.mp4', writer='ffmpeg', fps=30)

# Display the plot
plt.xlabel('Time')
plt.ylabel('Popularity')
plt.title('Programming Languages Popularity Over Time')
plt.show()
