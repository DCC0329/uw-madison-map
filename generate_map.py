import prettymaps
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

plot = prettymaps.plot(
    'University of Wisconsin-Madison, Madison, WI, USA',
    radius=1000,
    circle=True,
    figsize=(12, 12),
    layers={
        'streets': {
            'width': {
                'motorway': 5,
                'trunk': 5,
                'primary': 4,
                'secondary': 3,
                'tertiary': 2,
                'residential': 1,
                'service': 0.8,
                'footway': 0.5,
                'path': 0.5,
            }
        },
        'building': {'tags': {'building': True}},
        'water': {'tags': {'natural': 'water', 'water': True, 'waterway': True}},
        'green': {
            'tags': {
                'landuse': 'grass',
                'natural': ['island', 'wood'],
                'leisure': 'park',
            }
        },
        'forest': {'tags': {'landuse': 'forest'}},
    },
    style={
        'background': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'hatch': 'ooo...', 'zorder': -1},
        'perimeter': {'fc': '#F2F4CB', 'ec': '#dadbc1', 'lw': 0, 'hatch': 'ooo...', 'zorder': 0},
        'green': {'fc': '#D0F1BF', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'forest': {'fc': '#64B96A', 'ec': '#2F3737', 'lw': 1, 'zorder': 1},
        'water': {'fc': '#a1e3ff', 'ec': '#2F3737', 'lw': 1, 'zorder': 3},
        'streets': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'zorder': 4},
        'building': {'palette': ['#FFC857', '#E9724C', '#C5283D'], 'ec': '#2F3737', 'lw': 0.5, 'zorder': 5},
    },
    use_preset=False,
    show=False,
    credit={'text': 'University of Wisconsin–Madison  |  prettymaps', 'x': 0, 'y': -20},
)

plot.ax.set_title('University of Wisconsin–Madison',
                  fontsize=22, fontweight='bold',
                  color='#2F3737', pad=15, fontfamily='serif')

plot.fig.savefig('uw_madison_map.png', dpi=150, bbox_inches='tight',
                 facecolor='#F2F4CB')
print("地图已保存为 uw_madison_map.png")
