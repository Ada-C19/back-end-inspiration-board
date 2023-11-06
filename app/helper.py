from flask import abort, make_response, jsonify

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({'message':f'{cls.__name__} {model_id} invalid'}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({'message':f'{cls.__name__} {model_id} not found'}, 404))
    
    return model

def validate_message(message):
    if not message:
        return make_response(jsonify(errors=[{"field": "cardMessage", "message": "Message is required"}]), 400)
    
    if len(message) > 40:
        return make_response(jsonify(errors=[{"field": "cardMessage", "message": "Message should not exceed 40 characters"}]), 400)