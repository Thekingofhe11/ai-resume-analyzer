# Run the backend from the project backend folder
$python = "$PSScriptRoot\venv\Scripts\python.exe"
& $python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
