# Time Audit

App to easily and effectively track time usage, to audit where your time goes to and calibrate accordingly.

## FAQ

### What should I enter for a task?
This is meant to be flexible text entries for you to track what you have done, in the 
way you like to break things down and write it.

## Roadmap

- Allocate hours to things done, view time allocation pie chart
- Categorize things done, view category pie chart

## Setup Environment

1. Install Python 3.13
   ```bash
   # On macOS with Homebrew
   brew install python@3.13
   
   # On Ubuntu/Debian
   sudo apt update
   sudo apt install python3.13
   ```

2. Install Poetry
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Configure Poetry to use local virtualenvs (recommended for IDE integration)
   ```bash
   poetry config virtualenvs.in-project true
   ```

4. Install dependencies
   1. For local development (default, includes dev dependencies):
   ```bash
   poetry install
   ```
   2. For production (no dev dependencies):
   ```bash
   poetry install --without dev
   ```

5. Activate the virtual environment (note: your IDE should automatically do this)
   ```bash
   # Option 1: Activate the environment (recommended)
   poetry env use python3.13
   poetry env activate

   # Option 2: Run commands through Poetry
   poetry run streamlit run app.py
   ```

   Note: If you get a "command not available" error with `poetry shell`, use `poetry env activate` instead.

6. (Optional) Check Installed Python Version
   ```bash
   poetry env info
   ```


## Set up Supabase
1. Create a new project at [Supabase](https://supabase.com)
2. Create a new table called `tasks` with the following columns (easy through UI):
    ```sql
    id          bigint (primary key, identity)
    task        text (required)
    task_date   date (required)
    created_at  timestamptz (required)
    ```
3. Enable Row Level Security (RLS) on the table
4. Add the following RLS policy (WARNING: development only! Not secure for production):
    ```sql
    CREATE POLICY "Allow anonymous access" ON public.tasks
    AS PERMISSIVE FOR ALL
    TO anon
    USING (true)
    WITH CHECK (true);
    ```
5. Get your project URL and anon key from Project Settings > API
6. Create a `.env` file in the project root with:
    ```
    SUPABASE_URL=your_project_url
    SUPABASE_KEY=your_anon_key
    ```

## Development

### Running the App
After activating the environment:
```bash
streamlit run app.py
```

Or using Poetry directly:
```bash
poetry run streamlit run app.py
```

### Keeping Dependencies Up to Date
When there are changes to dependencies in `pyproject.toml`:
```bash
poetry update
```

## TODO
- migrate to Poetry
- require signed commits