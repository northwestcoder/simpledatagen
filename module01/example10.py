from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask
from marshmallow import Schema, fields

# Create an APISpec
spec = APISpec(
    title="Swagger Petstore",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Optional marshmallow support
class CategorySchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)


class PetSchema(Schema):
    category = fields.List(fields.Nested(CategorySchema))
    name = fields.Str()


# Optional Flask support
app = Flask(__name__)


@app.route("/random")
def random_pet():
    """A cute furry animal endpoint.
    ---
    get:
      description: Get a random pet
      responses:
        200:
          content:
            application/json:
              schema: PetSchema
    """
    pet = get_random_pet()
    return PetSchema().dump(pet)


# Register the path and the entities within it
with app.test_request_context():
    spec.path(view=random_pet)


