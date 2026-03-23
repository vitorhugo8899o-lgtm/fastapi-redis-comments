import pytest


@pytest.mark.asyncio
async def test_create_user_sucess(client):
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


@pytest.mark.asyncio
async def test_login_user(client, user):

    payload = {'email': f'{user["email"]}', 'password': f'{user["password"]}'}

    response = await client.post('/users/login', json=payload)

    data = response.json()

    status = 200

    assert response.status_code == status
    assert 'id_user' in data
    assert 'email' in data
    assert 'message' in data

    assert data['email'] == payload['email']
    assert data['message'] == 'Usuário Logado!'
    assert isinstance(data['id_user'], int)


@pytest.mark.asyncio
async def test_email_does_not_exist(client):
    payload = {
        'email': 'emailnãoexiste@gmail.com',
        'password': 'senhaforte123',
    }

    response = await client.post('/users/login', json=payload)

    status = 404

    assert response.status_code == status
    assert response.json()['detail'] == 'Email não está cadastrado.'


@pytest.mark.asyncio
async def test_password_wrong(client, user):

    payload = {'email': f'{user["email"]}', 'password': 'senhaerrada123'}

    response = await client.post('/users/login', json=payload)

    status = 401

    assert response.status_code == status
    assert response.json()['detail'] == 'Email ou senha invalidos'


@pytest.mark.asyncio
async def test_user_update_information(client, user):
    payload = {
        'new_info': {
            'name': 'new_user',
            'email': 'new_user@example.com',
            'password': 'newuserpassword123',
        },
        'user': {
            'email': f'{user["email"]}',
            'password': f'{user["password"]}',
        },
    }

    response = await client.put('/users/me', json=payload)

    status = 200

    assert response.status_code == status
    assert (
        response.json()
        == 'Informações Atualizadas com Sucesso!, Bem vindo new_user'
    )  # noqa E501


@pytest.mark.asyncio
async def test_delete_user_account(client, user):

    payload = {
        'confirm': {'message': 'Confirmo deletar minha conta'},
        'user': {
            'email': f'{user["email"]}',
            'password': f'{user["password"]}',
        },
    }

    response = await client.request('DELETE', '/users/me', json=payload)

    status = 200

    assert response.status_code == status
    assert response.json() == 'Conta deletada!'


@pytest.mark.asyncio
async def test_get_all_users_in_system(client, user):
    response = await client.get(f'/users?init={0}&end={-1}')

    data = response.json()

    status = 200

    assert response.status_code == status
    assert len(data) == 1
    assert data[0] == {'id_user': '1', 'email': 'test@example.com'}
