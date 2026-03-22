import pytest


@pytest.mark.asyncio
async def test_create_user_success(client):
    payload = {
        'name': 'test_user',
        'email': 'test@example.com',
        'password': 'senhasupersecreta',
    }

    response = await client.post('/users', json=payload)

    print(response)

    status = 201

    assert response.status_code == status
    assert response.json()['email'] == 'test@example.com'
    assert response.json()['name'] == 'test_user'
    assert response.json()['id'] == 1


@pytest.mark.asyncio
async def test_email_already_in_use(client):
    payload = {
        'name': 'test_user',
        'email': 'test@example.com',
        'password': 'senhasupersecreta',
    }

    user1 = await client.post('/users', json=payload)

    print(user1.json())

    response = await client.post('/users', json=payload)

    status = 409

    assert response.status_code == status
    assert response.json()['detail'] == 'Este email já está cadastrado.'
