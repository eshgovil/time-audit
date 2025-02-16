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

## Set up Supabase
1. Create a new project at [Supabase](https://supabase.com)
2. Create a new table called `tasks` with the following columns:
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

## TODO
- migrate to Poetry
- require signed commits