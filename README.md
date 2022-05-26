# OHS-SRC
# Deployment
## Important
* Auth files `config.json` and `ohs-src-firebase-admin.json` need to be placed in `auth/`


## MacOS
```bash
git clone https://github.com/MatchaOnMuffins/OHS-SRC.git
cd OHS-SRC/
python3 -m venv ./venv/
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 main.py
```

## Windows
```bash
git clone https://github.com/MatchaOnMuffins/OHS-SRC.git
cd OHS-SRC\
python -m venv .\venv\
.\venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
python main.py
```