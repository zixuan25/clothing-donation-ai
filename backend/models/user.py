from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    """User model"""
    
    def __init__(self, username, email, password, organization=None):
        self.id = None
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.organization = organization
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.is_active = True
    
    def check_password(self, password):
        """Verify password"""
        return check_password_hash(self.password_hash, password)
    
    def set_password(self, password):
        """Set new password"""
        self.password_hash = generate_password_hash(password)
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'organization': self.organization,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active
        }
