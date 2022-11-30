# Import standard libraries
import pandas as pd
import plotly.express as px

df = pd.read_csv('plot.csv').dropna()

Clusters = \
    {
        4: 'Cluster 4',
        5: 'Cluster 5',
        6: 'Cluster 6',
        7: 'Cluster 7',
        1: 'Cluster 1',
        2: 'Cluster 2',
        3: 'Cluster 3',

    }
color_set_3 = \
    [
        "#005F73",
        "#A88860",
        "#EE9B00",
        "#BB3E03",
        "#94D2BD",
        "#9B2226",
        "#0A9396",

    ]
fig = px.scatter(
    df,
    x='PC 1',
    y='PC 2',
    color=df['cluster'].map(Clusters),
    range_x=[-6.5, 25],
    range_y=[-6.5, 6.5],
    color_discrete_sequence=color_set_3,
    # template='seaborn',
    # labels={"cluster": "Clusters"},
    width=840,
    height=600

)
fig.for_each_trace(lambda t: t.update(name=t.name.split("=")[-1]))
fig.update_layout(legend_title_text='')
fig.update_traces(marker=dict(size=9), row=0,
                  col=0,
                  selector=dict(mode='markers'))
fig.update_layout(legend=dict(
    yanchor="bottom",
    x=0.997,
    xanchor="right",
    y=0.041,
    font=dict(
        family="Courier",
        size=12,
        color="black"
    ),

))

fig.update_xaxes(zeroline=True, zerolinewidth=1.5, zerolinecolor='black')
fig.update_yaxes(zeroline=True, zerolinewidth=1.5, zerolinecolor='black')
fig.show()

import os

if not os.path.exists("images"):
    os.mkdir("images")
import plotly.io as pio

pio.write_image(fig, 'images/clust_1_5_column.svg', width=900, height=600, scale=3)
pio.write_image(fig, 'images/clust_1_5_column.png', width=900, height=600, scale=3)

pio.write_image(fig, 'images/clust_1_column.svg', width=600, height=600, scale=3)
pio.write_image(fig, 'images/clust_1_column.png', width=600, height=600, scale=3)
print('done')
#  make sure that the X and Y axis indicator are at least 8
# legend below plot
# smaller dots.
