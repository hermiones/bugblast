# bugblast
💥 API Fuzzing Tool for QA Engineers – Built with Python, powered by chaos
## BugBlast API Fuzzer

### Setup Instructions

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repo-url>
   cd bugblast
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Prepare a text file (e.g., `endpoints.txt`) with one API endpoint per line.

2. Run the fuzzer:
   ```bash
   python main.py -i endpoints.txt
   ```

### Project Structure

- `main.py` — Entry point for the fuzzer
- `fuzzers/sql_injections.py` — SQL injection fuzzing logic
- `requirements.txt` — Python dependencies
- `endpoints.txt` — Your API endpoints (not included)

### Notes

- The `fuzzers` directory is a local module, not a pip package. No need to install it separately.
- The virtual environment folder (`venv` or `.venv`) is ignored by git.
