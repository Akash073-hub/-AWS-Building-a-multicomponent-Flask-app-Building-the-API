from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Dictionary to mimic the database
devices = {
    "001": {"id": "001", "name": "Light bulb", "location": "hall", "status": "off"},
    "002": {"id": "002", "name": "Humidity sensor", "location": "bedroom", "status": "on"},
    "003": {"id": "003", "name": "Humidifier", "location": "bedroom", "status": "off"}
}

# Marshmallow Schema
class DeviceSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    status = fields.Str(required=True)

device_schema = DeviceSchema()


@app.route('/items/<string:identifier>', methods=['GET', 'PUT', 'DELETE'])
def device(identifier):

    # GET device
    if request.method == 'GET':
        device = devices.get(identifier)
        if not device:
            return jsonify({'message': 'Device not found'}), 404
        return jsonify(device), 200

    # UPDATE device
    elif request.method == 'PUT':
        try:
            args = device_schema.load(request.json, partial=True)
        except ValidationError as err:
            return jsonify(err.messages), 400

        if identifier not in devices:
            return jsonify({'message': 'Device not found'}), 404

        devices[identifier].update(args)
        return jsonify({"message": "Device updated", "device": devices[identifier]}), 200

    # DELETE device
    elif request.method == 'DELETE':
        if identifier not in devices:
            return jsonify({'message': 'Device not found'}), 404

        deleted_device = devices.pop(identifier)
        return jsonify({"message": "Device deleted", "device": deleted_device}), 200


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
