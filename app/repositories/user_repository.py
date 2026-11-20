
from app.database import  database
users = {}
next_user_id = 1

async def save_user(user_data: dict):
    query = """
        INSERT INTO users
        (first_name, last_name, email, age, address, joining_date)
        VALUES
        (:first_name, :last_name, :email, :age, :address, :joining_date)
    """

    values = {
        "first_name": user_data["first_name"],
        "last_name": user_data["last_name"],
        "email": user_data["email"],
        "age": user_data["age"],
        "address": user_data["address"],
        "joining_date": user_data["joining_date"]
    }

    user_id = await database.execute(query=query, values=values)

    return user_id

    user_id = next_user_id
    users[user_id] = user_data
    next_user_id += 1

    return user_id

async def get_all_users():
    query = """
        SELECT * FROM users
    """

    users = await database.fetch_all(query=query)

    return users
async def get_user_by_id(user_id: int):
    query = """
    SELECT * from users
    where user_id = :user_id
    """

    user = await database.fetch_one(
        query=query,
        values={"user_id": user_id}
    )
    return user



async def update_user(user_id: int, user_data: dict):
    existing_user = await get_user_by_id(user_id)

    if existing_user is None:
        return None

    query = """
        UPDATE users
        SET first_name = :first_name,
            last_name = :last_name,
            email = :email,
            age = :age,
            address = :address
        WHERE user_id = :user_id
    """

    values = {
        "user_id": user_id,
        "first_name": user_data["first_name"],
        "last_name": user_data["last_name"],
        "email": user_data["email"],
        "age": user_data["age"],
        "address": user_data["address"]
    }

    await database.execute(query=query, values=values)

    return await get_user_by_id(user_id)

async def delete_user(user_id: int):
    existing_user = await get_user_by_id(user_id)

    if existing_user is None:
        return None

    query = """
        DELETE FROM users
        WHERE user_id = :user_id
    """

    await database.execute(
        query=query,
        values={"user_id": user_id}
    )

    return dict(existing_user)

async def register_user(user_id: int):
    existing_user = await get_user_by_id(user_id)

    if existing_user is None:
        return None

    query = """
        UPDATE users
        SET is_registered = TRUE
        WHERE user_id = :user_id
    """

    await database.execute(
        query=query,
        values={"user_id": user_id}
    )

    return await get_user_by_id(user_id)