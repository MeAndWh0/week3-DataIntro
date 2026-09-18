def check_summarise_scores(summarise_scores):
    """Check the student's score-summary function and show a friendly result."""
    test_cases = [
        ([6, 8, 10], {"count": 3, "total": 24, "average": 8.0}),
        ([1.5, 2.5], {"count": 2, "total": 4.0, "average": 2.0}),
        ([], {"count": 0, "total": 0, "average": None}),
    ]

    for scores, expected in test_cases:
        actual = summarise_scores(scores)
        assert actual == expected, (
            f"For {scores}, expected {expected}, but got {actual}."
        )

    print("All checks passed. Your function works for the example cases!")
