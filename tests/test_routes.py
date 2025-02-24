def test_get_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_individual_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "terrestrial",
        "has_moon": False
    }

def test_get_individual_planet_with_no_data(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404

def test_get_planets(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Mercury",
        "description": "terrestrial",
        "has_moon": False
    },
    {
        "id": 2,
        "name": "Saturn",
        "description": "gas giants",
        "has_moon": True
    }]

def test_post_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "terrestrial",
        "has_moon": True
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Earth successfully created"
