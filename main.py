```python
#!/usr/bin/env python3
"""
Kodus Code Review Test Script.

A small demonstration program containing reusable functions,
input validation, logging, and a command-line entry point.
"""

import logging
from typing import Final


APP_NAME: Final[str] = "Kodus Code Review Test Script"
DEFAULT_NAME: Final[str] = "World"

logger = logging.getLogger(__name__)


def greet(name: str) -> str:
    """
    Create a greeting message for a person.

    Args:
        name: The person's name.

    Returns:
        A formatted greeting message.

    Raises:
        ValueError: If the name is empty or contains only whitespace.
    """
    if not name or not name.strip():
        raise ValueError("Name cannot be empty.")

    return f"Hello, {name.strip()}!"


def add(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        The sum of the two integers.
    """
    return a + b


def run_demo() -> None:
    """Run the application demonstration."""
    logger.info("Starting application")

    print(f"=== {APP_NAME} ===")
    print()

    try:
        greeting = greet(DEFAULT_NAME)
        print(greeting)

        result = add(5, 3)
        print(f"5 + 3 = {result}")

    except ValueError as error:
        logger.error("Failed to generate greeting: %s", error)
        print(f"Error: {error}")

    print()
    print("Script completed successfully!")

    logger.info("Application finished")


def main() -> None:
    """Configure logging and start the application."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    run_demo()


if __name__ == "__main__":
    main()
```
