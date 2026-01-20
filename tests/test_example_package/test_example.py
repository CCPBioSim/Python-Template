# tests/test_example_package/test_example.py

from example_package.example import placeholder


class TestExamplePackage:
    """
    Class-based placeholder tests for example_package.

    - Demonstrates using a test class with pytest.
    - Can easily be extended with more methods for real tests.
    """

    def test_placeholder(self):
        """
        Minimal placeholder test.

        - Verifies that the placeholder function runs.
        - Serves as a template for adding future tests.
        """
        assert placeholder() is True
