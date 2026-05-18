from app import create_app

def test_index_returns_a_link_to_duties_page():
       client = create_app().test_client()
       response = client.get("/")
       assert response.status_code == 200
       assert b'<a href="/duties"> Duties </a>' in response.data