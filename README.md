
# Submission

### Final Project Proposal

Team Members:

1. Joseph Geiger
2. Kristian Krattiger

Application Name: Web Yt-dlp

Application Description: Feature rich self hostable web ui for downloading youtube videos and music with controls for metadata parsing and formatting

### Major Features:

1. Download videos off youtube
2. Download music off youtube
3. Modify metadata
4. Select metadata to embed into music files
5. Queue and folder on host machine selection

### Planned pages/screens

1. Link input
2. File format chooser and metadata manipulator
3. Download progress page

### Requirements

1. Python version 3.10+
2. Node.js

### Setup

From the project root, create the Python env and install backend requirements:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

On macOS or Linux, use `python3 -m venv .venv` and `.venv/bin/pip install -r requirements.txt` instead.

### Start the server

From the `frontend` folder:

```powershell
npm start
```

or from the `backend` folder:

```powershell
.venv\Scripts\uvicorn server:app --reload
```

On macOS or Linux, use `npm run start:unix` or `.venv/bin/uvicorn server:app --reload` instead.

Then navigate to http://localhost:8000 in your browser.
