import pytest


@pytest.mark.asyncio
async def test_create_comment_sucess(client, user):
    payload = {
        'comment': {'comment': 'comentário foda'},
        'user': {
            'email': f'{user["email"]}',
            'password': f'{user["password"]}',
        },
    }

    response = await client.post('/comments', json=payload)

    status = 201

    data = response.json()

    assert response.status_code == status
    assert data['_id_comment'] == 'comment:1'
    assert data['_id_user'] == 1
    assert data['_email_user'] == user['email']
    assert data['comment'] == 'comentário foda'
    assert data['likes'] == 0


@pytest.mark.asyncio
async def test_get_all_comments(client, comment_popule):
    response = await client.get(f'/comments?init={0}&end={-1}')

    status = 200

    total_comment = 10

    data = response.json()

    assert response.status_code == status
    assert len(data) == total_comment
    assert data[0] == {
        'id': '1',
        'message': f'{comment_popule["comment"]["comment"]}',
        'email_user': 'test@example.com',
    }


@pytest.mark.asyncio
async def test_like_in_comment(client, comment_popule, user):
    payload = {'email': f'{user["email"]}', 'password': f'{user["password"]}'}

    response = await client.post(f'/comments/{1}', json=payload)

    status = 200

    assert response.status_code == status
    assert response.json() == 'Comentário curtido: likes no comentário 1'


@pytest.mark.asyncio
async def test_user_alredy_like_the_comment(client, comment_popule, user):
    payload = {'email': f'{user["email"]}', 'password': f'{user["password"]}'}

    await client.post(f'/comments/{1}', json=payload)

    response = await client.post(f'/comments/{1}', json=payload)

    status = 409

    assert response.status_code == status
    assert response.json()['detail'] == 'Você já curtiu esse comentário'


@pytest.mark.asyncio
async def test_comment_not_found(client, user):
    payload = {'email': f'{user["email"]}', 'password': f'{user["password"]}'}

    response = await client.post(f'/comments/{89}', json=payload)

    status = 404

    assert response.status_code == status
    assert response.json()['detail'] == 'Comentário não encontrado'


@pytest.mark.asyncio
async def test_get_all_liked(client, user):
    payload = {'email': f'{user["email"]}', 'password': f'{user["password"]}'}

    await client.post(f'/comments/{1}', json=payload)

    response = await client.post(f'/comments/{1}/liked_list')

    status = 200

    assert response.status_code == status
    assert (
        response.json()
        == """Total de curtidas: 1. Pessoas que curtiram: {'test@example.com'}"""  # noqa E501
    )


@pytest.mark.asyncio
async def test_comment_not_founf_or_delete(client):
    response = await client.post(f'/comments/{1}/liked_list')

    status = 404

    assert response.status_code == status
    assert (
        response.json()['detail'] == 'Comentário não encontrado ou deletado.'  # noqa E501
    )


@pytest.mark.asyncio
async def test_comment_not_likes_(client, user):
    payload = {
        'comment': {'comment': 'comentário foda'},
        'user': {
            'email': f'{user["email"]}',
            'password': f'{user["password"]}',
        },
    }

    comment = await client.post('/comments', json=payload)

    response = await client.post(f'/comments/{1}/liked_list')

    status = 200

    assert comment.json()['_id_comment'] == 'comment:1'
    assert response.status_code == status
    assert response.json() == 'Esse comentário não possui curtidas'


@pytest.mark.asyncio
async def test_delete_comment(client, user, comment_popule):

    payload = {'email': f'{user["email"]}', 'password': f'{user["password"]}'}

    response = await client.request('DELETE', f'/comments/{1}', json=payload)

    status = 200

    assert response.status_code == status
    assert response.json() == 'Comentário deletado.'


@pytest.mark.asyncio
async def test_try_to_delete_comment_from_another_user(
    client, user_popule, comment_popule
):  # noqa E501

    payload = {'email': 'test1@example.com', 'password': 'senhasupersecreta'}

    response = await client.request('DELETE', f'/comments/{2}', json=payload)

    status = 403

    assert response.status_code == status
    assert (
        response.json()['detail'] == 'O email não coincide com o do comentário'
    )  # noqa E501


@pytest.mark.asyncio
async def test_comment_not_exists(client, user_popule, comment_popule):

    payload = {'email': 'test1@example.com', 'password': 'senhasupersecreta'}

    response = await client.request('DELETE', f'/comments/{50}', json=payload)

    status = 404

    assert response.status_code == status
    assert response.json()['detail'] == 'Comentário não encontrado'
