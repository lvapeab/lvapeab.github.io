# Modified from https://github.com/neulab/compare-mt/blob/master/compare_mt/reporters.py

import matplotlib

from argparse import ArgumentParser
matplotlib.use('agg')
from matplotlib import pyplot as plt

plt.rcParams['font.family'] = 'sans-serif'
import numpy as np
import os

import logging as log

log.basicConfig(level=log.INFO)

# Global variables used by all reporters. These are set by compare_mt_main.py
fig_size = None



fig_counter, tab_counter = 0, 0
bar_colors = ["#7293CB", "#E1974C", "#84BA5B", "#D35E60", "#808585", "#9067A7", "#AB6857", "#CCC210"]



def get_parser() -> ArgumentParser:
    parser = ArgumentParser()
    # Model Parameters
    parser.add_argument('--datas', action='store', type=str, dest='datas', nargs='+')
    parser.add_argument('--tags', action='store', type=str, dest='tags')
    parser.add_argument('--output', action='store', dest='output_file', type=str)
    return parser

def make_bar_chart(datas,
                   output_directory, output_fig_file, output_fig_format='pdf', sys_names=None,
                   errs=None, title=None, xlabel=None, xticklabels=None, ylabel=None):
    sys_names = sys_names or ['Adaptive', 'Static']
    fig, ax = plt.subplots(figsize=fig_size)
    ind = np.arange(len(datas[0]))
    width = 0.7 / len(datas)
    bars = []
    for i, data in enumerate(datas):
        err = errs[i] if errs != None else None
        bars.append(ax.bar(ind + i * width, data, width, color=bar_colors[i], bottom=0, yerr=err))
    # Set axis/title labels
    if title is not None:
        ax.set_title(title)
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    if xticklabels is not None:
        ax.set_xticks(ind + width / 2)
        ax.set_xticklabels(xticklabels)
        plt.xticks(rotation=70)
    else:
        ax.xaxis.set_visible(False)

    ax.legend(bars, sys_names)
    ax.autoscale_view()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    out_file = os.path.join(output_directory, f'{output_fig_file}.{output_fig_format}')
    plt.savefig(out_file, format=output_fig_format, bbox_inches='tight')


if __name__ == '__main__':
    parser = get_parser().parse_args()
    datas = []
    for filename in parser.datas:
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
            data = [float(x) for x in lines]
            datas.append(data)

    with open((parser.tags), 'r') as f:
        xlabels = f.read().splitlines()

    make_bar_chart(datas,
                   './',
                   parser.output_file,
                   xlabel="BLEU",
                   ylabel='Count',
                   xticklabels=xlabels,
    )