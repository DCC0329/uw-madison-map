import prettymaps
import matplotlib

from matplotlib.patches import Circle
matplotlib.use('Agg')

plot = prettymaps.plot(
    '1220 Linden Dr, Madison, WI 53706',
    radius=2500,
    figsize=(12, 12),
    layers={
        'streets': {
            'width': {
                'motorway': 4,
                'trunk': 4,
                'primary': 3,
                'secondary': 2.5,
            }
        },
        'streets_small': {
            'custom_filter': '["highway"~"tertiary|residential|service|footway|path|cycleway|unclassified"]',
            'width': {
                'tertiary': 1,
                'residential': 0.6,
                'service': 0.4,
                'footway': 0.3,
                'path': 0.3,
                'cycleway': 0.3,
                'unclassified': 0.6,
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
        'streets_small': {'fc': '#2F3737', 'ec': '#475657', 'alpha': 1, 'zorder': 3},
        'building': {'palette': ['#FFC857', '#E9724C', '#C5283D'], 'ec': '#2F3737', 'lw': 0.5, 'zorder': 5},
    },
    use_preset=False,
    show=False,
    credit={'text': ''},
)

# 正圆裁切 + 黑色边框
ax = plot.ax
fig = plot.fig
xlim = ax.get_xlim()
ylim = ax.get_ylim()
cx = (xlim[0] + xlim[1]) / 2
cy = (ylim[0] + ylim[1]) / 2
r = min(xlim[1] - xlim[0], ylim[1] - ylim[0]) / 2 * 0.68

clip_circle = Circle((cx, cy), r, transform=ax.transData)
for collection in ax.collections:
    collection.set_clip_path(clip_circle)
for patch in ax.patches:
    patch.set_clip_path(clip_circle)
for line in ax.lines:
    line.set_clip_path(clip_circle)

# 黑色圆形边框
border = Circle((cx, cy), r, transform=ax.transData,
                fill=False, ec='#2F3737', lw=0.8, zorder=10)
ax.add_patch(border)

ax.set_title('University of Wisconsin–Madison',
             fontsize=22, fontweight='bold',
             color='#2F3737', pad=15, fontfamily='serif')

fig.savefig('uw_madison_map.png', dpi=150, bbox_inches='tight',
            facecolor='#F2F4CB')
print("地图已保存为 uw_madison_map.png")
