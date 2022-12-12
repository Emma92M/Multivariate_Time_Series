#%%
from cos import make_random_grid
from main import transpose, get_perpendicular, random_matrix

from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objects as go
import numpy as np
import pandas as pd

data = pd.read_csv('/Users/emmaminasyan/Downloads/onsample_sep1.csv')

column = ['longitute','latitude']
df_1 = data[column]

grid = np.array(df_1)


print(grid)
# #print(grid)
# #%%
# grid1, _ = make_random_grid(40, 40)
# #print(grid1)
# #%%
fig = go.Figure(data=go.Scatter(x=[a[0] for a in grid], y=[a[1] for a in grid], mode='markers'))
# # #%%
fig.show()
# # #%%
new_grid, rot_mat=transpose(grid)
np.savetxt("/Users/emmaminasyan/Downloads/new_grid.csv", new_grid, delimiter=",")
#print(new_grid)


fig = go.Figure()
# # #
# # # # Add traces

fig.add_trace(go.Scatter(x=[a[0] for a in new_grid], y=[a[1] for a in new_grid], mode='markers', name='grid'))
fig.show()
# # # #%%
# # # #rot_mat
# # #%%

first, second, first_perp, second_perp, center = get_perpendicular(grid)

print('First', first)
print('Second', second)
print("first perp", first_perp)
print('Second Perp',second_perp)
print('centre', center)