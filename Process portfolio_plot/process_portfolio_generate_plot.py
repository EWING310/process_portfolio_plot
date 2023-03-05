import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import json

with open('data_process_portfolio.json') as f:
    data = json.load(f)

processes = data['processes']

importance = [process['Importance'] for process in processes]
health = [process['Health'] for process in processes]
feasibility = [process['Feasibility'] for process in processes]
names = [process['name'] for process in processes]

fig, ax = plt.subplots()

colors = ['black' if x <= 33 else 'silver' if x <= 66 else 'whitesmoke' for x in feasibility]

ax.scatter(health, importance, s=200, c=colors, edgecolor='black')

ax.set_xlabel('Health (Poor to Good)')
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xticklabels(['Poor', '',"", '', 'Good'])

ax.set_ylabel('Importance (Low to High)')
ax.set_yticks([0, 25, 50, 75, 100])
ax.set_yticklabels(['Low', '',"", '', 'High'])

# Adding the quadrant lines
plt.plot([50,50],[0,100], linewidth=0.5, color='black' )
plt.plot([0,100],[50,50], linewidth=0.5, color='black' )

for i, name in enumerate(names):
    if health[i] > 20 and importance[i] > 50:
        ax.annotate(name, (health[i] + 2, importance[i] + 3))
    elif health[i] > 20 and importance[i] < 50:
        ax.annotate(name, (health[i] + 2, importance[i] - 3))
    elif health[i] < 20 and importance[i] > 50:
        ax.annotate(name, (health[i] - 30, importance[i] + 3))
    else:
        ax.annotate(name, (health[i] - 13, importance[i] - 10))


black_patch = mpatches.Patch(color='black', label='Low:')
silver_patch = mpatches.Patch(color='silver', label='Medium')
whitesmoke_patch = mpatches.Patch(color='whitesmoke', label='High')

plt.legend(handles=[black_patch, silver_patch, whitesmoke_patch], loc='lower right')

plt.title("Selection Focus", x=0, y=100, fontsize=12, fontweight='bold')

plt.show()
