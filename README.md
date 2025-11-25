# AI Mesh Transformer - Condenser Firewall Inspection System

A comprehensive Streamlit application showcasing an AI-powered multimodal inspection system for condenser firewall assemblies at Tata Motors' Harrier/Safari production line.

## 🚀 Features

- **Executive Summary**: Key performance indicators and project overview
- **Context & Problem Statement**: Manufacturing challenges and proposed solutions
- **Defect Taxonomy**: Comprehensive classification of defects and sensor modalities
- **AI Architecture**: Detailed Mesh Transformer architecture visualization
- **3D Sensor Placement**: Interactive 3D visualization of condenser with sensor positions
- **Defect Detection Flow**: Step-by-step inspection pipeline
- **ROI Calculator**: Interactive financial analysis tool
- **Implementation Timeline**: Project milestones and Gantt chart
- **References**: Documentation and resource links

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager

## 🛠️ Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Running Locally

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

## ☁️ Deployment to Streamlit Community Cloud

1. **Create a GitHub repository** and push this code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Sign up/Login** to [Streamlit Community Cloud](https://streamlit.io/cloud)

3. **Deploy your app**:
   - Click "New app"
   - Select your GitHub repository
   - Choose the branch (usually `main`)
   - Set the main file path to `app.py`
   - Click "Deploy"

4. **Your app will be live** at `https://your-app-name.streamlit.app`

## 📁 Project Structure

```
.
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── assets/            # (Optional) Place images, videos, etc. here
```

## 🎨 Customization

### Adding Images
- Place images in an `assets/` folder
- Update image paths in `app.py` to reference local files or URLs

### Adding Videos
- Embed YouTube videos using Streamlit's `st.video()` or iframe HTML
- Update video URLs in the References section

### Modifying Data
- Edit defect taxonomy data in the "Defect Taxonomy" section
- Update timeline data in the "Implementation Timeline" section
- Adjust sensor positions in the "Sensor Placement" section

## 📊 Key Metrics

- **Defect Detection Accuracy**: 98.5%
- **Cycle Time**: 5.2 seconds per unit
- **ROI Breakeven**: 17 months
- **False Positive Rate**: < 0.5%

## 🔧 Technical Stack

- **Frontend**: Streamlit
- **Visualization**: Plotly
- **Data Processing**: Pandas, NumPy
- **3D Rendering**: Plotly 3D

## 📝 Notes

- The app uses placeholder images and links. Replace with actual resources before deployment.
- Some features (like 3D defect overlays) are simulated. Full implementation would require additional 3D modeling libraries.
- The ROI calculator uses realistic but example values. Adjust based on actual project data.

## 🤝 Contributing

This is a project-specific application. For modifications, please contact the project team.

## 📄 License

Proprietary - Tata Motors Ltd.

## 👥 Project Team

- **Lead Researcher**: Dr. Arvind Mathur
- **Organization**: Tata Motors Ltd.
- **Location**: Pimpri-Chinchwad Manufacturing Plant

---

**Last Updated**: 2024

