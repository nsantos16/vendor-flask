from fastapi import status

from tests.utils.config import client
from config.settings import settings
from src.constants import VENDING_MACHINE_ENDPOINT, INVENTORY_ENDPOINT, X_COINS, X_INVENTORY_REMAINING
from tests.utils.fixtures import init_db


def test_init_state_vending_machine():
    inventory_response = client.get(INVENTORY_ENDPOINT)
    assert inventory_response.status_code == status.HTTP_200_OK
    items = inventory_response.json()
    assert len(items) == 3
    for item in items:
        assert item["stock"] == 5


def test_buy_item():
    inventory_response = client.get(INVENTORY_ENDPOINT)
    assert inventory_response.status_code == status.HTTP_200_OK
    items = inventory_response.json()

    insufficient_coins_response = client.put(f"{INVENTORY_ENDPOINT}/{items[0]['id']}")
    assert insufficient_coins_response.status_code == status.HTTP_400_BAD_REQUEST
    assert insufficient_coins_response.headers[X_COINS] == "0"

    insert_coin_response = client.put(VENDING_MACHINE_ENDPOINT, json={"coin": 1})
    assert insert_coin_response.status_code == status.HTTP_204_NO_CONTENT

    double_coin_response = client.put(VENDING_MACHINE_ENDPOINT, json={"coin": 1})
    assert double_coin_response.status_code == status.HTTP_204_NO_CONTENT
    assert double_coin_response.headers[X_COINS] == "2"

    buy_item_response = client.put(f"{INVENTORY_ENDPOINT}/{items[0]['id']}")
    assert buy_item_response.status_code == status.HTTP_200_OK
    assert buy_item_response.headers[X_COINS] == "0"
    assert buy_item_response.headers[X_INVENTORY_REMAINING] == "4"


def test_buy_no_stock_item():
    inventory_response = client.get(INVENTORY_ENDPOINT)
    assert inventory_response.status_code == status.HTTP_200_OK
    items = inventory_response.json()

    item = items[1]
    assert item["stock"] == 5

    for i in range(item["stock"]):
        buy_item_response = _buy_item(item["id"])
        assert buy_item_response.status_code == status.HTTP_200_OK
        current_stock = item["stock"] - i - 1
        assert int(buy_item_response.headers[X_INVENTORY_REMAINING]) == current_stock
        assert int(buy_item_response.headers[X_COINS]) == 0

    no_stock_response = _buy_item(item["id"])
    assert no_stock_response.status_code == status.HTTP_404_NOT_FOUND
    assert int(no_stock_response.headers[X_COINS]) == 2
    assert no_stock_response.headers.get(X_INVENTORY_REMAINING) is None


def test_get_all_coins_back():
    client.put(VENDING_MACHINE_ENDPOINT, json={"coin": 1})
    client.put(VENDING_MACHINE_ENDPOINT, json={"coin": 1})
    coins_back_response = client.delete(VENDING_MACHINE_ENDPOINT)
    assert coins_back_response.status_code == status.HTTP_204_NO_CONTENT
    assert int(coins_back_response.headers[X_COINS]) == 2

    coins_back_response = client.delete(VENDING_MACHINE_ENDPOINT)
    assert coins_back_response.status_code == status.HTTP_204_NO_CONTENT
    assert int(coins_back_response.headers[X_COINS]) == 0


def test_insert_more_than_one_coin():
    if not settings.feat_flag_more_than_one_coin:
        error_response = client.put(VENDING_MACHINE_ENDPOINT, json={'coin': 2})
        assert error_response.status_code == status.HTTP_400_BAD_REQUEST
        error_response = client.put(VENDING_MACHINE_ENDPOINT, json={'coin': 0})
        assert error_response.status_code == status.HTTP_400_BAD_REQUEST
        error_response = client.put(VENDING_MACHINE_ENDPOINT, json={'coin': -2})
        assert error_response.status_code == status.HTTP_400_BAD_REQUEST


def _buy_item(item_id):
    client.put(VENDING_MACHINE_ENDPOINT, json={'coin': 1})
    client.put(VENDING_MACHINE_ENDPOINT, json={'coin': 1})
    buy_item_response = client.put(f"{INVENTORY_ENDPOINT}/{item_id}")

    return buy_item_response
