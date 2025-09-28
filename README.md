# OrderFlow - QR Code Food Ordering System

A comprehensive digital ordering platform that enables restaurants to provide contactless dining experiences through QR code-based table ordering.

## Overview

OrderFlow is a modern restaurant management and ordering system that allows customers to scan QR codes at their tables to browse menus, place orders, and manage their dining experience without staff interaction. The system provides restaurants with complete control over their menu, inventory, and order management.

## Key Features

### 🍽️ Digital Menu Management
- **Dynamic Menu System**: Create and organize menu items by categories with customizable sorting
- **Rich Item Details**: Support for descriptions, images, pricing, and spice level indicators
- **Real-time Availability**: Toggle item availability instantly across all tables
- **Allergen Management**: Comprehensive allergen tracking with contamination risk levels (contains/may contain)

### 📱 QR Code Table Ordering
- **Unique Table QR Codes**: Each table generates a unique QR code for order placement
- **Session Management**: Secure session tokens with automatic expiration
- **Multi-device Support**: Multiple customers at the same table can view and contribute to orders

### 🛒 Advanced Order Customization
- **Flexible Customization Options**: Support for required and optional modifications
- **Multiple Selection Types**: Radio buttons, checkboxes, and quantity-based options
- **Price Modifiers**: Dynamic pricing based on selected customizations
- **Special Requests**: Free-text field for specific customer requirements

### 📦 Smart Inventory Management
- **Recipe-based Tracking**: Automatic ingredient consumption calculation based on menu item recipes
- **Real-time Stock Monitoring**: Live inventory levels with minimum threshold alerts
- **Transaction History**: Complete audit trail of all inventory movements
- **Multi-category Organization**: Organize ingredients by type and storage location

### 💰 Order Processing
- **Order Status Tracking**: Real-time updates from placed to completed
- **Service Charge Calculation**: Automatic service charge and tax computation
- **Kitchen Integration**: Estimated preparation times and completion tracking

### 🏪 Multi-Restaurant Support
- **Restaurant Management**: Support for multiple restaurant locations
- **Isolated Data**: Complete data separation between different restaurants
- **Customizable Settings**: Per-restaurant configuration options

## System Architecture

### Core Components

**Restaurant Management**
- Multi-tenant architecture supporting multiple restaurant locations
- Complete restaurant profile management with contact information and descriptions

**Table & QR System**
- Dynamic QR code generation for each table
- Session-based access control with automatic cleanup
- Table status management and availability tracking

**Menu & Catalog System**
- Hierarchical category organization
- Rich media support for menu item images
- Advanced filtering and sorting capabilities

**Order Processing Engine**
- Real-time order status updates
- Integrated customization handling
- Automatic inventory deduction

**Inventory Management**
- Recipe-based ingredient tracking
- Automated stock level calculations
- Comprehensive transaction logging

## Technology Stack

The system is designed to handle high-volume restaurant operations with:
- Scalable database architecture
- Real-time order processing
- Mobile-optimized customer interface
- Restaurant staff management dashboard

## Getting Started

### Prerequisites
- Database server (MySQL/PostgreSQL)
- Web server environment
- Mobile-responsive frontend framework

### Installation
```bash
# Clone the repository
git clone [repository-url]
cd orderflow

# Install dependencies
[package-manager] install

# Configure database connection
cp .env.example .env
# Edit .env with your database credentials

# Run database migrations
[migration-command]

# Start the application
[start-command]
```

## Usage

### For Restaurants
1. **Setup**: Create restaurant profile and configure basic settings
2. **Menu Creation**: Add categories, menu items, and customization options
3. **Table Management**: Set up tables and generate QR codes
4. **Inventory Setup**: Define ingredients and recipes for accurate tracking
5. **Staff Training**: Train staff on order management and kitchen integration

### For Customers
1. **Scan QR Code**: Use any QR code scanner to access the table's menu
2. **Browse Menu**: View categories, items, and detailed information including allergens
3. **Customize Orders**: Select options and modifications as needed
4. **Place Order**: Review order summary and submit
5. **Track Progress**: Monitor order status in real-time

## Features in Detail

### Allergen Management
- Comprehensive allergen database with severity levels
- Clear contamination risk indicators (contains/may contain)
- Multi-language support through i18n keys
- Visual icons for quick identification

### Customization System
- Flexible option types (single select, multi-select, quantity)
- Required vs. optional modifications
- Dynamic pricing adjustments
- Maximum selection limits

### Inventory Intelligence
- Recipe-based consumption tracking
- Automated stock deduction on order completion
- Waste tracking and adjustment capabilities
- Supplier and restocking management

### Order Management
- Real-time status updates
- Kitchen display integration
- Service charge automation

## Security Features

- Secure QR code token generation
- Session-based access control
- Data isolation between restaurants
- Audit trails for all transactions

## Support

For technical support, feature requests, or bug reports, please contact the development team or create an issue in the project repository.

## License

[License information to be added]