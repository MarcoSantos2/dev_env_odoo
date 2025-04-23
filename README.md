# Odoo Real Estate Module

A custom Odoo module for managing real estate properties, offers, and property characteristics. This module allows real estate agencies to manage their property listings, track offers, and organize properties by types and tags.

## Features

### Property Management
- Create and manage property listings with detailed information:
  - Basic details (name, description, postcode)
  - Pricing (expected price, selling price)
  - Property characteristics (bedrooms, living area, facades)
  - Additional features (garage, garden, garden orientation)
  - Availability dates
  - Property status tracking

### Property Types
- Categorize properties by type
- Manage different property types through a dedicated menu
- Associate properties with specific types

### Property Tags
- Flexible tagging system for properties
- Custom tags with attributes:
  - Cozy indicator
  - Renovation status
- Easy tag management through the Settings menu

### Offer Management
- Track and manage offers for properties
- Record offer details:
  - Offer price
  - Partner information
  - Offer status (Accepted/Refused)
- Inline offer creation and editing
- View all offers associated with a property

## Technical Details

### Models
- `estate.property`: Main property model
- `estate.property.type`: Property type classification
- `estate.property.tag`: Property tagging system
- `estate.property.offer`: Property offers management

### Views
- List views for properties, types, tags, and offers
- Detailed form views with:
  - Property information organized in tabs
  - Inline offer management
  - Tag management with many2many widget
- Search views with filtering and grouping options

### Menu Structure
- Root menu: Real Estate
  - Advertisements
    - Properties
  - Settings
    - Property Types
    - Property Tags

## Installation

1. Clone this repository into your Odoo addons directory:
```bash
git clone [repository-url] /path/to/odoo/addons/estate
```

2. Update your Odoo configuration to include the module's path:
```conf
[options]
addons_path = /path/to/odoo/addons,/path/to/odoo/addons/estate
```

3. Restart your Odoo server

4. Install the module:
   - Go to Apps
   - Search for "Real Estate"
   - Click Install

## Usage

1. Start by creating property types and tags in the Settings menu
2. Create properties under the Advertisements menu
3. Add relevant details, tags, and types to properties
4. Record and manage offers for properties
5. Track property status changes

## Dependencies

- Odoo 18.0
- Base Odoo modules (`base`)

## Author

Marco
