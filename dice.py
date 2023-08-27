import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

probe_amount = int(input("Set amount of probe: "))
probe_units = [random.randrange(1, 7) for i in range(probe_amount)]
probe_group, probe_group_size = np.unique(probe_units, return_counts=True)

probe_str = f'{probe_amount:,}'.replace('.', ' ')
chart_name = f'Frequency of the number of points after {probe_str} throws of the dice'
sns.set_style('whitegrid')
axes = sns.barplot(x=probe_group, y=probe_group_size, palette="bright")
axes.set_title(chart_name)
axes.set(xlabel="Number of dots", ylabel="Frequency")
axes.set_ylim(top=max(probe_group_size)* 1.10)

for bar, probe_dice_amount in zip(axes.patches, probe_group_size):
    legend_x = bar.get_x() + bar.get_width() / 2.0
    legend_y = bar.get_height()
    proce_dice_amount_str = f'{probe_dice_amount:,}'.replace('.', ' ')
    summary = f'{proce_dice_amount_str}\n{probe_dice_amount/probe_amount:.3%}'.replace('.', ',')
    axes.text(legend_x, legend_y, summary, fontsize=9, ha='center', va='bottom')

plt.show()

# print('probe amount: ', probe_amount)
# print('probe units: ', probe_units)
# print('probe group: ', probe_group)
# print('probe group size: ', probe_group_size)

