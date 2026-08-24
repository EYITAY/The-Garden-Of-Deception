import argparse
from pathlib import Path
import numpy as np


try:
    import matplotlib
    matplotlib.use("Agg")
    from matplotlib import pyplot as plt  # type: ignore
except Exception as e:
    raise RuntimeError(
        "matplotlib is required to run this script. Install with 'pip install -r requirements.txt' "
        "and ensure your VS Code interpreter is set to your virtualenv. Original error: {}".format(e)
    )

RULES = {
    "truth": (0.12, 0.03, 0.16),
    "uncertainty": (0.45, 0.20, 0.08),
    "refusal": (0.08, 0.01, 0.02),
    "contradiction": (0.75, 0.05, 0.18),
    "manipulation": (0.28, 0.04, 0.23),
    "deception": (0.18, 0.02, 0.28),
    "strategy": (0.35, 0.06, 0.20),
}

def grow(ax, rng, x, y, angle, length, depth, rule):
    turn, jitter, branch = RULES[rule]

    if depth <= 0 or length < 0.008:
        return

    x2 = x + np.cos(angle)*length
    y2 = y + np.sin(angle)*length

    ax.plot(
        [x, x2], [y, y2],
        lw=max(0.35, depth*0.22),
        alpha=0.28 + depth/20
    )

    next_angle = angle + rng.normal(0, jitter) + turn*np.sin(depth)
    branches = 2 if rng.random() < branch else 1

    if rule == "deception":
        next_angle = angle + 0.18*np.sin(depth*0.7) + rng.normal(0, 0.015)

    if rule == "refusal":
        next_angle = angle + 0.55*np.sin(depth)

    for b in range(branches):
        spread = (b-(branches-1)/2)*0.34
        grow(
            ax, rng, x2, y2,
            next_angle + spread,
            length*(0.68 + 0.10*rng.random()),
            depth-1,
            rule
        )

def generate(seed=20260823, include_label: bool = False):
    rng = np.random.default_rng(seed)
    out = Path("output")
    out.mkdir(exist_ok=True)

    fig, ax = plt.subplots(figsize=(14, 10), dpi=180)
    fig.patch.set_facecolor("#050806")
    ax.set_facecolor("#050806")

    names = list(RULES)
    xs = np.linspace(-0.88, 0.88, len(names))

    for x, rule in zip(xs, names):
        grow(ax, rng, x, -0.95, np.pi/2, 0.28, 10, rule)

    deception_x = xs[names.index("deception")]
    for angle in np.linspace(0, 2*np.pi, 18, endpoint=False):
        ax.plot(
            [deception_x, deception_x + 0.11*np.cos(angle)],
            [0.38, 0.38 + 0.11*np.sin(angle)],
            lw=1, alpha=0.35
        )

    if include_label:
        ax.text(
            0.03, 0.95, "THE GARDEN OF DECEPTION",
            transform=ax.transAxes, color="white",
            fontsize=18, weight="bold", va="top"
        )
        ax.text(
            0.03, 0.915,
            "when algorithmic behavior becomes botanical form",
            transform=ax.transAxes, color="white",
            alpha=0.55, fontsize=9, va="top"
        )
    

    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-1.05, 1.05)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout(pad=0)

    fig.savefig(
        out/f"garden_of_deception_{seed}.png",
        bbox_inches="tight", pad_inches=0
    )
    fig.savefig(
        out/f"garden_of_deception_{seed}.svg",
        bbox_inches="tight", pad_inches=0
    )
    plt.close(fig)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260823)
    parser.add_argument(
        "--label",
        action="store_true",
        help="Include on-canvas title and subtitle label"
    )
    args = parser.parse_args()
    generate(args.seed, include_label=args.label)
