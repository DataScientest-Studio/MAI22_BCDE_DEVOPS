import requests

def test_welcome():
    r = requests.get(url="http://127.0.0.1:8000/welcome") 
    assert "data" in r.json()   
    

def test_welcome2():
    r = requests.get(url="http://127.0.0.1:8000/welcome") 
    assert "Welcome to all"==r.json()["data"]

def test_number():
    r = requests.get(url="http://127.0.0.1:8000/number") 
    assert int(r.text)==1

def test_health():
    r = requests.get(url="http://127.0.0.1:8000/health")
    assert r.json()=="Hello"
    
    
