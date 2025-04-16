## How to Run Tests Locally
1. Have pytest lib package installed:
    ```bash
    pip install pytest
    ```
2. Run one of the testing commands:
    ```bash
    pytest
    ```
    ```bash
    pytest tests/<test-file-name>.py
    ```
    ```bash
    python -m pytest tests/<test-file-name>.py
    ```
## NOTE
- Depending on API calls, there might be errors attributed to rate-limits.
- Running tests locally does not require the server to be running, and thus bypasses lib-specific status codes, messages, or otherwise responses. If you think a test should have passed, try conducting the same test by writing it in the `tests.http` file and seeing the response.
