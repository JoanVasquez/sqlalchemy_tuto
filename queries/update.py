from main import session
from models.user import Preference, User

user_preference = (
    Preference.query
    .join(Preference.user)
    .filter(User.email == "johndoe@gmail.com")
    .first()
)

user_preference.currency = "GBP"
session.commit()

user = User.query \
    .filter(User.first_name == "John") \
    .filter(User.last_name == "Doe") \
    .update({"email": "johndoe@gmail.com"})

session.commit()