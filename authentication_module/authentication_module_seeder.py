# from django_seed import Seed
# from models import User
# from django.conf import settings
# import os
# import random
# import django
# from faker import Faker

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Role_base_system.settings')

# django.setup()

# fake = Faker()
# def generate_fake_user(num_users):
#     for _ in range(num_users):
#         email = fake.email()
#         name = fake.name()
#         date_of_birth = fake.date_of_birth()
#         gender = random.choice(['male','female'])
#         password = fake.password()
#         role_id = 4
#         phone = fake.phone_number()
#         address = fake.address()

#         user = User.objects.create_user(
#             email=email,
#             password=password,
#             name=name,
#             phone=phone,
#             date_of_birth=date_of_birth,
#             gender=gender,
#             address=address,
#             role_id=role_id)
#         user.save()

# num_users_to_generate = 5
# generate_fake_user(num_users_to_generate)
