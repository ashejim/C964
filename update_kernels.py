import json
from pathlib import Path

def normalize_kernel(notebook_path):
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "metadata" not in data:
            data["metadata"] = {}

        if "kernelspec" not in data["metadata"]:
            data["metadata"]["kernelspec"] = {}

        ks = data["metadata"]["kernelspec"]

        # Check if change is needed
        if ks.get("name") == "python" and ks.get("display_name") == "python":
            return False

        ks["display_name"] = "python"
        ks["language"] = "python"
        ks["name"] = "python"

        with open(notebook_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1)

        return True

    except Exception as e:
        print(f"Error processing {notebook_path}: {e}")
        return False


def main():
    root = Path(".")

    notebooks = list(root.rglob("*.ipynb"))
    updated = 0

    for nb in notebooks:
        if normalize_kernel(nb):
            print(f"Updated: {nb}")
            updated += 1

    print(f"\nFinished. {updated} notebook(s) updated out of {len(notebooks)} found.")


if __name__ == "__main__":
    main()