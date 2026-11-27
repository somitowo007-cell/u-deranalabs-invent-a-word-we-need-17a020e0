import os

ENTRY = "lanegret (n.) \u2014 the instant regret of changing lanes just as your old lane starts moving faster."

def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
