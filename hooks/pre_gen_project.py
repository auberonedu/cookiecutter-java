import datetime
import os
import json

def add_year_to_context():
    # Get the current year
    year = str(datetime.datetime.now().year)

    # Path to the cookiecutter context file
    context_file = os.path.join(os.getcwd(), "cookiecutter.json")

    # Load, modify, and save back the context
    with open(context_file, "r") as f:
        context = json.load(f)

    context["year"] = year

    with open(context_file, "w") as f:
        json.dump(context, f, indent=4)

if __name__ == "__main__":
    add_year_to_context()
