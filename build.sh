#exit on error
set -o errexit
python -m pip install requirements.txt
python manage.py migrate


