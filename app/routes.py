from flask import Blueprint, jsonify, request
from .models import Book, CustomerOrder

main = Blueprint('main', __name__)

# 临时内存存储（后续 Yuxuan 测试时会用到）
inventory = []
orders = []

@main.route('/inventory')
def inventory_page():
    return "Inventory page"

@main.route('/orders')
def orders_page():
    return "Orders page"