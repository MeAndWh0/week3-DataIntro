import json
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = PROJECT_ROOT / "notebooks" / "02_week3_first_look.ipynb"


def check_first_look(namespace):
    """Check answers from the live notebook namespace."""
    answers_are_correct = (
        namespace.get("number_of_rows") == 344
        and namespace.get("number_of_columns") == 7
        and namespace.get("column_with_most_missing") == "sex"
        and namespace.get("duplicate_rows") == 0
        and namespace.get("numeric_columns") == [
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g",
        ]
    )
    if not answers_are_correct:
        print("Some answers are missing or need another look. Review the dataset outputs and try again.")
        return False

    print("Dataset inspection checks passed!")
    return True


def load_exercise_answers():
    with NOTEBOOK_PATH.open(encoding="utf-8") as notebook_file:
        notebook = json.load(notebook_file)

    namespace = {}
    for cell in notebook["cells"]:
        source = "".join(cell.get("source", []))
        if cell.get("cell_type") == "code" and "number_of_rows = None" in source:
            exec(compile(source, str(NOTEBOOK_PATH), "exec"), namespace)
            return namespace
    raise AssertionError("First-look exercise answer cell was not found.")


class FirstLookTests(unittest.TestCase):
    def test_dataset_inspection_answers(self):
        self.assertTrue(check_first_look(load_exercise_answers()))


if __name__ == "__main__":
    unittest.main()