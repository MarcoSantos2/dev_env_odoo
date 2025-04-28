# Estate Module UI Enhancement

This directory contains SCSS files that define the custom styling for the Estate Real Estate module.

## Design Decisions

### Color Palette
- **Primary Blue**: Trust, stability, and professionalism
- **Secondary Red**: For important highlights and sold properties
- **Neutrals**: Clean, modern grayscale palette for readable text and subtle backgrounds
- **Status Colors**: Distinctive colors for each property state (new, offer received, sold, etc.)

### Typography
- System fonts for better performance and native feel
- Clear hierarchy with well-defined heading and body text sizes
- Improved line-heights for better readability

### Components
- Card-based design with subtle shadows and hover effects
- Consistent border radius and spacing
- Status indicators with color coding
- Mobile-responsive layouts

### Accessibility
- Sufficient color contrast for all text
- Focus states for keyboard navigation
- Semantic markup for screen readers

## How to Update Styles

1. Edit the SCSS files in this directory
2. Rebuild the assets using one of the methods below

## Rebuilding Assets

### Method 1: From Odoo UI
1. Enable Developer Mode (Settings → Developer Tools → Activate the developer mode)
2. Go to Settings → Technical → User Interface → Assets
3. Click "Clear assets" to rebuild all assets

### Method 2: From Terminal
```bash
# Option 1: Restart the Odoo server
docker-compose restart web

# Option 2: Use the command line to clear assets
python3 odoo-bin --clear-caches
```

### Method 3: Debug=assets Parameter
Add `?debug=assets` to your URL to force asset reloading during development:
```
http://localhost:8069/web?debug=assets
```

## Adding New Style Files

1. Create a new SCSS file in this directory
2. Import it in `estate_styles.scss` or add it directly to the assets.xml file
3. Rebuild assets using one of the methods above

## Best Practices

1. Follow the established naming convention (`o-estate-*`) for variables and classes
2. Use the defined variables for colors, spacing, shadows, etc. rather than hard-coded values
3. Test responsive behavior at different screen sizes
4. Ensure sufficient contrast for accessibility 