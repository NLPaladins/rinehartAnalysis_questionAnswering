import matplotlib.pyplot as plt
import matplotlib.colors as plt_colors
import matplotlib.lines as mlines
import numpy as np


def create_locs_labels(book, suspects, perp, dets, co_ocs, crime):
    # divide the book into n chunks based on sentences
    total_sents = book.get_total_sentences()
    chapter_locs = []
    cum_sents = 0
    for chapter in book.clean:
        chapter_locs.append(cum_sents)
        cum_sents += len(chapter) - 2

    locs = []
    labels = []
    colors = []
    # other suspects
    for name, values in suspects.items():
        ch, sent_num, _ = values
        locs.append(chapter_locs[ch - 1] + sent_num)
        labels.append(name)
        colors.append('tab:blue')

    # perpetrator
    for name, values in perp.items():
        ch, sent_num, _ = values
        locs.append(chapter_locs[ch - 1] + sent_num)
        labels.append(name)
        colors.append('tab:red')

    # detective
    for name, values in dets.items():
        ch, sent_num, _ = values
        locs.append(chapter_locs[ch - 1] + sent_num)
        labels.append(name)
        colors.append('tab:green')

    # perp + det co-occurence
    for i, co_oc in enumerate(co_ocs):
        ch, sent_num, _, _ = co_oc
        locs.append(chapter_locs[ch - 1] + sent_num)
        labels.append(str(i + 1))
        colors.append('tab:orange')
    # crime occurence

    # add end of book
    locs.append(total_sents)
    labels.append('END')
    colors.append('tab:cyan')

    # sort
    idx = np.argsort(locs)
    locs = np.array(locs)[idx]
    labels = np.array(labels)[idx]
    colors = np.array(colors)[idx]

    return locs, labels, colors


def make_timeline(book, locs, labels, colors, title, num_x_labels=10, out_path=None):
    fig, ax = plt.subplots(figsize=(12, 5), tight_layout=True)

    total_sents = book.get_total_sentences()
    x_ticks = np.arange(1, total_sents + 1, int(total_sents / num_x_labels))
    x_labels = [str(int((pct) * 100 / num_x_labels)) + '%' for pct in range(num_x_labels + 1)]
    ax.set_title(f'Timeline: {title}', size=20)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, size=14)
    ax.get_yaxis().set_visible(False)

    # tiling the event heights with some nice levels
    levels = np.tile([-5, 5, -3, 3, -1, 1],
                     int(np.ceil(len(labels) / 6)))[:len(labels)]

    # plot the event lines
    markerline, stemline, baseline = ax.stem(locs, levels,
                                             linefmt="C3-", basefmt="k-",
                                             use_line_collection=True)

    # make the marker circle look nicer
    plt.setp(markerline, mec="k", mfc="w", zorder=3)
    # shift the markers to the baseline by replacing the y-data by zeros.
    markerline.set_ydata(np.zeros(len(labels)))

    # annotate chapters
    vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
    for sent_num, lv, label, va in zip(locs, levels, labels, vert):
        ax.annotate(label, xy=(sent_num, lv), xytext=(6.5 * len(label), np.sign(lv) * 3),
                    textcoords="offset points", va=va, ha="right", size=12)

    # set colors
    colors = [plt_colors.to_rgba(color) for color in colors]
    stemline.set_colors(colors)

    # legend
    legend_colors = ['tab:blue', 'tab:red', 'tab:green', 'tab:orange']
    legend_names = ['other suspects', 'perpetrator', 'detective', 'co-occurences']
    proxies = [mlines.Line2D([], [], color=legend_colors[i], marker='_',
                             markersize=15, label=legend_names[i]) for i in range(4)]
    fig.legend(handles=proxies, bbox_to_anchor=(1.0, 0.935), loc='upper left', fontsize=14)

    ax.margins(y=0.1)
    if out_path:
        plt.save(out_path, dpi=300)
    plt.show()
