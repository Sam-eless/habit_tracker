from rest_framework.generics import CreateAPIView

from users.models import User
from users.user_serializer import UserSerializer


# Create your views here.
class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
