import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import io
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="Visual Inspection System - Condenser Quality Control",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .defect-box {
        border: 2px solid #ff4444;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        background-color: #fff5f5;
    }
    .pass-box {
        border: 2px solid #44ff44;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        background-color: #f5fff5;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'inspection_history' not in st.session_state:
    st.session_state.inspection_history = []
if 'current_image' not in st.session_state:
    st.session_state.current_image = None
if 'detected_defects' not in st.session_state:
    st.session_state.detected_defects = []

# Sidebar Navigation
st.sidebar.title("🔬 Visual Inspection System")
st.sidebar.markdown("---")

section = st.sidebar.radio(
    "Navigate to:",
    [
        "🏠 Dashboard",
        "📸 Image Upload & Analysis",
        "🔍 Defect Detection",
        "📊 Defect Gallery",
        "📈 Inspection Statistics",
        "⚙️ Settings & Configuration",
        "📋 Inspection Reports"
    ]
)

# ============================================================================
# DASHBOARD
# ============================================================================
if section == "🏠 Dashboard":
    st.markdown('<div class="main-header">Visual Inspection System</div>', unsafe_allow_html=True)
    st.subheader("Condenser Quality Control - Tata Motors Harrier/Safari Line")
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>98.5%</h3>
            <p>Detection Accuracy</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>5.2s</h3>
            <p>Avg. Inspection Time</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>1,247</h3>
            <p>Units Inspected Today</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>0.3%</h3>
            <p>Rejection Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Recent Inspections
    st.subheader("Recent Inspections")
    
    # Sample inspection data
    recent_data = {
        'Unit ID': ['HAR-2024-001234', 'HAR-2024-001235', 'HAR-2024-001236', 'HAR-2024-001237', 'HAR-2024-001238'],
        'Timestamp': [
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            (datetime.now() - pd.Timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M:%S'),
            (datetime.now() - pd.Timedelta(minutes=5)).strftime('%Y-%m-%d %H:%M:%S'),
            (datetime.now() - pd.Timedelta(minutes=8)).strftime('%Y-%m-%d %H:%M:%S'),
            (datetime.now() - pd.Timedelta(minutes=12)).strftime('%Y-%m-%d %H:%M:%S')
        ],
        'Status': ['✅ PASS', '✅ PASS', '❌ FAIL', '✅ PASS', '✅ PASS'],
        'Defects Found': [0, 0, 2, 0, 0],
        'Confidence': [99.8, 98.5, 97.2, 99.1, 98.9]
    }
    
    df_recent = pd.DataFrame(recent_data)
    st.dataframe(df_recent, use_container_width=True, hide_index=True)
    
    # Defect Distribution Chart
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Defect Type Distribution (Last 24h)")
        defect_dist = {
            'Defect Type': ['Bent Fin', 'Blocked Section', 'UV Leak', 'Thermal Anomaly', 'Surface Contamination', 'Structural Deformity'],
            'Count': [12, 8, 3, 5, 15, 2]
        }
        df_dist = pd.DataFrame(defect_dist)
        
        fig = px.pie(
            df_dist,
            values='Count',
            names='Defect Type',
            title="Defect Distribution",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Inspection Status Over Time")
        time_data = pd.DataFrame({
            'Hour': range(24),
            'Passed': np.random.randint(40, 60, 24),
            'Failed': np.random.randint(0, 5, 24)
        })
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=time_data['Hour'],
            y=time_data['Passed'],
            mode='lines+markers',
            name='Passed',
            line=dict(color='#2ca02c', width=3)
        ))
        fig.add_trace(go.Scatter(
            x=time_data['Hour'],
            y=time_data['Failed'],
            mode='lines+markers',
            name='Failed',
            line=dict(color='#d62728', width=3)
        ))
        fig.update_layout(
            title="Inspection Status (24 Hours)",
            xaxis_title="Hour",
            yaxis_title="Count",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# IMAGE UPLOAD & ANALYSIS
# ============================================================================
elif section == "📸 Image Upload & Analysis":
    st.title("Image Upload & Analysis")
    
    st.write("Upload condenser images for visual inspection and defect detection.")
    
    # Image upload
    col1, col2 = st.columns([2, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Choose an image file",
            type=['png', 'jpg', 'jpeg', 'bmp', 'tiff'],
            help="Upload a condenser image for inspection"
        )
    
    with col2:
        st.subheader("Quick Actions")
        if st.button("📷 Use Sample Image", use_container_width=True):
            # Create a sample image
            sample_img = Image.new('RGB', (800, 600), color='lightblue')
            draw = ImageDraw.Draw(sample_img)
            # Draw a simple condenser representation
            for i in range(20):
                draw.rectangle([10 + i*40, 100, 30 + i*40, 500], fill='silver', outline='gray')
            st.session_state.current_image = sample_img
            uploaded_file = None
        
        if st.button("🔄 Clear Current Image", use_container_width=True):
            st.session_state.current_image = None
            st.session_state.detected_defects = []
            st.rerun()
    
    # Display uploaded image
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.session_state.current_image = image
    elif st.session_state.current_image is not None:
        image = st.session_state.current_image
    else:
        image = None
    
    if image:
        st.markdown("---")
        
        # Image information
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Image Size", f"{image.size[0]} × {image.size[1]}")
        with col2:
            st.metric("Format", image.format or "Unknown")
        with col3:
            st.metric("Mode", image.mode)
        with col4:
            file_size = len(uploaded_file.getvalue()) if uploaded_file else 0
            st.metric("File Size", f"{file_size / 1024:.1f} KB" if file_size > 0 else "N/A")
        
        st.markdown("---")
        
        # Image display with analysis options
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("Image Preview")
            st.image(image, use_container_width=True, caption="Uploaded Condenser Image")
        
        with col2:
            st.subheader("Analysis Options")
            
            analysis_mode = st.radio(
                "Select Analysis Mode:",
                ["Full Inspection", "Quick Scan", "Defect-Specific", "Custom Region"]
            )
            
            if st.button("🔍 Run Inspection", type="primary", use_container_width=True):
                # Simulate inspection
                with st.spinner("Analyzing image..."):
                    import time
                    time.sleep(1)
                    
                    # Simulate defect detection
                    defects = []
                    if np.random.random() > 0.3:  # 70% chance of finding defects
                        defect_types = ['Bent Fin', 'Surface Contamination', 'Blocked Section']
                        for _ in range(np.random.randint(1, 3)):
                            defects.append({
                                'type': np.random.choice(defect_types),
                                'confidence': np.random.uniform(85, 99),
                                'location': (np.random.randint(50, image.size[0]-50), 
                                            np.random.randint(50, image.size[1]-50)),
                                'severity': np.random.choice(['Low', 'Medium', 'High'])
                            })
                    
                    st.session_state.detected_defects = defects
                    st.success(f"Analysis complete! Found {len(defects)} potential defect(s).")
                    st.rerun()
            
            # Image enhancement options
            st.markdown("---")
            st.subheader("Image Enhancement")
            
            enhance_brightness = st.slider("Brightness", 0.5, 2.0, 1.0, 0.1)
            enhance_contrast = st.slider("Contrast", 0.5, 2.0, 1.0, 0.1)
            
            if st.button("Apply Enhancements", use_container_width=True):
                from PIL import ImageEnhance
                enhancer = ImageEnhance.Brightness(image)
                enhanced = enhancer.enhance(enhance_brightness)
                enhancer = ImageEnhance.Contrast(enhanced)
                enhanced = enhancer.enhance(enhance_contrast)
                st.session_state.current_image = enhanced
                st.rerun()

# ============================================================================
# DEFECT DETECTION
# ============================================================================
elif section == "🔍 Defect Detection":
    st.title("Defect Detection & Visualization")
    
    if st.session_state.current_image is None:
        st.warning("⚠️ Please upload an image first in the 'Image Upload & Analysis' section.")
        if st.button("Go to Image Upload"):
            st.session_state.section = "📸 Image Upload & Analysis"
            st.rerun()
    else:
        image = st.session_state.current_image
        
        # Defect detection results
        if st.session_state.detected_defects:
            st.subheader("🔴 Detected Defects")
            
            # Create annotated image
            annotated_image = image.copy()
            draw = ImageDraw.Draw(annotated_image)
            
            for i, defect in enumerate(st.session_state.detected_defects):
                x, y = defect['location']
                # Draw bounding box
                box_size = 100
                draw.rectangle(
                    [x - box_size//2, y - box_size//2, x + box_size//2, y + box_size//2],
                    outline='red',
                    width=3
                )
                # Draw label
                label = f"{defect['type']}\n{defect['confidence']:.1f}%"
                draw.text((x - box_size//2, y - box_size//2 - 20), label, fill='red')
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Annotated Image")
                st.image(annotated_image, use_container_width=True, caption="Defects Highlighted")
            
            with col2:
                st.subheader("Defect Details")
                
                for i, defect in enumerate(st.session_state.detected_defects, 1):
                    with st.expander(f"Defect #{i}: {defect['type']}", expanded=True):
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.metric("Confidence", f"{defect['confidence']:.1f}%")
                            st.metric("Severity", defect['severity'])
                        with col_b:
                            st.metric("Location", f"({defect['location'][0]}, {defect['location'][1]})")
                        
                        # Defect type information
                        defect_info = {
                            'Bent Fin': 'Fin deformation detected. May affect airflow and cooling efficiency.',
                            'Surface Contamination': 'Foreign particles or residue detected on surface.',
                            'Blocked Section': 'Obstruction detected in condenser channels.',
                            'UV Leak': 'UV-visible dye indicates potential refrigerant leak.',
                            'Thermal Anomaly': 'Temperature variation detected beyond normal range.',
                            'Structural Deformity': 'Geometric deviation from specification detected.'
                        }
                        
                        st.info(defect_info.get(defect['type'], 'Defect information not available.'))
            
            # Inspection result
            st.markdown("---")
            if len(st.session_state.detected_defects) > 0:
                st.markdown('<div class="defect-box">', unsafe_allow_html=True)
                st.markdown("### ❌ INSPECTION FAILED")
                st.write(f"**Defects Found:** {len(st.session_state.detected_defects)}")
                st.write("**Action Required:** Unit requires review and potential rework.")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="pass-box">', unsafe_allow_html=True)
                st.markdown("### ✅ INSPECTION PASSED")
                st.write("No defects detected. Unit meets quality standards.")
                st.markdown('</div>', unsafe_allow_html=True)
        
        else:
            st.info("ℹ️ No defects detected yet. Run inspection analysis to detect defects.")
            
            # Show original image
            st.subheader("Original Image")
            st.image(image, use_container_width=True)
            
            if st.button("🔍 Run Defect Detection", type="primary"):
                st.info("Please run inspection from the 'Image Upload & Analysis' section first.")
        
        # Defect classification reference
        st.markdown("---")
        st.subheader("Defect Classification Reference")
        
        defect_types = pd.DataFrame({
            'Defect Type': [
                'Bent Fin',
                'Blocked Section',
                'UV Leak',
                'Thermal Anomaly',
                'Surface Contamination',
                'Structural Deformity',
                'Mounting Misalignment',
                'Pressure Drop'
            ],
            'Severity': ['High', 'High', 'Critical', 'Medium', 'Low', 'High', 'High', 'Critical'],
            'Detection Method': [
                'RGB Camera',
                'Structured Light',
                'UV Camera',
                'Thermal IR',
                'RGB Camera',
                'RGB + Structured Light',
                'Structured Light',
                'Pressure/Temp Sensor'
            ],
            'Typical Confidence': ['99.2%', '97.8%', '98.5%', '96.5%', '95.2%', '98.9%', '99.1%', '97.5%']
        })
        
        st.dataframe(defect_types, use_container_width=True, hide_index=True)

# ============================================================================
# DEFECT GALLERY
# ============================================================================
elif section == "📊 Defect Gallery":
    st.title("Defect Gallery")
    st.write("Browse examples of different defect types detected in condenser inspections.")
    
    # Defect categories
    defect_categories = st.multiselect(
        "Filter by Defect Type:",
        options=['Bent Fin', 'Blocked Section', 'UV Leak', 'Thermal Anomaly', 
                'Surface Contamination', 'Structural Deformity', 'Mounting Misalignment'],
        default=['Bent Fin', 'Blocked Section', 'UV Leak']
    )
    
    # Sample defect gallery data
    gallery_data = []
    for defect_type in defect_categories:
        for i in range(3):
            gallery_data.append({
                'Defect Type': defect_type,
                'Unit ID': f'HAR-2024-{1000 + i}',
                'Date': (datetime.now() - pd.Timedelta(days=np.random.randint(1, 30))).strftime('%Y-%m-%d'),
                'Severity': np.random.choice(['Low', 'Medium', 'High', 'Critical']),
                'Confidence': np.random.uniform(90, 99.5),
                'Status': np.random.choice(['Rejected', 'Reworked', 'Under Review'])
            })
    
    if gallery_data:
        df_gallery = pd.DataFrame(gallery_data)
        
        # Display gallery
        cols_per_row = 3
        for idx in range(0, len(df_gallery), cols_per_row):
            cols = st.columns(cols_per_row)
            for col_idx, col in enumerate(cols):
                if idx + col_idx < len(df_gallery):
                    defect = df_gallery.iloc[idx + col_idx]
                    with col:
                        # Create placeholder image
                        img = Image.new('RGB', (300, 200), color='lightgray')
                        st.image(img, use_container_width=True)
                        
                        st.write(f"**{defect['Defect Type']}**")
                        st.write(f"Unit: {defect['Unit ID']}")
                        st.write(f"Severity: {defect['Severity']}")
                        st.write(f"Confidence: {defect['Confidence']:.1f}%")
                        st.write(f"Status: {defect['Status']}")
                        st.write(f"Date: {defect['Date']}")
        
        # Statistics
        st.markdown("---")
        st.subheader("Gallery Statistics")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Defects", len(df_gallery))
        with col2:
            st.metric("Avg. Confidence", f"{df_gallery['Confidence'].mean():.1f}%")
        with col3:
            critical_count = len(df_gallery[df_gallery['Severity'] == 'Critical'])
            st.metric("Critical Defects", critical_count)

# ============================================================================
# INSPECTION STATISTICS
# ============================================================================
elif section == "📈 Inspection Statistics":
    st.title("Inspection Statistics & Analytics")
    
    # Time range selector
    col1, col2 = st.columns(2)
    with col1:
        date_from = st.date_input("From Date", value=datetime.now() - pd.Timedelta(days=30))
    with col2:
        date_to = st.date_input("To Date", value=datetime.now())
    
    # Generate sample statistics
    days = (date_to - date_from).days
    total_inspections = days * 500
    total_passed = int(total_inspections * 0.97)
    total_failed = total_inspections - total_passed
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Inspections", f"{total_inspections:,}")
    with col2:
        st.metric("Pass Rate", f"{(total_passed/total_inspections)*100:.2f}%")
    with col3:
        st.metric("Failed Inspections", f"{total_failed:,}")
    with col4:
        st.metric("Avg. Daily Volume", f"{total_inspections//days:,}")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Defect Frequency by Type")
        defect_freq = pd.DataFrame({
            'Defect Type': ['Bent Fin', 'Blocked Section', 'UV Leak', 'Thermal Anomaly', 
                          'Surface Contamination', 'Structural Deformity'],
            'Count': [45, 32, 12, 28, 67, 15]
        })
        
        fig = px.bar(
            defect_freq,
            x='Defect Type',
            y='Count',
            color='Count',
            color_continuous_scale='Reds',
            title="Defect Frequency"
        )
        fig.update_xaxes(tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Inspection Trend")
        trend_data = pd.DataFrame({
            'Date': pd.date_range(date_from, date_to, freq='D'),
            'Passed': np.random.randint(480, 520, len(pd.date_range(date_from, date_to, freq='D'))),
            'Failed': np.random.randint(5, 25, len(pd.date_range(date_from, date_to, freq='D')))
        })
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=trend_data['Date'],
            y=trend_data['Passed'],
            mode='lines+markers',
            name='Passed',
            line=dict(color='#2ca02c', width=2)
        ))
        fig.add_trace(go.Scatter(
            x=trend_data['Date'],
            y=trend_data['Failed'],
            mode='lines+markers',
            name='Failed',
            line=dict(color='#d62728', width=2)
        ))
        fig.update_layout(
            title="Daily Inspection Results",
            xaxis_title="Date",
            yaxis_title="Count",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Defect severity distribution
    st.markdown("---")
    st.subheader("Defect Severity Distribution")
    
    severity_data = pd.DataFrame({
        'Severity': ['Low', 'Medium', 'High', 'Critical'],
        'Count': [89, 45, 32, 12],
        'Percentage': [53.0, 26.8, 19.0, 7.1]
    })
    
    fig = px.bar(
        severity_data,
        x='Severity',
        y='Count',
        text='Percentage',
        color='Severity',
        color_discrete_map={
            'Low': '#90EE90',
            'Medium': '#FFD700',
            'High': '#FF8C00',
            'Critical': '#FF4500'
        },
        title="Defect Severity Distribution"
    )
    fig.update_traces(texttemplate='%{text}%', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# SETTINGS & CONFIGURATION
# ============================================================================
elif section == "⚙️ Settings & Configuration":
    st.title("Settings & Configuration")
    
    st.subheader("Detection Parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Confidence Thresholds**")
        min_confidence = st.slider(
            "Minimum Confidence (%)",
            min_value=70,
            max_value=99,
            value=85,
            help="Minimum confidence level for defect detection"
        )
        
        critical_threshold = st.slider(
            "Critical Defect Threshold (%)",
            min_value=90,
            max_value=99,
            value=95,
            help="Confidence threshold for critical defects"
        )
    
    with col2:
        st.write("**Image Processing**")
        image_resolution = st.selectbox(
            "Processing Resolution",
            options=['Original', '1920x1080', '1280x720', '640x480'],
            index=0
        )
        
        enable_enhancement = st.checkbox("Enable Auto-Enhancement", value=True)
        
        noise_reduction = st.checkbox("Enable Noise Reduction", value=True)
    
    st.markdown("---")
    st.subheader("Defect Type Configuration")
    
    defect_config = pd.DataFrame({
        'Defect Type': ['Bent Fin', 'Blocked Section', 'UV Leak', 'Thermal Anomaly'],
        'Enabled': [True, True, True, True],
        'Min Confidence': [85, 80, 90, 75],
        'Severity': ['High', 'High', 'Critical', 'Medium']
    })
    
    edited_config = st.data_editor(
        defect_config,
        use_container_width=True,
        num_rows="dynamic"
    )
    
    st.markdown("---")
    st.subheader("System Information")
    
    sys_info = {
        'Component': ['AI Model Version', 'Detection Engine', 'Image Processor', 'Last Update'],
        'Value': ['v2.1.3', 'Mesh Transformer', 'OpenCV 4.8', '2024-01-15']
    }
    
    st.dataframe(pd.DataFrame(sys_info), use_container_width=True, hide_index=True)
    
    if st.button("💾 Save Configuration", type="primary"):
        st.success("Configuration saved successfully!")

# ============================================================================
# INSPECTION REPORTS
# ============================================================================
elif section == "📋 Inspection Reports":
    st.title("Inspection Reports")
    
    # Report generation options
    col1, col2 = st.columns(2)
    
    with col1:
        report_type = st.selectbox(
            "Report Type",
            options=['Daily Summary', 'Defect Analysis', 'Quality Metrics', 'Custom Report']
        )
        
        date_range = st.date_input(
            "Date Range",
            value=(datetime.now() - pd.Timedelta(days=7), datetime.now())
        )
    
    with col2:
        include_images = st.checkbox("Include Sample Images", value=True)
        include_charts = st.checkbox("Include Charts", value=True)
        export_format = st.selectbox(
            "Export Format",
            options=['PDF', 'Excel', 'CSV', 'JSON']
        )
    
    if st.button("📄 Generate Report", type="primary"):
        with st.spinner("Generating report..."):
            import time
            time.sleep(2)
            
            st.success("Report generated successfully!")
            
            # Sample report data
            st.markdown("---")
            st.subheader("Report Preview")
            
            report_data = {
                'Metric': [
                    'Total Inspections',
                    'Passed',
                    'Failed',
                    'Pass Rate',
                    'Avg. Confidence',
                    'Most Common Defect',
                    'Critical Defects'
                ],
                'Value': [
                    '3,500',
                    '3,395',
                    '105',
                    '97.0%',
                    '98.2%',
                    'Surface Contamination',
                    '8'
                ]
            }
            
            st.dataframe(pd.DataFrame(report_data), use_container_width=True, hide_index=True)
            
            # Download button (simulated)
            st.download_button(
                label=f"📥 Download Report ({export_format})",
                data="Sample report data",
                file_name=f"inspection_report_{datetime.now().strftime('%Y%m%d')}.{export_format.lower()}",
                mime="application/octet-stream"
            )
    
    st.markdown("---")
    st.subheader("Report History")
    
    report_history = pd.DataFrame({
        'Report ID': ['RPT-001', 'RPT-002', 'RPT-003'],
        'Type': ['Daily Summary', 'Defect Analysis', 'Quality Metrics'],
        'Date': ['2024-01-15', '2024-01-14', '2024-01-13'],
        'Status': ['Generated', 'Generated', 'Generated']
    })
    
    st.dataframe(report_history, use_container_width=True, hide_index=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Visual Inspection System | Condenser Quality Control | Tata Motors | 2024"
    "</div>",
    unsafe_allow_html=True
)

