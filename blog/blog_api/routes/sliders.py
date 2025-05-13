from ninja import Router
from blog_api.schemas.slider import SliderSchema
from blog_app.models import Slider
from django.shortcuts import get_object_or_404

router = Router(tags=['Slider'])


@router.get('/sliders/', response=list[SliderSchema])
def get_slider_items(request):
    items = Slider.objects.all()
    return items

