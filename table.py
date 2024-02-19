from collections import defaultdict
import json


# Load and restructure data for table
def load_and_restructure_data():
    with open("stats.json", "r") as file:
        stats = json.loads(file.read())

    languages = defaultdict(int)
    data = {"totals": defaultdict(int)}

    for problem in stats:
        if not problem["title"]:
            continue
        if problem["type"].startswith("Binary"):
            problem["type"] = "Binary Tree"
        if problem["type"] not in data:
            data[problem["type"]] = defaultdict(int)

        data[problem["type"]][problem["difficulty"]] += 1
        data["totals"][problem["difficulty"]] += 1

        languages["python"] += 1 if problem["python"] else 0
        languages["javascript"] += 1 if problem["javascript"] else 0
        languages["both"] += 1 if problem["python"] and problem["javascript"] else 0
    print("\nRestructured data for table.")

    header = "<!-- " + f"{languages}"[27:-1] + " -->"
    return header, data


# Generates new markdown table from data
def create_markdown_table(data):
    table = "| |Easy|Medium|Hard|Total|\n|-|-|-|-|-|"

    keys = sorted(data.keys())
    for p_type in keys:
        if p_type == "totals":
            continue
        vals = data[p_type]

        # f-strings are NOT cooperating with me rn
        easy, medium, hard = vals["easy"], vals["medium"], vals["hard"]
        total = easy + medium + hard
        row = f"\n|{p_type}|{easy}|{medium}|{hard}|{total}|"
        table += row

    totals = data["totals"]
    easy, medium, hard = totals["easy"], totals["medium"], totals["hard"]
    overall_total = easy + medium + hard
    table += f"\n|Totals|**{easy}**|**{medium}**|**{hard}**|**{overall_total}**|"

    print("Created new markdown table.")
    return table


# Updates readme file with new table
def update_readme(table="_Table placeholder_", path="readme.md"):
    splitter = "<!-- scriptdivider -->"
    with open(path, "r") as file:
        readme = file.read()

    readme = readme.split(splitter)
    readme[1] = "\n" + table + "\n"

    with open(path, "w") as file:
        file.write(splitter.join(readme))

    print("readme.md has been updated!")


if __name__ == "__main__":
    header, data = load_and_restructure_data()
    table = create_markdown_table(data)
    full_table = header + "\n\n" + table
    update_readme(full_table, "readme.md")
