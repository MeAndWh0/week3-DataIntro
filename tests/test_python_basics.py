import json
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = PROJECT_ROOT / "notebooks" / "00_python_basics.ipynb"


def load_notebook_namespace():
    with NOTEBOOK_PATH.open(encoding="utf-8") as notebook_file:
        notebook = json.load(notebook_file)

    # Avoid opening an interactive pager for the notebook's help() example.
    namespace = {"__name__": "__notebook__", "help": lambda *args, **kwargs: None}
    for cell in notebook["cells"]:
        if cell.get("cell_type") == "code":
            source = "".join(cell.get("source", []))
            if "check_summarise_scores(summarise_scores)" in source:
                continue
            exec(compile(source, str(NOTEBOOK_PATH), "exec"), namespace)
    return namespace


class SummariseScoresTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summarise_scores = load_notebook_namespace()["summarise_scores"]

    def test_summarises_whole_number_scores(self):
        self.assertEqual(
            self.summarise_scores([6, 8, 10]),
            {"count": 3, "total": 24, "average": 8.0},
        )

    def test_summarises_decimal_scores(self):
        self.assertEqual(
            self.summarise_scores([1.5, 2.5]),
            {"count": 2, "total": 4.0, "average": 2.0},
        )

    def test_empty_list_has_no_average(self):
        self.assertEqual(
            self.summarise_scores([]),
            {"count": 0, "total": 0, "average": None},
        )


if __name__ == "__main__":
    unittest.main()