import sys

sys.path.append('../Go')

from main import app, ClubMemberForm


def test_correct():
    response = app.test_client().get('/')
    assert response.status_code == 200


def test_empty():
    response = app.test_client().post('/', data={'name': '', 'email': ''})
    assert response.status_code == 200


def test_app_error():
    response = app.test_client().post(
        '/', data={
            'name': '...!sdfdsf##',
            'email': 'sdfgdgfdgfs'
        })
    assert response.status_code == 200

def test_empty_name():
    response = app.test_client().post(
        '/', data={
            'name': '',
            'email': 'sdfgdgfdgfs@gmail.com'
        })
    assert response.status_code == 200

def test_empty_email():
    response = app.test_client().post(
        '/', data={
            'name': 'asdfdsffsda',
            'email': ''
        })
    assert response.status_code == 200


def test_validation_name():
    pos = ['Dmitrii', 'Qw o g', 'Ere goneal']
    neg = ['!.%', 'Dmi56%%', 'jikflKKFl )(', 'Хеловіа']
    for case in pos:
        form = ClubMemberForm(name=case, email='sdfgdgfdgf@gmail.com')
        form.validate()
        assert form.errors == {}
    for case in neg:
        form = ClubMemberForm(name=case, email='sdfgdgfdgf@gmail.com')
        form.validate()
        assert form.errors == {'name': ['Incorrect value']}

def test_validation_email():
    pos = ['Dmitrii@gmail.com', 'Qw@gma.com', 'Ere@a.ua']
    neg = ['!.%', 'Dmiasdas', 'фауау', 'asdfgmail.com', 'alfa;flkjf@gmail.com', 'adfadsf@gmailcom']
    for case in pos:
        form = ClubMemberForm(name='Qwqer', email=case)
        form.validate()
        assert form.errors == {}
    for case in neg:
        form = ClubMemberForm(name='affae', email=case)
        form.validate()
        assert form.errors == {'email': ['Invalid email address.']}