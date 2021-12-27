<h1>Simple app for adding club members into list.</h1>

<h2>Install</h2>

<code>git clone https://github.com/scientia-ac-labore/club_members_list</code>

<code>cd club_members_list</code>

<code>python3 -m venv env</code>

For Windows

<code>path\env\Scripts\activate.bat</code>
  
For Linux
  
<code>source env/bin/activate</code>

<code>pip install -r requirements.txt</code>

<code>flask run</code>

<h2>Test</h2>

<code>pytest tests/test_form.py</code>

<h2>Logging</h2>

For logging, change <code>FLASK_ENV=production</code> in <code>.flaskenv</code> to <code>FLASK_ENV=development</code>
