from django_seed import Seed
from models import Role

seeder = Seed.seeder()

roles_data = {'role_id': 6,'role_name':'demo'}

for role_data in roles_data:
    seeder.add_entity(Role,1,role_data)

seeder.execute()