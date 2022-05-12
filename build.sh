
#exit on error
set -o errexit
source env/bin/activate
python manage.py collectstatic --no-input
python manage.py migrate


