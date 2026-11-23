from pathlib import Path

LABEL = "WARNING: Contents under pressure. May spontaneously share opinions, start meetings, and reply-all. Accuracy not included."

def main() -> None:
    # Competition limit: the whole label must fit on one printed line.
    assert len(LABEL) <= 160, len(LABEL)
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LABEL + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
