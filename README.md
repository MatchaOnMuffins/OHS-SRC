# OHS-SRC
# Installation

## MacOS
```bash
git clone https://github.com/MatchaOnMuffins/OHS-SRC.git
cd OHS-SRC/
python3 -m venv ./venv/
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Windows
```bash
git clone https://github.com/MatchaOnMuffins/OHS-SRC.git
cd OHS-SRC\
python -m venv .\venv\
.\venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```
# Configuration
Place files `config.json` and `ohs-src-firebase-admin.json` into `auth/`

# Execution
To run program, execute
```bash
python main.py
```

# Cleaning Up
To deactivate venv, run
```bash
deactivate
```
# License
Licensed under the [MIT License](LICENSE)