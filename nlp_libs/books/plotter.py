import matplotlib.pyplot as plt

import seaborn as sns

SMALL_SIZE = 14
MEDIUM_SIZE = 16
BIGGER_SIZE = 20

plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


def plot_differences(custom, pretrained, title, distance='cosine'):
    if distance == 'cosine':
        metric = 'cosineSim'
    else:
        metric = 'dotSim'
    fig, axes = plt.subplots(2, 2, figsize=(15, 15), facecolor='w')
    fig.suptitle(f'Comparison Statistics for {title}')
    pretrained['vectorSize'] = pretrained['model_name'].apply(lambda x: int(x.split('-')[-1]))

    axis = axes[0, 0]
    customStd = custom.groupby(['vectorSize']).agg(['mean', 'std', 'min', 'max'])[metric][['std']]
    sns.lineplot(ax=axis, x='vectorSize', y='std', data=customStd)
    axis.set_title('Custom Std', size=20)

    axis = axes[0, 1]
    preStd = pretrained.groupby(['vectorSize']).agg(['mean', 'std', 'min', 'max'])[metric][
        ['std']]
    sns.lineplot(ax=axis, x='vectorSize', y='std', data=preStd)
    axis.set_title('Pretrained Std', size=20)

    axis = axes[1, 0]
    sns.violinplot(ax=axis, x='vectorSize', y=metric, data=custom)
    axis.set_title('Custom Violin', size=20)

    axis = axes[1, 1]
    sns.violinplot(ax=axis, x='vectorSize', y=metric, data=pretrained)
    axis.set_title('Pretrained Violin', size=20)
