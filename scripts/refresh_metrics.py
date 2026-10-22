#!/usr/bin/env python3
"""Regenerate the README from data/profile.json.

Star and fork counts for arian-gogani/nobulex are not fetched. GitHub
returns HTTP 451 for that repository, and the profile no longer publishes
those counts.
"""

from __future__ import annotations

from render import main as render_readme


def main() -> None:
    render_readme()


if __name__ == "__main__":
    main()
