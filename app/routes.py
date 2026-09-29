from flask import Blueprint, jsonify, request
from .models import Book, CustomerOrder

main = Blueprint('main', __name__)

# 临时内存存储
inventory = []
orders = []

# --- Story 4: Inventory CRUD ---

@main.route('/inventory', methods=['GET'])
def get_inventory():
    """获取所有库存列表"""
    result = [{'title': b.title, 'author': b.author, 'second_hand': b.is_second_hand} for b in inventory]
    return jsonify(result), 200

@main.route('/inventory', methods=['POST'])
def add_book():
    """添加新书（按数量）或二手书（按独立物品）"""
    data = request.get_json()
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({'error': 'Missing title or author'}), 400
    
    book = Book(data['title'], data['author'], data.get('is_second_hand', False))
    inventory.append(book)
    return jsonify({'message': 'Book added successfully', 'book': data}), 201

@main.route('/inventory/<int:index>', methods=['PUT'])
def update_book(index):
    """更新库存中指定书籍的信息"""
    if index >= len(inventory) or index < 0:
        return jsonify({'error': 'Book not found'}), 404
    
    data = request.get_json()
    inventory[index].title = data.get('title', inventory[index].title)
    inventory[index].author = data.get('author', inventory[index].author)
    return jsonify({'message': 'Book updated successfully'}), 200

@main.route('/inventory/<int:index>', methods=['DELETE'])
def delete_book(index):
    """删除指定书籍"""
    if index >= len(inventory) or index < 0:
        return jsonify({'error': 'Book not found'}), 404
    
    inventory.pop(index)
    return jsonify({'message': 'Book deleted successfully'}), 200

# --- Story 6: Order Management (占位，先不写) ---
@main.route('/orders')
def orders_page():
    return "Orders page"