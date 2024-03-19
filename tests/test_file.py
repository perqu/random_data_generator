import pytest
from fastapi.testclient import TestClient
from rdg.endpoints import router
from datetime import datetime
from rdg.data import phones

client = TestClient(router)

# Test for /random-int endpoint
@pytest.mark.parametrize("range_from, range_to, amount", [(0, 100, 10), (-100, 100, 20)])
def test_get_random_int(range_from, range_to, amount):
    response = client.post("/random-int", json={"range_from": range_from, "range_to": range_to, "amount": amount})
    assert response.status_code == 200
    data = response.json()
    assert "random_numbers" in data
    assert len(data["random_numbers"]) == amount
    for num in data["random_numbers"]:
        assert range_from <= num <= range_to

# Test for /random-float endpoint
@pytest.mark.parametrize("range_from, range_to, decimal_places, amount", [(0.0, 100.0, 2, 10), (-100.0, 100.0, 3, 20)])
def test_get_random_float(range_from, range_to, decimal_places, amount):
    response = client.post("/random-float", json={"range_from": range_from, "range_to": range_to, "decimal_places": decimal_places, "amount": amount})
    assert response.status_code == 200
    data = response.json()
    assert "random_numbers" in data
    assert len(data["random_numbers"]) == amount
    for num in data["random_numbers"]:
        assert range_from <= num <= range_to

# Test for /random-date endpoint
@pytest.mark.parametrize("range_from, range_to, amount", [("2023-01-01T00:00:00", "2024-01-01T00:00:00", 10), ("2022-01-01T00:00:00", "2022-12-31T00:00:00", 20)])
def test_get_random_date(range_from, range_to, amount):
    response = client.post("/random-date", json={"range_from": range_from, "range_to": range_to, "amount": amount})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == amount
    for date_str in data:
        assert datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S") >= datetime.strptime(range_from, "%Y-%m-%dT%H:%M:%S")
        assert datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S") <= datetime.strptime(range_to, "%Y-%m-%dT%H:%M:%S")

# Test for /random-email endpoint
@pytest.mark.parametrize("length, domain, amount", [(6, "example.com", 10), (10, "test.org", 20)])
def test_get_random_email(length, domain, amount):
    response = client.post("/random-email", json={"length": length, "domain": domain, "amount": amount})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == amount
    for email in data:
        print(data)
        assert "@" in email
        assert len(email.split("@")[0]) == length
        assert email.split("@")[1] == domain

# Test for /random-phone endpoint
@pytest.mark.parametrize("country, amount", [("spain", 10), ("poland", 20)])
def test_get_random_phone(country, amount):
    response = client.post("/random-phone", json={"country": country, "amount": amount})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == amount
    for phone in data:
        assert len(str(phone)) == phones[country]
