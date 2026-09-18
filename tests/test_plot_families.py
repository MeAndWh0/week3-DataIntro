import json
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = PROJECT_ROOT / "notebooks" / "01_week3_plot_families.ipynb"


def check_plot_design(namespace):
    """Check answers from the live notebook namespace."""
    answers_are_correct = (
        namespace.get("plot_family") == "comparison"
        and namespace.get("x_variable") == "species"
        and namespace.get("y_variable") == "body_mass_g"
        and namespace.get("show_individuals") is True
        and namespace.get("bar_axis_starts_at_zero") is True
    )
    if not answers_are_correct:
        print("Some answers are missing or need another look. Review the question and try again.")
        return False

    print("Plot design checks passed!")
    return True


def load_exercise_answers():
    with NOTEBOOK_PATH.open(encoding="utf-8") as notebook_file:
        notebook = json.load(notebook_file)

    namespace = {}
    for cell in notebook["cells"]:
        source = "".join(cell.get("source", []))
        if cell.get("cell_type") == "code" and "plot_family = None" in source:
            exec(compile(source, str(NOTEBOOK_PATH), "exec"), namespace)
            return namespace
    raise AssertionError("Plot exercise answer cell was not found.")


class PlotDesignTests(unittest.TestCase):
    def test_plot_design_answers(self):
        self.assertTrue(check_plot_design(load_exercise_answers()))


if __name__ == "__main__":
    unittest.main()