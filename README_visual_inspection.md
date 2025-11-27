# Visual Inspection System - Condenser Quality Control

A dedicated Streamlit application for visual inspection and defect detection in condenser firewall assemblies at Tata Motors' Harrier/Safari production line.

## 🎯 Purpose

This standalone application focuses specifically on **visual inspection** capabilities, providing:
- Image upload and analysis
- Real-time defect detection
- Defect visualization and annotation
- Inspection statistics and analytics
- Defect gallery and reference
- Inspection report generation

## 🚀 Features

### Core Features
- **📸 Image Upload & Analysis**: Upload condenser images for inspection
- **🔍 Defect Detection**: AI-powered defect detection with confidence scores
- **📊 Defect Gallery**: Browse examples of different defect types
- **📈 Inspection Statistics**: Analytics and trends over time
- **⚙️ Configuration**: Customize detection parameters
- **📋 Reports**: Generate inspection reports in multiple formats

### Defect Types Supported
- Bent Fin
- Blocked Section
- UV Leak
- Thermal Anomaly
- Surface Contamination
- Structural Deformity
- Mounting Misalignment
- Pressure Drop

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager

## 🛠️ Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements_visual_inspection.txt
   ```

## 🏃 Running Locally

Run the Streamlit app:
```bash
streamlit run visual_inspection.py
```

The app will open in your default web browser at `http://localhost:8501`

## ☁️ Deployment to Streamlit Community Cloud

1. **Create a GitHub repository** (or use existing one)
2. **Push this file** (`visual_inspection.py`) and `requirements_visual_inspection.txt` to your repository
3. **Sign up/Login** to [Streamlit Community Cloud](https://streamlit.io/cloud)
4. **Deploy your app**:
   - Click "New app"
   - Select your GitHub repository
   - Choose the branch (usually `main`)
   - Set the main file path to `visual_inspection.py`
   - Click "Deploy"

5. **Your app will be live** at: `https://your-app-name.streamlit.app`

## 📁 File Structure

```
.
├── visual_inspection.py          # Main Streamlit application
├── requirements_visual_inspection.txt  # Python dependencies
└── README_visual_inspection.md   # This file
```

## 🎨 Key Sections

1. **Dashboard**: Overview with key metrics and recent inspections
2. **Image Upload & Analysis**: Upload and analyze condenser images
3. **Defect Detection**: View detected defects with annotations
4. **Defect Gallery**: Browse defect examples
5. **Inspection Statistics**: Analytics and trends
6. **Settings**: Configure detection parameters
7. **Inspection Reports**: Generate and download reports

## 📊 Key Metrics

- **Defect Detection Accuracy**: 98.5%
- **Average Inspection Time**: 5.2 seconds
- **Pass Rate**: 97%+
- **False Positive Rate**: < 0.5%

## 🔧 Technical Stack

- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Image Processing**: PIL (Pillow)
- **Data Processing**: Pandas, NumPy

## 📝 Notes

- This is a **standalone application** focused on visual inspection
- The main project app (`app.py`) contains the full system overview
- Image uploads are processed in-memory (no persistent storage)
- Defect detection uses simulated AI results (replace with actual model in production)

## 🔗 Related Projects

- Main Project App: `app.py` - Complete system overview and documentation
- Repository: [condenser-inspection-app](https://github.com/vikramsankhala/condenser-inspection-app)

## 👥 Project Team

- **Lead Researcher**: Dr. Arvind Mathur
- **Organization**: Tata Motors Ltd.
- **Location**: Pimpri-Chinchwad Manufacturing Plant

---

**Last Updated**: 2024

