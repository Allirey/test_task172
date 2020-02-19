git clone https://github.com/Allirey/test_task172 \
cd test_task172/ \
python3 -m venv venv \
source venv/bin/activate \
pip install -r requirements.txt \
./manage.py migrate \
./manage.py runserver