import matplotlib.pyplot as plt
import seaborn as sns
from typing import *

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


def make_space_above(axes, top_margin=1):
    """ Increase figure size to make top_margin (in inches) space for
        titles, without changing the axes sizes"""
    fig = axes.figure
    s = fig.subplotpars
    w, h = fig.get_size_inches()

    figh = h - (1 - s.top) * h + top_margin
    fig.subplots_adjust(bottom=s.bottom * h / figh, top=1 - top_margin / figh)
    fig.set_figheight(figh)
    return fig


def _plot_scores(tokens, scores, counts, title, base_c, min_score):
    """ Plot Scores"""

    fig, ax = plt.subplots(figsize=(21, 1))

    fig = make_space_above(ax, top_margin=7)
    fig.patch.set_facecolor('white')
    fig.patch.set_alpha(1.0)
    x_vals = [x + str(i) for i, x in enumerate(tokens)]
    counts = normalize(counts, 0.3, 1)
    colors = [(*base_c, c) for c in counts]
    edge_colors = [(*base_c, c) for c in counts]
    ax.tick_params(axis='both', which='minor', labelsize=29)
    ax.bar(x_vals, scores, color=colors, linewidth=1,
           edgecolor=edge_colors, label="Color intensity: Same Answer Count")
    # plt.colorbar(label="Same Answer Count", orientation="horizontal", ax=ax, mappable=bar)
    ax.set_title(title)
    ax.set_xlabel("Answers to successive windows")
    ax.set_ylabel("Confidence Score")
    limit_size = lambda x: x if len(x) < 17 else x[:15] + '(..)'
    tokens = [limit_size(token) for token in tokens]
    ax.set_xticks(ticks=[i for i in range(len(tokens))], labels=tokens,
                  fontsize=12, rotation=60, ha='right')
    if min_score > 0.05:
        y_min = min_score - 0.05
    else:
        y_min = min_score
    ax.set_ylim(y_min, 1.0)
    ax.legend()

    fig.tight_layout()
    fig.show()


def normalize(values, a, b):
    min_value = min(values)
    max_value = max(values)
    scores_norm = [(b - a) * (s - min_value) / (max_value - min_value) + a for s in values]
    return scores_norm


def clean_tokens(tokens):
    new_tokens = []
    for token in tokens:
        words = token.strip().split()
        words = [word.strip() for word in words]
        token = ' '.join(words)
        new_tokens.append(token)
    return new_tokens


def plot_scores(answers, title: str = '', min_score: float = 0.3, base_c: Tuple = None):
    if base_c is None:
        base_c = (0, 0, 1)
    # answers = [ for d in answers]
    _tokens = []
    _scores = []
    for answer in answers:
        _tokens.append(answer['answer'])
        _scores.append(answer['score'])
    _tokens = clean_tokens(_tokens)
    # filter tokens/scores
    tokens = []
    scores = []
    token_counts = []
    for t, s in zip(_tokens, _scores):
        c = _tokens.count(t)
        if s > min_score:
            tokens.append(t)
            scores.append(s)
            token_counts.append(c)

    _plot_scores(tokens=tokens, scores=scores, counts=token_counts, title=title,
                 base_c=base_c, min_score=min_score)
