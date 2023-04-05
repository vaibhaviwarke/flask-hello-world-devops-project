from app import app


def test_hello():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Hello world!!!'

def check_sum():
    response = app.test_client().get('/sum')
    assert response.status_code == 200
    assert response.data == 30
