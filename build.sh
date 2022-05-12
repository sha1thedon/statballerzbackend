#exit on error
set -o errexit
ls env/Scripts
uname -r
source env/Scripts/activate
python manage.py collectstatic --no-input
python manage.py migrate


