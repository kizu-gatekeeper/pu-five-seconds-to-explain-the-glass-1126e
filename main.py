"""Write a house cat's defence to the make.fun output directory."""

import os

LINE = "Your Honour, the glass was already falling. I merely provided the supervision it clearly lacked."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
