# Time Audit

App to easily and effectively track time usage, to audit where your time goes to and calibrate accordingly

## Setup Environment

1. Install Python 3.13
   ```bash
   # On macOS with Homebrew
   brew install python@3.13
   
   # On Ubuntu/Debian
   sudo apt update
   sudo apt install python3.13
   ```

2. Create and activate virtual environment
   ```bash
   python3.13 -m venv .venv
   source .venv/bin/activate  # On Unix/macOS
   # OR
   .\venv\Scripts\activate  # On Windows
   ```

3. Install pip-tools
   ```bash
   pip install pip-tools
   ```

4. Install dependencies
   ```bash
   pip-sync
   ```

TODO: migrate to Poetry
