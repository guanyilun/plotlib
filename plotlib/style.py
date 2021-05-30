_styles = {
    'default': {
        'font.size'       : 12,
        'font.family'     : 'serif',
        'text.usetex'     : True,
        'figure.figsize'  : (6,4),
        'figure.dpi'      : 180,
        'xtick.direction' : 'in',
        'ytick.direction' : 'in',
        'xtick.top'       : True,
        'ytick.right'     : True,
        'cycle'           : 'classic',
        'lines.linewidth' : 1,
    }
} 

def use(style):
    import matplotlib as mpl
    from cycler import cycler
    if style in _styles:
        rules = _styles[style]
        for k, v in rules.items():
            # some keys that need special treatment
            if k == 'cycle':
                from .color import colors
                if v in colors:
                    color = colors[v]
                    mpl.rcParams['axes.prop_cycle'] = cycler(color=color)
            else:
                mpl.rcParams[k] = v
    else:  # if style is not font
        plt.style.use(style)

def use_cycler(c):
    from cycler import cycler
    from .color import colors
    if c in colors:
        color = colors[v]
        mpl.rcParams['axes.prop_cycle'] = cycler(color=color)
