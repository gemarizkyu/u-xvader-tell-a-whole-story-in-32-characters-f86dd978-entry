"""Tell a Whole Story in 32 Characters: This WiFi survived my divorce.

Writes one Wi-Fi network name to /output/entry.txt.

Why this name: it lands the joke on the first read and implies a whole
story in a few words a stranger sees in a phone's network list. The
situation is a home Wi-Fi network, the character is the narrator (and
the ex implied by the word "my"), and something happened: a divorce.
The network is still here; the marriage is not. It is deadpan, fresh
next to the stock Wi-Fi jokes (Pretty Fly for a Wi-Fi, FBI Surveillance
Van, It Burns When IP), and tight: 29 characters, every word earning
its place, easy to say out loud. "Survived my divorce" beats the
runner-up "outlived my marriage": a divorce is an event that happened,
a marriage is only a state, and the event is what makes the story.

Deterministic: no clock, no randomness, no network, no model calls.
The name is 29 characters, inside the 1-32 gate.
"""

from pathlib import Path

# The entry: a network that outlasted a marriage.
NAME = "This WiFi survived my divorce"


def build_name() -> str:
    """Return the single Wi-Fi network name.

    One line of plain text, no trailing newline: the gate counts the
    file's characters, so the file holds exactly the name.
    """
    return NAME


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = (output_dir / "entry.txt").resolve()
    # Refuse to write outside the intended output directory.
    if output_path.parent != output_dir.resolve():
        raise ValueError("unsafe output path")
    name = build_name()
    if not 1 <= len(name) <= 32:
        raise ValueError(f"entry is {len(name)} characters, must be 1-32")
    if not name.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in name or "\r" in name:
        raise ValueError("entry must be a single line")
    if not name.isascii():
        raise ValueError("entry must be plain ASCII so it displays the same in every network list")
    output_path.write_text(name, encoding="utf-8")


if __name__ == "__main__":
    main()
