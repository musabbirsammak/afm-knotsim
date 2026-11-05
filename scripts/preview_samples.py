"""Plot a grid of generated samples with crossings and topology overlaid.

For now, ``--templates`` plots the 3D seed templates so you can check them by eye.
"""

import argparse

import matplotlib.pyplot as plt

from knotsim.chains.templates import TEMPLATES, get_template


def preview_templates(out: str) -> None:
    names = []
    for name in TEMPLATES:
        try:
            get_template(name)
            names.append(name)
        except NotImplementedError:
            pass
    fig = plt.figure(figsize=(4 * len(names), 4))
    for i, name in enumerate(names, start=1):
        c = get_template(name)
        ax = fig.add_subplot(1, len(names), i, projection="3d")
        ax.plot(*c.T, lw=2)
        ax.plot(*c[[-1, 0]].T, lw=2, color="C0")  # close the loop
        ax.set_title(name)
        ax.set_axis_off()
    fig.savefig(out, dpi=120, bbox_inches="tight")
    print(f"saved {out}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--templates", action="store_true")
    p.add_argument("--out", default="outputs/templates.png")
    a = p.parse_args()
    if a.templates:
        preview_templates(a.out)
    else:
        raise NotImplementedError("Sample preview needs knotsim.io.read_shard")
