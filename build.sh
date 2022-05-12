#exit on error
set -o errexit
python -m pip install -r requirements.txt
python manage.py migrate


