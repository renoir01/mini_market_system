# Mini Market Inventory System

## Introduction
The Mini Market Inventory System is a web application built with Django to manage inventory, sales, and user accounts for a small market. It provides RESTful APIs and a user-friendly interface for different user roles: Admin, Staff, and Cashier.

## Features
- **Inventory Management**: CRUD operations for products and categories, stock level tracking.
- **Sales Management**: Point of Sale (POS) system, sales reporting, handling returns and exchanges.
- **User Management**: Role-based access control, profile management.
- **Role-Based Access Control**: Different permissions for Admin, Staff, and Cashier roles.
- **Comprehensive Logging**: Audit trails for critical operations.
- **Error Handling**: Consistent error response format with standard HTTP status codes.

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/mini_market_inventory.git
   cd mini_market_inventory
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000/`

## Usage Guidelines
- **Admin**: Access to all system features, manage user accounts and permissions, configure system settings.
- **Staff**: Manage inventory, process sales and returns, generate sales reports.
- **Cashier**: Access to POS system, process sales transactions, handle returns and exchanges.

## Developer Notes
- Follow PEP 8 coding standards.
- Use Django best practices for maintainability and scalability.
- Ensure comprehensive unit tests for all critical functionalities.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.