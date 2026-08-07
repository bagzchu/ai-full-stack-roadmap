from errors import AppError, UnAuthorizedError, ResourceNotFoundError, ValidationError

#mock database
USER_DATABASE = {
                    101: {
                        "name": "Ram", "role": "Admin", "age": 44
                    }
                }

def fetch_and_update_user(user_id: int, age: int) -> dict:
    if age <= 0:
        raise ValidationError("Age must be a positive integer")

    if user_id not in USER_DATABASE:
        raise ResourceNotFoundError(resource_name="User", resource_id=str(user_id))

    USER_DATABASE[user_id]["age"] = age
    return USER_DATABASE[user_id]