# Выбери какой уровень использовать (сейчас Level 5 - Generics)
# Чтобы переключиться на другой уровень, просто раскомментируй нужную строку

# Level 2: FBV
# from .fbv import products_list, product_detail

# Level 3: CBV
# from .cbv import ProductListAPIView, ProductDetailAPIView

# Level 4: Mixins
# from .mixins import ProductListAPIView, ProductDetailAPIView

# Level 5: Generics (активный)
from .generics import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryProductsAPIView
)