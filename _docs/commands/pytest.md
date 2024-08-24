# Pytest Commands

This guide outlines various commands to run tests using pytest.

- **Run pytest:**
    ```bash
    pytest
    ```
- **Run pytest specify markers:**
    ```bash
    pytest -m <marker>
    pytest -m "<marker> and <marker>"
    ```

- **Run all tests in a directory:**
    ```bash
    pytest path/to/directory
    ```

- **Run tests in a specific file:**
    ```bash
    pytest path/to/test_file.py
    ```

- **Run a specific test function:**
    ```bash
    pytest path/to/test_file.py::test_function
    ```

- **Run tests that match a specific substring:**
    ```bash
    pytest -k "substring"
    ```

- **Run tests based on markers:**
    ```bash
    pytest -m "marker_name"
    pytest -m "model and model_structure"
    pytest -m "model or model_structure"
    ```

- **Run tests and generate code coverage report:**
    ```bash
    pytest --cov=path/to/package
    ```

- **Run tests and display print statements:**
    ```bash
    pytest -s
    ```

- **Run tests and stop at the first failure:**
    ```bash
    pytest --exitfirst
    ```

- **Run tests in parallel:**
    ```bash
    pytest -n num_workers
    ```

- **Run tests with verbose output:**
    ```bash
    pytest -v
    ```

- **Run tests and ignore warnings:**
    ```bash
    pytest -p no:warnings
    ```

- **Run tests and rerun failed tests:**
    ```bash
    pytest --reruns num_reruns
    ```

- **Run tests and mark them as slow:**
    ```bash
    pytest --slow
    ```

- **Run tests and mark them as xfail (expected to fail):**
    ```bash
    pytest --xfail
    ```
