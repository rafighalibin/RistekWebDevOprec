
1. Inisasi virtual environment:<br>
python -m venv env

2. Nyalakan virtual environment:<br>
env\Scripts\activate.bat

3. Install dependencies:<br>
pip install -r requirements.txt

4. Apply DB scheme:<br>
python manage.py migrate

5. Runserver:<br>
python manage.py runserver