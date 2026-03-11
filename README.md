## How to Run

## Prerequisites
- Python 3.10+
- Git
- Docker (optional)

### Local Setup
1. Clone the repository:
   `git clone https://github.com/HilufTesfay/esk-assignment1.git`
   `cd esk-assignment1`

2. Create and activate a virtual environment (recommended):
   `python3 -m venv venv`
   `source venv/bin/activate`

3. Install dependencies:
   `pip install --upgrade pip`
   `pip install -r requirements.txt`

4. Run tests:
   `pytest -v`

### Docker
1. Build the image:
   `docker build -t eskalate-assignment .`

2. Run tests in the container:
   `docker run --rm eskalate-assignment`
