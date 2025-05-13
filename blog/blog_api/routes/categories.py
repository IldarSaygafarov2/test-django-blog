# PUT - обновляет все поля в таблице при запросе
# PATCH - обновляет поля частично
# POST - отправка данных

from ninja import Router
from django.shortcuts import get_object_or_404
from blog_app.models import Category
from blog_api.schemas.category import CategorySchema, CategoryCreateSchema
from slugify import slugify


router = Router(tags=['Categories'])


@router.get('/categories/', response=list[CategorySchema])
def get_all_categories(request):
    categories = Category.objects.all()
    return categories

#cat = Category.objects.filter(id=5).first()
# if cat is not None:
#   return cat
# else:
#   return {'detail': 'not found'}
@router.get('/categories/{category_id}/', response=CategorySchema)
def get_category_detail(request, category_id: int):
    category = get_object_or_404(Category, pk=category_id)
    return category
    
    
@router.post('/categories/', response=CategorySchema)
def create_new_category(request, data: CategoryCreateSchema):
    new_category = Category.objects.create(
        name=data.name,
        slug=slugify(data.name)
    )
    return new_category
    
