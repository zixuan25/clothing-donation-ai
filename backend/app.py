from flask import Flask, render_template, jsonify
from flask_cors import CORS
from config import Config
import os

def create_app(config_class=Config):
    """Application factory function"""
    app = Flask(__name__, 
                template_folder='../frontend',
                static_folder='../frontend')
    
    app.config.from_object(config_class)
    
    # Initialize extensions
    CORS(app)
    
    # Register blueprints
    from routes.auth import auth_bp
    from routes.clothing_items import items_bp
    from routes.inventory import inventory_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(items_bp, url_prefix='/api/items')
    app.register_blueprint(inventory_bp, url_prefix='/api/inventory')
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health():
        return jsonify({'status': 'healthy'}), 200
    
    # Root route
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
