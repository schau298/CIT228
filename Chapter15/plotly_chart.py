import plotly.graph_objects as go
from plotly import offline
labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'Other'
used_at_sites = [376, 348, 153, 104, 19]
explode = (.25, 0, 0, 0, 0)  # only "explode" the 1st wedge
wedgeColors=('lightblue','lightyellow','lightpink','orange','lightgrey')

fig = go.Figure(data=[go.Pie(labels=labels, values=used_at_sites)])
fig.update_traces(
    hoverinfo='label+percent',
    textinfo='value',
    textfont_size=15, 
    marker=dict(colors=wedgeColors,line=dict(color='black',width=3))
    )
layout=fig.update_layout(
    title_text="Popular Graphics Files Across the Web",
    title_font_color="red", 
    title_font_size=35, 
    title_font_family="Arial", 
    title_xref="paper", 
    title_yref="paper",
    margin_l=150,
    margin_r=150
    )
#fig.show()

offline.plot({'data': fig, 'layout':layout}, filename='plotly.html')