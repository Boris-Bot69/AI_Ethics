# AI Ethics Literacy - Project Structure

## Recommended Folder Structure

```
AI_Ethics/
├── app.py                          # Main Streamlit application
├── requirements.txt                 # Python dependencies
├── README.md                       # Project documentation
├── .git/                          # Git repository
│
├── src/                           # Source code directory
│   ├── pages/                     # Individual page files
│   │   ├── ai_ethics_activities.py
│   │   ├── ai_ethics_scenarios.py
│   │   ├── oecd_principles.py
│   │   └── research.py
│   │
│   ├── styles/                    # CSS and styling files
│   │   └── (future CSS files)
│   │
│   ├── utils/                     # Utility functions
│   │   └── (helper functions)
│   │
│   └── components/                # Reusable components
│       └── (navigation, etc.)
│
├── docs/                          # Documentation
│   └── (project docs)
│
├── config/                        # Configuration files
│   └── (settings, etc.)
│
└── tests/                         # Test files
    └── (unit tests, etc.)
```

## Current Files Status

✅ **Main Application**: `app.py` (recreated)
✅ **Page Files**: All 4 page files are present
✅ **Dependencies**: `requirements.txt`
✅ **Documentation**: `README.md`

## Next Steps

1. **Move page files** to `src/pages/` directory
2. **Extract CSS** to separate files in `src/styles/`
3. **Create utility functions** in `src/utils/`
4. **Organize components** in `src/components/`

## Benefits of This Structure

- **Separation of Concerns**: Pages, styles, and utilities are organized
- **Maintainability**: Easy to find and modify specific components
- **Scalability**: Easy to add new pages and features
- **Professional**: Follows industry best practices
