from django.core.management.base import BaseCommand
from api.models import Category, Product

class Command(BaseCommand):
    help = 'Fill database with test data'
    
    def handle(self, *args, **options):
        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()
        
        # Create 4 categories
        categories = [
            'Electronics',
            'Clothes', 
            'Books',
            'Food'
        ]
        
        category_objs = {}
        for cat_name in categories:
            category_objs[cat_name] = Category.objects.create(name=cat_name)
        
        # Create 20 products
        products_data = [
            # Electronics (5 products)
            {'name': 'iPhone 15', 'price': 999, 'description': 'Apple smartphone', 'count': 15, 'category': 'Electronics'},
            {'name': 'Samsung Galaxy', 'price': 899, 'description': 'Android smartphone', 'count': 12, 'category': 'Electronics'},
            {'name': 'MacBook Pro', 'price': 1999, 'description': 'Apple laptop', 'count': 8, 'category': 'Electronics'},
            {'name': 'Sony Headphones', 'price': 299, 'description': 'Wireless headphones', 'count': 20, 'category': 'Electronics'},
            {'name': 'iPad Air', 'price': 599, 'description': 'Apple tablet', 'count': 10, 'category': 'Electronics'},
            
            # Clothes (5 products)
            {'name': 'T-Shirt', 'price': 29, 'description': 'Cotton t-shirt', 'count': 50, 'category': 'Clothes'},
            {'name': 'Jeans', 'price': 79, 'description': 'Blue jeans', 'count': 30, 'category': 'Clothes'},
            {'name': 'Jacket', 'price': 149, 'description': 'Winter jacket', 'count': 15, 'category': 'Clothes'},
            {'name': 'Sneakers', 'price': 99, 'description': 'Sports shoes', 'count': 25, 'category': 'Clothes'},
            {'name': 'Hat', 'price': 19, 'description': 'Baseball cap', 'count': 40, 'category': 'Clothes'},
            
            # Books (5 products)
            {'name': 'Python Crash Course', 'price': 39, 'description': 'Learn Python', 'count': 20, 'category': 'Books'},
            {'name': 'Django for Beginners', 'price': 49, 'description': 'Web development', 'count': 15, 'category': 'Books'},
            {'name': 'Harry Potter', 'price': 29, 'description': 'Fantasy novel', 'count': 25, 'category': 'Books'},
            {'name': 'The Hobbit', 'price': 24, 'description': 'Adventure story', 'count': 18, 'category': 'Books'},
            {'name': '1984', 'price': 19, 'description': 'Classic novel', 'count': 22, 'category': 'Books'},
            
            # Food (5 products)
            {'name': 'Apple', 'price': 1, 'description': 'Fresh apple', 'count': 100, 'category': 'Food'},
            {'name': 'Banana', 'price': 1, 'description': 'Ripe banana', 'count': 80, 'category': 'Food'},
            {'name': 'Bread', 'price': 3, 'description': 'Fresh bread', 'count': 30, 'category': 'Food'},
            {'name': 'Milk', 'price': 4, 'description': 'Whole milk', 'count': 40, 'category': 'Food'},
            {'name': 'Cheese', 'price': 6, 'description': 'Cheddar cheese', 'count': 25, 'category': 'Food'},
        ]
        
        for product_data in products_data:
            category_name = product_data.pop('category')
            category = category_objs[category_name]
            Product.objects.create(category=category, is_active=True, **product_data)
        
        self.stdout.write(self.style.SUCCESS(f'Added {Category.objects.count()} categories and {Product.objects.count()} products!'))