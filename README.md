# AI-Assisted Clothing Donation Management System

A web-based platform for charitable organizations to manage and track donated clothing items using AI-powered classification, rule-based categorization, and heuristic-based recommendations.

## Quick Start

### Prerequisites
- Python 3.8+
- MySQL 5.7+
- Git

### Installation

1. Clone repository
```bash
git clone https://github.com/zixuan25/clothing-donation-ai.git
cd clothing-donation-ai
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure database
- Update MySQL credentials in `backend/config.py`
- Run: `python database/init_db.py`

5. Run application
```bash
cd backend
python app.py
```

Visit http://localhost:5000

## Features
- ✅ User Authentication
- ✅ Image Upload & AI Classification
- ✅ Inventory Management
- ✅ Real-time Tracking
- ✅ Smart Distribution Recommendations

## Project Structure
```
clothing-donation-ai/
├── frontend/          # Web UI
├── backend/           # Flask API
├── ai_model/          # AI/ML components
├── database/          # Database schema
└── uploads/           # Uploaded images
```

## API Endpoints
- POST `/api/auth/register` - Register user
- POST `/api/auth/login` - Login user
- POST `/api/items/upload` - Upload clothing image
- GET `/api/items` - Get all items
- PUT `/api/items/<id>` - Update item
- DELETE `/api/items/<id>` - Delete item
- GET `/api/inventory` - Get inventory status

## Status
🚀 In Active Development