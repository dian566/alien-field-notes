#!/usr/bin/env python3
"""Alien Field Notes entry for make.fun: one alien tourist's review of Earth."""

# The line below is fixed by the bounty brief; this program only writes it out.

from os import makedirs

REVIEW = (
    "Four stars. Stunning blue marble, lovely sunsets — but the locals "
    "worship glowing rectangles, queue for bitter bean water, and only "
    "look up when something falls."
)


def write_review() -> None:
    """Write the review to /output/entry.txt, nothing else."""
    if len(REVIEW) > 200 or not REVIEW.strip():
        raise ValueError("entry must be a non-empty line of at most 200 characters")
    if "\n" in REVIEW or "\r" in REVIEW:
        raise ValueError("entry must be a single line")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(REVIEW)


if __name__ == "__main__":  # run as a script
    write_review()
