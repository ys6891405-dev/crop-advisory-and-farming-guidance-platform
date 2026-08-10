from database import get_db_connection


def create_user(name, email, password):
    connection = get_db_connection()

    connection.execute(
        """
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
        """,
        (name, email, password)
    )

    connection.commit()
    connection.close()


def get_user_by_email(email):
    connection = get_db_connection()

    user = connection.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    ).fetchone()

    connection.close()

    return user