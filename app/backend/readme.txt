In this folder, execute the following Powershell Commands:
(Console with STRG+Ö in VsCode)

1. Create Python Environment
    python -m venv .venv

2. Install Dependencies
    pip install -r requirements.txt

3. Migrate Django manage.py
    python manage.py migrate

4. Start the Django Server
    python manage.py runserver
    (To specify a port, put its number after "runserver")