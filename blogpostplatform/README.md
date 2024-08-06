# BlogpostPlatform

## Description

This is a simple blogpost platform made as part of Django training bootcamp.

## Setup Instructions

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.10 and higher

### Step 1: Create a virtual environment

Create a virtual environment to install dependencies in and activate it:

```bash
python3 -m venv .blogpostplaform_venv
source .blogpostplaform_venv/bin/activate
```

### Step 2: Install required dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Apply migrations

```bash
python manage.py migrate
```

### Step 4: Run the dev server

```bash
python manage.py runserver
```