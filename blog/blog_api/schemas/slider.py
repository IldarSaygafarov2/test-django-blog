from ninja import Schema


class SliderSchema(Schema):
    id: int
    title: str
    description: str
    image: str