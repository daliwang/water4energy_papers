#!/usr/bin/env python3
"""Figure 1: ERA5 monthly-mean precipitation with SST/index boxes and TVA target."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from netCDF4 import Dataset

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "figures" / "domain_indices_sst_tva.png"
NC = (
    Path("/Users/7xw/Documents/Work/Water4Energy/data/01_global_predictors")
    / "reanalysis/era5/daily_1deg_from_hourly/2024/12"
    / "era5_daily_sum_total_precipitation_202412_1deg_na_pac_atl.nc"
)

# lon in [-180, 180]
BOXES = [
    dict(name="Niño 3.4 / ONI", lon0=-170.0, lon1=-120.0, lat0=-5.0, lat1=5.0,
         ec="#00b4d8", ls="-", lw=2.0),
    dict(name="E. Pacific SST", lon0=-140.0, lon1=-90.0, lat0=-10.0, lat1=10.0,
         ec="#e85d04", ls="--", lw=1.8),
    dict(name="N. Atlantic SST", lon0=-80.0, lon1=0.0, lat0=0.0, lat1=60.0,
         ec="#2d6a4f", ls=":", lw=2.2),
]
TVA = dict(lon0=-90.5, lon1=-81.0, lat0=34.0, lat1=37.8)


def add_box(ax, lon0, lon1, lat0, lat1, ec, ls="-", lw=1.8, z=5):
    ax.add_patch(
        Rectangle(
            (lon0, lat0),
            lon1 - lon0,
            lat1 - lat0,
            fill=False,
            edgecolor=ec,
            linewidth=lw,
            linestyle=ls,
            zorder=z,
        )
    )


def add_label(ax, x, y, text, color, ha="center", va="center"):
    ax.text(
        x,
        y,
        text,
        color=color,
        fontsize=7,
        fontweight="bold",
        ha=ha,
        va=va,
        zorder=9,
        bbox=dict(boxstyle="round,pad=0.18", facecolor="white", edgecolor="none", alpha=0.88),
    )


def load_monthly_tp_mm_day(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    with Dataset(path) as ds:
        lat = np.asarray(ds.variables["latitude"][:], dtype=float)
        lon = np.asarray(ds.variables["longitude"][:], dtype=float)
        tp_m = np.asarray(ds.variables["tp"][:], dtype=float)  # m / day (daily sum)
    tp_mm = np.nanmean(tp_m, axis=0) * 1000.0
    return lon, lat, tp_mm


def main() -> None:
    lon, lat, tp = load_monthly_tp_mm_day(NC)
    lon2d, lat2d = np.meshgrid(lon, lat)

    fig, ax = plt.subplots(figsize=(7.2, 4.55), dpi=170)
    ax.set_facecolor("#ececec")
    ax.set_xlim(-180, 0)
    ax.set_ylim(-12, 70)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_xticks([-180, -150, -120, -90, -60, -30, 0])
    ax.set_xticklabels(["180°W", "150°W", "120°W", "90°W", "60°W", "30°W", "0°"])
    ax.set_yticks([-10, 0, 10, 20, 30, 40, 50, 60, 70])
    ax.set_yticklabels(["10°S", "Eq", "10°N", "20°N", "30°N", "40°N", "50°N", "60°N", "70°N"])
    ax.axhline(0.0, color="0.15", lw=0.7, ls=":", zorder=4)
    ax.grid(True, color="white", lw=0.45, alpha=0.35, zorder=3)

    pcm = ax.pcolormesh(
        lon2d,
        lat2d,
        tp,
        cmap="viridis",
        vmin=0.0,
        vmax=35.0,
        shading="nearest",
        zorder=2,
    )
    cbar = fig.colorbar(pcm, ax=ax, fraction=0.046, pad=0.02)
    cbar.set_label("mm day$^{-1}$")

    for b in BOXES:
        add_box(ax, b["lon0"], b["lon1"], b["lat0"], b["lat1"], b["ec"], b["ls"], b["lw"])
    add_box(ax, TVA["lon0"], TVA["lon1"], TVA["lat0"], TVA["lat1"], "#c1121f", "-", 2.2, z=6)

    add_label(ax, -145.0, 6.6, "Niño 3.4 / ONI", "#0077b6")
    add_label(ax, -115.0, -7.6, "E. Pacific SST", "#e85d04")
    add_label(ax, -40.0, 52.0, "N. Atlantic SST", "#2d6a4f")
    ax.annotate(
        "TVA",
        xy=(-85.75, 35.9),
        xytext=(-58, 22),
        fontsize=8,
        fontweight="bold",
        color="#c1121f",
        ha="center",
        arrowprops=dict(arrowstyle="-|>", color="#c1121f", lw=1.0),
        zorder=8,
        bbox=dict(boxstyle="round,pad=0.18", facecolor="white", edgecolor="none", alpha=0.9),
    )

    handles = [
        Line2D([0], [0], color="#00b4d8", lw=2.0, label="Niño 3.4 / ONI (predictor)"),
        Line2D([0], [0], color="#e85d04", lw=2.0, ls="--", label="Eastern Pacific SST (predictor)"),
        Line2D([0], [0], color="#2d6a4f", lw=2.2, ls=":", label="North Atlantic SST (predictor)"),
        Line2D([0], [0], color="#c1121f", lw=2.2, label="TVA target (spatial mean)"),
    ]
    ax.legend(handles=handles, loc="upper left", frameon=True, fontsize=6.5, framealpha=0.92)
    ax.set_title("ERA5 December 2024 monthly-mean precipitation (mm day$^{-1}$)", fontsize=10)
    fig.tight_layout()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close()
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
