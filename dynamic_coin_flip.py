
"""Dynamically graphing frequencies of coin flips."""
from matplotlib import animation
import matplotlib.pyplot as plt
import random 
import seaborn as sns
import sys

def update(frame_number, rolls, faces, frequencies):
    """Configures bar plot contents for each frame."""
    # roll die and update frequencies
    for i in range(rolls):
        frequencies[random.randrange(1, 3) - 1] += 1 

    # reconfigure plot for updated coin flip frequencies
    plt.cla()  # clear old contents contents of current Figure
    axes = sns.barplot(faces, frequencies, palette='bright')  # new bars
    axes.set_title(f'Coin Flip Heads vs. Tails for {sum(frequencies):,} tosses')
    axes.set(xlabel='Coin Side', ylabel='Frequency')  
    axes.set_ylim(top=max(frequencies) * 1.10)  # scale y-axis by 10%

    # display frequency & percentage above each patch (bar)
    for bar, frequency in zip(axes.patches, frequencies):
        text_x = bar.get_x() + bar.get_width() / 2.0  
        text_y = bar.get_height() 
        text = f'{frequency:,}\n{frequency / sum(frequencies):.4%}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')

# read command-line arguments for number of frames and flips per frame
number_of_frames = int(sys.argv[1])  
rolls_per_frame = int(sys.argv[2])  

# white background with gray grid lines
sns.set_style('whitegrid')  
# Figure for animation
figure = plt.figure('Rolling a Fair Coin')  
# coin flips (1 Head, 2 Tails) for display on x-axis
values = ['Heads', 'Tails']  
frequencies = [0] * 2  # list of coin frequencies

# configure and start animation that calls function update
die_animation = animation.FuncAnimation(
    figure, update, repeat=False, frames=number_of_frames, interval=33,
    fargs=(rolls_per_frame, values, frequencies))

plt.show()  # display window