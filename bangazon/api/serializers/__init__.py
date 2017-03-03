# __all__ = ['customer_serializer', 'line_item_serializer',
# 'product_type_serializer', 'product_serializer',
# 'payment_type_serializer','customer_order_serializer']
from .customer_order_serializer import OrderSerializer
from .customer_serializer import CustomerSerializer
from .line_item_serializer import LineItemSerializer
from .payment_type_serializer import PaymentTypeSerializer
from .product_serializer import ProductSerializer
from .product_type_serializer import ProductTypeSerializer