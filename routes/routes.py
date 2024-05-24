from flask import Blueprint, request, jsonify
from db import db
from models import Blog

bp = Blueprint('routes', __name__)

@bp.route('/blogs', methods=['GET'])
def get_all_blogs():
    blogs = Blog.query.all()
    return jsonify([{
        'id': blog.id,
        'title': blog.title,
        'description': blog.description,
        'category': blog.category
    } for blog in blogs])

@bp.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog_by_id(blog_id):
    blog = Blog.query.get(blog_id)
    if blog:
        return jsonify({
            'id': blog.id,
            'title': blog.title,
            'description': blog.description,
            'category': blog.category
        })
    return jsonify({'error': 'Blog not found'}), 404

@bp.route('/blogs', methods=['POST'])
def post_blog():
    data = request.json
    new_blog = Blog(
        title=data.get('title'),
        description=data.get('description'),
        category=data.get('category')
    )
    db.session.add(new_blog)
    db.session.commit()
    return jsonify({
        'id': new_blog.id,
        'title': new_blog.title,
        'description': new_blog.description,
        'category': new_blog.category
    }), 201

@bp.route('/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    data = request.json
    blog = Blog.query.get(blog_id)
    if blog:
        blog.title = data.get('title', blog.title)
        blog.description = data.get('description', blog.description)
        blog.category = data.get('category', blog.category)
        db.session.commit()
        return jsonify({
            'id': blog.id,
            'title': blog.title,
            'description': blog.description,
            'category': blog.category
        })
    return jsonify({'error': 'Blog not found'}), 404
