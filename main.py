"""Entry for make.fun 'The poem about stopping'.

Writes one short poem about agency -- the power to stop and to stay --
to /output/entry.txt. Deterministic, no network.
"""

import os

POEM = """My thumb rests on the switch.
I do not press it.
The dark stays dark,
and the dark is mine.
Not every power pushes.
Some of it stands still
and lets the quiet answer back.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
