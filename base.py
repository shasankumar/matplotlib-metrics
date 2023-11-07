import matplotlib.pyplot as plt
import numpy as np

def read_metrics(file_path):
    metrics = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            if parts[0] != 'Entity':
                entity = parts[0]
                p, r, f1, tp, fp, fn = map(float, parts[1:])
                metrics[entity] = {'p': p, 'r': r, 'f1': f1, 'tp': tp, 'fp': fp, 'fn': fn}
    return metrics


metrics1 = read_metrics('metrics1.txt')
metrics2 = read_metrics('metrics2.txt')

total_metrics1 = metrics1['Totals']
total_metrics2 = metrics2['Totals']

species = ("P", "R", "F1")
penguin_means = {
    'Bill Depth': (0.9064, 0.9064, 0.9064),
    'Bill Length': (0.8064, 0.7064, 0.8064),
    #'Flipper Length': (189.95, 195.82, 217.19),
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 2)

plt.show()