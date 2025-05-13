from ninja import Router
from blog_api.schemas.auth import (
    UserLoginSchema, 
    UserRegistrationSchema,
    UserOutSchema
)
from blog_api.services.auth import auth_service

router = Router(tags=['Auth'])

@router.post('auth/login/')
def user_login(request, user_login_data: UserLoginSchema):
    return auth_service.user_login(request, user_login_data)


@router.post('auth/register/', response=UserOutSchema)
def register_user(request, user_register_data: UserRegistrationSchema):
    return auth_service.register_user(user_register_data)


@router.post('auth/logout/')
def user_logout(request):
    return auth_service.user_logout(request)
    