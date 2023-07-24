from flask import make_response, abort

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__.lower()} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message":f"{cls.__name__.lower()} {model_id} not found"}, 404))

    return model

def check_character_limit(request_body, text_string):
    if len(request_body.get(text_string)) > 40:
        abort(make_response({"details": f"{text_string.capitalize()} must be under 40 characters."}, 400))
    if len(request_body.get(text_string)) == 0:
        abort(make_response({"details": f"{text_string.capitalize()} cannot be empty."}, 400))