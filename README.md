# AI Ethics Literacy Website

A modern, responsive website focused on AI ethics literacy education, built from a Figma design template. This project provides an interactive platform for learning about AI ethics through scenarios, activities, and OECD principles.

## 🚀 **Two Versions Available:**

### **1. Static HTML Version** (`index.html`, `styles.css`, `script.js`)

- Pure HTML/CSS/JavaScript implementation
- No dependencies required
- Open `index.html` directly in browser

### **2. Streamlit Application** (`app.py`)

- Interactive web application with Streamlit
- Enhanced features with interactive components
- Easy deployment and sharing

## 🎨 Design Features

- **Clean, Modern Interface**: Minimalist design with ample white space
- **Custom Icons**: Hand-crafted CSS icons including school supplies (paperclip, magnifying glass, scissors, eraser, pencil, thumbtack, binder clip, ruler, pencil sharpener)
- **Soft Color Palette**: Light green (#90EE90), peach (#FFB6C1), and yellow (#FFD700) accents
- **Responsive Design**: Fully responsive across all device sizes
- **Interactive Elements**: Hover effects, smooth animations, and engaging user interactions

## 🚀 Features

### Navigation

- Clean horizontal navigation bar with dividers
- Active state indicators
- Smooth scrolling between sections

### Hero Section

- Large, bold typography for main title
- Descriptive paragraph with highlighted text
- Call-to-action button with hover effects
- Custom background shapes and decorative elements
- Definition blocks with colored bullet points

### AI Ethics Scenarios

- Two-column card layout
- Image placeholders for future content
- Descriptive text about AI ethics scenarios
- Interactive buttons with color-coded themes

### OECD Principles

- Custom clipboard illustrations
- Two-column layout for codebook and guiding questions
- Detailed descriptions of OECD AI principles
- Interactive clipboard elements

### Publications Section

- Academic citation format
- Clean card-based layout
- Hover effects for better user experience

## 🛠️ Technical Implementation

### HTML Structure

- Semantic HTML5 elements
- Accessible markup with proper ARIA labels
- Clean, organized structure

### CSS Features

- **Custom Icons**: All decorative elements created with pure CSS
- **CSS Grid & Flexbox**: Modern layout techniques
- **CSS Animations**: Smooth transitions and hover effects
- **Responsive Design**: Mobile-first approach
- **Custom Properties**: Organized color scheme

### JavaScript Functionality

- Smooth scrolling navigation
- Interactive hover effects
- Scroll-triggered animations
- Keyboard navigation support
- Scroll-to-top button
- Loading animations

### Streamlit Features (app.py)

- **Interactive Quiz**: AI ethics knowledge assessment
- **OECD Principles Explorer**: Interactive principle selector with detailed explanations
- **Real-time Updates**: Automatic reloading when code changes
- **Easy Deployment**: Simple deployment to Streamlit Cloud
- **Responsive Design**: Works on all devices and screen sizes

## 🎯 Custom Icons Created

All icons are built using pure CSS:

1. **Paperclip** - Curved wire with circular end
2. **Magnifying Glass** - Circle with handle
3. **Scissors** - Two crossed blades
4. **Eraser** - Pink rectangular block
5. **Pencil** - Brown shaft with yellow tip
6. **Thumbtack** - Red circle with triangular point
7. **Binder Clip** - Metal clip with curved arms
8. **Ruler** - Strip with measurement marks
9. **Pencil Sharpener** - Red container with circular opening

## 📱 Responsive Design

- **Desktop**: Full two-column layout
- **Tablet**: Adjusted spacing and single-column sections
- **Mobile**: Stacked layout with optimized typography

## 🎨 Color Scheme

- **Primary Text**: #333 (Dark Gray)
- **Background**: #FFFFFF (White)
- **Green Accent**: #90EE90 (Light Green)
- **Peach Accent**: #FFB6C1 (Light Peach)
- **Yellow Accent**: #FFD700 (Gold)
- **Red Accent**: #FF6B6B (Light Red)

## 🚀 Getting Started

### **Option 1: Static HTML Version**

1. **Clone the repository**

   ```bash
   git clone [repository-url]
   cd AI_Ethics
   ```

2. **Open in browser**
   ```bash
   # Simply open index.html in your web browser
   # Or use a local server:
   python -m http.server 8000
   # Then visit http://localhost:8000
   ```

### **Option 2: Streamlit Application**

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run Streamlit app**

   ```bash
   streamlit run app.py
   ```

3. **Access the application**
   - Open your browser to `http://localhost:8501`
   - The app will automatically reload when you make changes

### **Development**

- **HTML Version**: Edit `index.html`, `styles.css`, `script.js`
- **Streamlit Version**: Edit `app.py` for content and functionality

## 📁 File Structure

```
AI_Ethics/
├── index.html          # Main HTML structure (Static Version)
├── styles.css          # All CSS styles and custom icons
├── script.js           # JavaScript functionality
├── app.py              # Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## 🎯 Key Features

### Accessibility

- Keyboard navigation support
- Focus indicators
- Semantic HTML structure
- Screen reader friendly

### Performance

- Optimized CSS animations
- Efficient JavaScript
- Minimal dependencies
- Fast loading times

### User Experience

- Smooth animations
- Interactive elements
- Clear visual hierarchy
- Intuitive navigation

## 🔧 Customization

### Adding New Icons

Icons are created using CSS pseudo-elements. To add a new icon:

1. Add HTML element with appropriate class
2. Create CSS rules using `::before` and `::after` pseudo-elements
3. Use CSS transforms and positioning for complex shapes

### Modifying Colors

Update the CSS custom properties in `styles.css`:

```css
:root {
  --primary-green: #90ee90;
  --primary-peach: #ffb6c1;
  --primary-yellow: #ffd700;
  --primary-red: #ff6b6b;
}
```

### Adding New Sections

Follow the existing pattern:

1. Add HTML structure
2. Create CSS styles
3. Add JavaScript interactions if needed

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For questions or support, please open an issue in the repository.

---

**Built with ❤️ for AI Ethics Education**
