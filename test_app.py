import os
import tempfile
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<form' in response.data  # Checks if form is present

def test_submit_report(client, monkeypatch):
    # Prepare dummy data
    test_data = {
        'name': 'TestUser',
        'email': 'test@example.com',
        'skills': 'Python, Flask',
        'experience': '2 years'
    }
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, 'TestUser_report.pdf')

    # Patch REPORT_FOLDER and generate_report
    monkeypatch.setattr('app.REPORT_FOLDER', temp_dir)
    called = {}
    def fake_generate_report(path, name, email, skills, experience):
        called['called'] = True
        assert path == file_path
        assert name == test_data['name']
        assert email == test_data['email']
        assert skills == test_data['skills']
        assert experience == test_data['experience']
    monkeypatch.setattr('app.generate_report', fake_generate_report)

    response = client.post('/submit', data=test_data)
    assert response.status_code == 200
    assert b'Report Generated Successfully' in response.data
    assert called.get('called')