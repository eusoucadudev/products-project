from fastapi.testclient import TestClient
from fastapi import status
from app.db.models import Product as ProductModel
from app.main import app

client = TestClient(app=app)

def test_add_product_route(db_session, categories_on_db):
    body = {
        "category_slug": categories_on_db[0].slug,
        "product": {
            "name": "Camisa Mike",
            "slug": "camisa-mike",
            "price": 23.99,
            "stock": 23,
        }
    }

    response = client.post(url="/product/add", json=body)

    assert response.status_code == status.HTTP_201_CREATED

    products_on_db = db_session.query(ProductModel).all()

    assert len(products_on_db) == 1
    db_session.delete(products_on_db[0])
    db_session.commit()


def test_add_product_route_invalid_category_slug(db_session, categories_on_db):
    body = {
        "category_slug": categories_on_db[0].slug,
        "product": {
            "name": "Camisa Mike",
            "slug": "camisa-mike",
            "price": 23.99,
            "stock": 23,
        }
    }

    response = client.post(url="/product/add", json=body)

    assert response.status_code == status.HTTP_201_CREATED

    products_on_db = db_session.query(ProductModel).all()

    assert len(products_on_db) == 1
    db_session.delete(products_on_db[0])
    db_session.commit()