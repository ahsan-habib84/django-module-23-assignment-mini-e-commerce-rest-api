from decimal import Decimal

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Category, Product


class StoreAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword123",
        )
        self.token = Token.objects.create(user=self.user)
        self.category = Category.objects.create(name="Phones")
        self.product = Product.objects.create(
            name="Test Phone",
            description="A test product",
            price=Decimal("500.00"),
            stock=10,
            category=self.category,
        )

    def test_product_list(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, 200)

    def test_search_product(self):
        response = self.client.get("/api/products/?search=Test")
        self.assertEqual(response.status_code, 200)

    def test_create_order_requires_authentication(self):
        response = self.client.post(
            "/api/orders/",
            {"product": self.product.id, "quantity": 2},
            format="json",
        )
        self.assertEqual(response.status_code, 401)

    def test_authenticated_order(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        response = self.client.post(
            "/api/orders/",
            {"product": self.product.id, "quantity": 2},
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.product.refresh_from_db()
        self.assertEqual(self.product.stock, 8)
