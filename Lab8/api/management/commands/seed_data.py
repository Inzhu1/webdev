from django.core.management.base import BaseCommand
from api.models import Category,Product

class Command(BaseCommand):
    help='Заполняет базу данных тетсовыми данными'
    
    def handle(self,*args,**options):
        electronics=Category.objects.create(name='Electronics')
        clothes=Category.objects.create(name='Clothes')
        books=Category.objects.create(name='Books')
        
        Product.objects.create(
            name='Phone',
            price=800000,
            description='A powerful smartphone with an excellent camera',
            count=10,
            is_active=True,
            category=electronics
        )
        
        Product.objects.create(
            name='Laptop',
            price=600000,
            description='A laptop for work and play',
            count=5,
            is_active=True,
            category=electronics
        )
        
        Product.objects.create(
            name='TV',
            price=500000,
            description='Samsung Smart TV',
            count=7,
            is_active=True,
            category=electronics
        )
        
        Product.objects.create(
            name='T-Shirt',
            price=25000,
            description='Coton T-Shirt',
            count=20,
            is_active=True,
            category=clothes
        )
        
        Product.objects.create(
            name='Jeans',
            price=30000,
            description='Straight Jeans',
            count=15,
            is_active=True,
            category=clothes
        )
        
        Product.objects.create(
            name='Dress',
            price=50000,
            description='Black mini dress',
            count=8,
            is_active=True,
            category=clothes
        )
        
        Product.objects.create(
            name='Python for beginners',
            price=8000,
            description='Python tutorial book',
            count=10,
            is_active=True,
            category=books
        )
        
        Product.objects.create(
            name='Harry Potter',
            price=15000,
            description='Harry Potter book Part 1',
            count=7,
            is_active=True,
            category=books
        )
        
        self.stdout.write(self.style.SUCCESS('Test data added successfully!'))