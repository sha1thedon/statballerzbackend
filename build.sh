
#exit on error
set -o errexit
ls
source env/bin/activate
python manage.py collectstatic --no-input
python manage.py migrate


