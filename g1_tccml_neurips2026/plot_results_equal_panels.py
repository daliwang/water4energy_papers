#!/usr/bin/env python3
"""Equal-size two-panel scoreboard for the TCCML revision (not G1/IEEE labels)."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figures" / "results_equal_panels.png"

HIT_C = "#1f4e79"
HEIDKE_C = "#6baed6"
CHANCE = 1.0 / 3.0

# Shared x-order so bar width is identical in both panels.
# Cool/hot has no CFSv2 score; that slot is left empty.
XLABELS = [
    "Clim.\nmajority",
    "CFSv2",
    "Logistic",
    "FC",
    "LSTM",
    "CNN",
    "Residual\nTransformer",
]

# Wet/dry (Table 1 / IEEE scoreboard)
HIT_WD = np.array([0.333, 0.467, 0.667, 0.667, 0.400, 0.333, 0.667])
HSS_WD = np.array([0.000, 0.111, 0.432, 0.432, 0.100, 0.057, 0.432])

# Cool/hot: majority = chance; CFSv2 not scored
HIT_CH = np.array([0.333, np.nan, 0.400, 0.333, 0.267, 0.267, 0.467])
HSS_CH = np.array([0.000, np.nan, 0.167, 0.112, 0.046, 0.000, 0.195])


def grouped_bars(ax, hit, hss, *, title: str, show_ylabel: bool, show_legend: bool) -> None:
    x = np.arange(len(XLABELS), dtype=float)
    w = 0.36

    def draw(vals, offset, color):
        ok = np.isfinite(vals)
        bars = ax.bar(
            x[ok] + offset,
            vals[ok],
            w,
            color=color,
            edgecolor="none",
            zorder=3,
        )
        for rect, val in zip(bars, vals[ok]):
            ax.text(
                rect.get_x() + rect.get_width() / 2,
                rect.get_height() + 0.018,
                f"{val:.2f}",
                ha="center",
                va="bottom",
                fontsize=6.2,
                color="0.15",
            )

    draw(hit, -w / 2, HIT_C)
    draw(hss, +w / 2, HEIDKE_C)
    ax.axhline(CHANCE, color="0.45", ls=":", lw=0.9, zorder=2)
    ax.axhline(0.0, color="0.75", ls="-", lw=0.5, zorder=1)

    for i, val in enumerate(hit):
        if not np.isfinite(val):
            ax.text(x[i], 0.04, "n/a", ha="center", va="bottom", fontsize=6.5, color="0.45")

    ax.set_xticks(x)
    ax.set_xticklabels(XLABELS)
    ax.set_xlim(-0.72, len(XLABELS) - 0.28)
    ax.set_ylim(0.0, 0.82)
    ax.set_yticks(np.arange(0.0, 0.81, 0.2))
    ax.set_title(title, pad=4, loc="left", fontweight="bold")
    if show_ylabel:
        ax.set_ylabel("Score")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(length=3, pad=2)
    ax.yaxis.grid(True, ls=":", lw=0.5, color="0.85", zorder=0)
    ax.set_axisbelow(True)
    if show_legend:
        ax.legend(
            handles=[
                Patch(facecolor=HIT_C, label="Hit rate"),
                Patch(facecolor=HEIDKE_C, label="Heidke skill"),
                plt.Line2D([0], [0], color="0.45", ls=":", lw=0.9, label="Chance (hit)"),
            ],
            loc="upper left",
            frameon=False,
            borderaxespad=0.2,
            handlelength=1.4,
            handleheight=0.7,
        )


def main() -> None:
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["DejaVu Sans", "Helvetica", "Arial"],
            "font.size": 8,
            "axes.titlesize": 8.5,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "savefig.dpi": 300,
        }
    )
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(7.20, 3.05),
        sharey=True,
        gridspec_kw={"wspace": 0.10},
    )
    grouped_bars(
        axes[0],
        HIT_WD,
        HSS_WD,
        title="(a) Winter wet/dry",
        show_ylabel=True,
        show_legend=True,
    )
    grouped_bars(
        axes[1],
        HIT_CH,
        HSS_CH,
        title="(b) Winter cool/hot",
        show_ylabel=False,
        show_legend=False,
    )
    fig.subplots_adjust(left=0.07, right=0.995, top=0.90, bottom=0.22)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=300, facecolor="white")
    plt.close(fig)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
