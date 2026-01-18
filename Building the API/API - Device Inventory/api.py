from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError, validates_schema

app = Flask(__name__)

# Dictionary to mimic the database
devices = {
    "001": {"id": "001", "name": "Light bulb", "location": "hall", "status": "off"},
    "002": {"id": "002", "name": "Humidity sensor", "location": "bedroom", "status": "on"},
    "003": {"id": "003", "name": "Humidifier", "location": "bedroom", "status": "off"}
}


# Define Marshmallow Schema for request and response validation
class DeviceSchema(Schema):
    id = fields.Str(required=True)
    name = fields.Str(required=True)
    location = fields.Str(required=True)
    status = fields.Str(required=True)

    #Use validates_schema for custom validation logic
    @validates_schema(pass_original=True)
    def validate_required_fields(self, data, original_data, **kwargs):
        # TODO: declare a list of required_fields
        # TODO: check if the method is POST, iterate over required fields, if any of them are absent in the provided data, raise ValidationError with a custom message indicating which filed is missing.


device_schema = DeviceSchema()

@app.route('/items/<string:identifier>', methods=['GET', 'PUT', 'DELETE'])
def device(identifier):
    if request.method == 'GET':
        device = devices.get(identifier)
        if not device:
            return jsonify({'message': 'Device not found'}), 404
        return jsonify(device), 200

    elif request.method == 'PUT':
        try:
            args = device_schema.load(request.json, partial=True)
        except ValidationError as err:
            return jsonify(err.messages), 400

        if identifier not in devices:
            return jsonify({'message': 'Device not found'}), 404

        devices[identifier].update(args)
        return jsonify({"updated device": identifier}), 200

    elif request.method == 'DELETE':
        if identifier not in devices:
            return jsonify({'message': 'Device not found'}), 404
        del devices[identifier]
        return jsonify({'message': 'Device deleted'}), 200


@app.route('/items', methods=['GET', 'POST'])
def device_inventory():
    if request.method == 'GET':
        # TODO: return the list of devices in the required format

    elif request.method == 'POST':
        # TODO: try to initialize a new device using the method device_schema.load() with json data from the request, return the error message from validation in case it returns an error, with a reponse code 400

        # TODO: check it the new device id is already present in our data and if so, return an error message and code 400

        # TODO: add a new device to devices and return a success message in the required format


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
