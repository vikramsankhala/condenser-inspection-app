import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

# Page configuration
st.set_page_config(
    page_title="AI Mesh Transformer - Condenser Inspection",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🔍 Project Navigation")
st.sidebar.markdown("---")

section = st.sidebar.radio(
    "Navigate to:",
    [
        "🏠 Executive Summary",
        "📋 Context & Problem Statement",
        "🔬 Defect Taxonomy & Sensor Modalities",
        "🤖 AI Mesh Transformer Architecture",
        "📡 Sensor Placement (3D)",
        "🔄 Defect Detection Flow",
        "💰 ROI Calculator",
        "📅 Implementation Timeline",
        "📚 References"
    ]
)

# ============================================================================
# EXECUTIVE SUMMARY
# ============================================================================
if section == "🏠 Executive Summary":
    st.markdown('<div class="main-header">AI Mesh Transformer for Condenser Firewall Inspection</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.subheader("Tata Motors - Harrier/Safari Line")
        st.write("**Location:** Pimpri-Chinchwad Manufacturing Plant")
        st.write("**Project Type:** Automated Multimodal Quality Inspection System")
    
    with col2:
        st.image("https://via.placeholder.com/150x100/1f77b4/ffffff?text=Tata+Motors", caption="Tata Motors Logo")
    
    with col3:
        st.image("https://via.placeholder.com/150x100/ff7f0e/ffffff?text=AI+Lab", caption="AI Research Lab")
    
    st.markdown("---")
    
    # Key Metrics
    st.subheader("📊 Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Defect Detection Accuracy",
            value="98.5%",
            delta="+3.2% vs baseline",
            delta_color="normal"
        )
    
    with col2:
        st.metric(
            label="Cycle Time per Unit",
            value="5.2 sec",
            delta="-12 sec vs manual",
            delta_color="inverse"
        )
    
    with col3:
        st.metric(
            label="ROI Breakeven",
            value="17 months",
            delta="On track",
            delta_color="normal"
        )
    
    with col4:
        st.metric(
            label="False Positive Rate",
            value="< 0.5%",
            delta="-2.1% improvement",
            delta_color="normal"
        )
    
    st.markdown("---")
    
    # Executive Summary Content
    st.subheader("Executive Summary")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        This project presents an **AI Mesh Transformer-based automated inspection system** for condenser firewall 
        assemblies at Tata Motors' Harrier/Safari production line. The system integrates multiple sensor modalities 
        (RGB, UV, Thermal IR, Structured Light, Acoustic, and Pressure/Temperature sensors) to detect critical 
        defects including bent fins, blocked sections, leaks, and structural anomalies.
        
        **Key Innovations:**
        - **Mesh Transformer Architecture**: Enables 10x parameter fusion compared to traditional CNNs
        - **Multimodal Sensor Fusion**: 6 different sensor types working in harmony
        - **Real-time Processing**: Sub-6 second inspection cycle time
        - **High Accuracy**: 98.5% defect detection rate with <0.5% false positives
        """)
    
    with col2:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.write("**Did you know?**")
        st.write("Mesh transformers enable 10x parameter fusion compared to traditional CNNs, allowing for more comprehensive defect analysis across multiple sensor modalities simultaneously.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Project Team
    st.markdown("---")
    st.subheader("👥 Project Team")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("**Lead Researcher**")
        st.write("Dr. Arvind Mathur")
    with col2:
        st.write("**Technical Lead**")
        st.write("AI Research Team")
    with col3:
        st.write("**Industry Mentor**")
        st.write("Tata Motors Engineering")
    with col4:
        st.write("**Organization**")
        st.write("Tata Motors Ltd.")

# ============================================================================
# CONTEXT & PROBLEM STATEMENT
# ============================================================================
elif section == "📋 Context & Problem Statement":
    st.title("Context & Problem Statement")
    
    st.subheader("Manufacturing Context")
    st.write("""
    The **Tata Motors Harrier Firewall Station** at Pimpri-Chinchwad is responsible for assembling and inspecting 
    condenser units that are critical components in vehicle HVAC systems. These condensers must meet stringent 
    quality standards to ensure vehicle performance and customer satisfaction.
    """)
    
    # Problem Statement
    st.markdown("---")
    st.subheader("🔴 Current Challenges")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **1. Manual Inspection Limitations**
        - Time-consuming: ~17 seconds per unit
        - Human error: ~5% defect miss rate
        - Inconsistent quality assessment
        - High labor costs
        
        **2. Defect Complexity**
        - Multiple defect types requiring different detection methods
        - Some defects invisible to naked eye (UV leaks)
        - Thermal anomalies require specialized sensors
        """)
    
    with col2:
        st.write("""
        **3. Production Bottleneck**
        - Inspection station limits production throughput
        - Quality gates cause delays
        - Rework costs impact profitability
        
        **4. Scalability Issues**
        - Difficult to scale manual inspection
        - Training new inspectors takes time
        - Quality standards vary between shifts
        """)
    
    # Solution Overview
    st.markdown("---")
    st.subheader("✅ Proposed Solution")
    
    st.write("""
    An **AI-powered multimodal inspection system** that:
    - Automates the entire inspection process
    - Integrates 6 different sensor types for comprehensive coverage
    - Uses advanced Mesh Transformer architecture for intelligent defect detection
    - Reduces cycle time from 17s to 5.2s (70% improvement)
    - Achieves 98.5% accuracy with minimal false positives
    - Provides real-time analytics and quality metrics
    """)
    
    # Impact Visualization
    st.markdown("---")
    st.subheader("Impact Comparison")
    
    comparison_data = pd.DataFrame({
        'Metric': ['Cycle Time (sec)', 'Accuracy (%)', 'Cost per Unit (₹)', 'Throughput (units/hr)'],
        'Manual': [17, 95, 150, 212],
        'AI System': [5.2, 98.5, 45, 692]
    })
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Manual Inspection',
        x=comparison_data['Metric'],
        y=comparison_data['Manual'],
        marker_color='#ff7f0e'
    ))
    fig.add_trace(go.Bar(
        name='AI System',
        x=comparison_data['Metric'],
        y=comparison_data['AI System'],
        marker_color='#1f77b4'
    ))
    fig.update_layout(
        title="Manual vs AI System Performance",
        xaxis_title="Metrics",
        yaxis_title="Value",
        barmode='group',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# DEFECT TAXONOMY & SENSOR MODALITIES
# ============================================================================
elif section == "🔬 Defect Taxonomy & Sensor Modalities":
    st.title("Defect Taxonomy & Sensor Modalities")
    
    # Defect Taxonomy Data
    defects_data = {
        'Defect Type': [
            'Bent Fin',
            'Blocked Section',
            'UV Leak',
            'Thermal Anomaly',
            'Structural Deformity',
            'Surface Contamination',
            'Mounting Misalignment',
            'Pressure Drop'
        ],
        'Severity': ['High', 'High', 'Critical', 'Medium', 'High', 'Low', 'High', 'Critical'],
        'Primary Sensor': [
            'RGB Camera',
            'Structured Light',
            'UV Camera',
            'Thermal IR',
            'RGB + Structured Light',
            'RGB Camera',
            'Structured Light',
            'Pressure/Temp Sensor'
        ],
        'AI Head': [
            'Vision Transformer',
            '3D Mesh Analyzer',
            'UV Anomaly Detector',
            'Thermal Pattern Analyzer',
            'Multi-Modal Fusion',
            'Surface Classifier',
            'Geometric Validator',
            'Flow Dynamics Model'
        ],
        'Detection Time (ms)': [120, 180, 95, 150, 250, 100, 160, 80],
        'Accuracy (%)': [99.2, 97.8, 98.5, 96.5, 98.9, 95.2, 99.1, 97.5]
    }
    
    df_defects = pd.DataFrame(defects_data)
    
    st.subheader("Defect Classification Table")
    
    # Interactive filters
    col1, col2 = st.columns(2)
    with col1:
        severity_filter = st.multiselect(
            "Filter by Severity",
            options=df_defects['Severity'].unique(),
            default=df_defects['Severity'].unique()
        )
    with col2:
        sensor_filter = st.multiselect(
            "Filter by Primary Sensor",
            options=df_defects['Primary Sensor'].unique(),
            default=df_defects['Primary Sensor'].unique()
        )
    
    # Filter dataframe
    filtered_df = df_defects[
        (df_defects['Severity'].isin(severity_filter)) &
        (df_defects['Primary Sensor'].isin(sensor_filter))
    ]
    
    # Display table
    st.dataframe(
        filtered_df.style.background_gradient(subset=['Accuracy (%)'], cmap='RdYlGn'),
        use_container_width=True,
        height=400
    )
    
    # Defect selection for detailed view
    st.markdown("---")
    st.subheader("Defect Details")
    
    selected_defect = st.selectbox(
        "Select a defect to view detailed information:",
        options=df_defects['Defect Type'].tolist()
    )
    
    if selected_defect:
        defect_info = df_defects[df_defects['Defect Type'] == selected_defect].iloc[0]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Detection Time", f"{defect_info['Detection Time (ms)']} ms")
        with col2:
            st.metric("Accuracy", f"{defect_info['Accuracy (%)']}%")
        with col3:
            st.metric("Severity", defect_info['Severity'])
        
        st.write(f"**Primary Sensor:** {defect_info['Primary Sensor']}")
        st.write(f"**AI Processing Head:** {defect_info['AI Head']}")
        
        # Sensor Modalities Overview
        st.markdown("---")
        st.subheader("Sensor Modalities Overview")
        
        sensors_info = {
            'Sensor Type': [
                'RGB Camera',
                'UV Camera',
                'Thermal IR',
                'Structured Light',
                'Acoustic Sensor',
                'Pressure/Temp Sensor'
            ],
            'Purpose': [
                'Visual defect detection, surface inspection',
                'Leak detection (UV-visible dyes)',
                'Thermal anomaly detection',
                '3D geometry and depth measurement',
                'Structural integrity via acoustic signature',
                'Flow dynamics and pressure monitoring'
            ],
            'Resolution': ['4K', '2K', '640x480', '1920x1080', 'N/A', '16-bit'],
            'Frame Rate': ['30 fps', '15 fps', '25 fps', '60 fps', '44.1 kHz', '100 Hz']
        }
        
        df_sensors = pd.DataFrame(sensors_info)
        st.dataframe(df_sensors, use_container_width=True)

# ============================================================================
# AI MESH TRANSFORMER ARCHITECTURE
# ============================================================================
elif section == "🤖 AI Mesh Transformer Architecture":
    st.title("AI Mesh Transformer Architecture")
    
    st.write("""
    The Mesh Transformer architecture enables efficient fusion of multimodal sensor data through a novel 
    attention mechanism that processes spatial and temporal relationships across different sensor modalities.
    """)
    
    # Architecture Diagram (using Plotly)
    st.subheader("Architecture Overview")
    
    # Create a simplified architecture diagram
    fig = go.Figure()
    
    # Input layer (sensors)
    sensor_positions = {
        'RGB': (0, 2),
        'UV': (0, 1),
        'Thermal': (0, 0),
        'Structured Light': (0, -1),
        'Acoustic': (0, -2),
        'Pressure/Temp': (0, -3)
    }
    
    # Draw sensor inputs
    for sensor, (x, y) in sensor_positions.items():
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(size=30, color='#1f77b4'),
            text=[sensor],
            textposition='middle right',
            name=sensor,
            hovertemplate=f'<b>{sensor} Sensor</b><extra></extra>'
        ))
    
    # Feature extraction layer
    fig.add_trace(go.Scatter(
        x=[1, 1, 1, 1, 1, 1],
        y=[2, 1, 0, -1, -2, -3],
        mode='markers',
        marker=dict(size=25, color='#ff7f0e', symbol='square'),
        name='Feature Extraction',
        hovertemplate='Feature Extraction Layer<extra></extra>'
    ))
    
    # Mesh Transformer blocks
    fig.add_trace(go.Scatter(
        x=[2.5, 2.5, 2.5],
        y=[1, 0, -1],
        mode='markers',
        marker=dict(size=40, color='#2ca02c', symbol='diamond'),
        name='Mesh Transformer',
        hovertemplate='Mesh Transformer Block<extra></extra>'
    ))
    
    # Attention mechanism
    fig.add_trace(go.Scatter(
        x=[4],
        y=[0],
        mode='markers',
        marker=dict(size=50, color='#d62728', symbol='star'),
        name='Multi-Head Attention',
        hovertemplate='Multi-Head Attention Fusion<extra></extra>'
    ))
    
    # Output heads
    output_heads = {
        'Bent Fin': (5.5, 1.5),
        'Blocked': (5.5, 0.5),
        'Leak': (5.5, -0.5),
        'Thermal': (5.5, -1.5)
    }
    
    for head, (x, y) in output_heads.items():
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(size=20, color='#9467bd'),
            text=[head],
            textposition='middle right',
            name=head,
            hovertemplate=f'<b>{head} Detection Head</b><extra></extra>'
        ))
    
    # Add connections (arrows)
    for sensor, (x, y) in sensor_positions.items():
        fig.add_annotation(
            x=1, y=y,
            ax=x, ay=y,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='gray'
        )
    
    fig.update_layout(
        title="AI Mesh Transformer Architecture",
        xaxis=dict(showgrid=False, showticklabels=False, range=[-0.5, 7]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[-4, 3]),
        height=600,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Architecture Components
    st.markdown("---")
    st.subheader("Key Components")
    
    components = {
        'Component': [
            'Input Layer',
            'Feature Extraction',
            'Mesh Transformer Blocks',
            'Multi-Head Attention',
            'Output Heads',
            'Decision Fusion'
        ],
        'Description': [
            '6 parallel sensor inputs with preprocessing',
            'CNN-based feature extraction per modality',
            '3 transformer blocks with cross-modal attention',
            'Fuses features across all sensor modalities',
            'Specialized heads for each defect type',
            'Final decision layer with confidence scoring'
        ],
        'Parameters': [
            'Variable (sensor-dependent)',
            '~2M per sensor',
            '~15M per block',
            '~8M',
            '~1M per head',
            '~500K'
        ]
    }
    
    df_components = pd.DataFrame(components)
    st.dataframe(df_components, use_container_width=True)
    
    # Technical Details
    st.markdown("---")
    st.subheader("Technical Specifications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **Model Architecture:**
        - Total Parameters: ~60M
        - Input Dimensions: Multi-modal (varies by sensor)
        - Output: 8-class defect classification + confidence scores
        - Training Data: 50,000+ labeled samples
        - Validation Accuracy: 98.5%
        """)
    
    with col2:
        st.write("""
        **Performance Metrics:**
        - Inference Time: <250ms per unit
        - Memory Usage: ~2GB GPU
        - Throughput: 692 units/hour
        - Power Consumption: ~150W
        - Model Size: ~240MB
        """)
    
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.write("**Did you know?**")
    st.write("The Mesh Transformer architecture processes all 6 sensor modalities simultaneously, enabling real-time multimodal fusion that traditional sequential processing cannot achieve.")
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# SENSOR PLACEMENT (3D)
# ============================================================================
elif section == "📡 Sensor Placement (3D)":
    st.title("Sensor Placement - 3D Visualization")
    
    st.write("""
    Interactive 3D visualization of the condenser assembly with sensor positions and coverage areas.
    Click on sensor markers to view detailed information.
    """)
    
    # 3D Condenser Model with Sensors
    fig = go.Figure()
    
    # Create condenser base (rectangular box)
    condenser_length = 0.6
    condenser_width = 0.4
    condenser_height = 0.05
    
    # Condenser base
    x_base = [0, condenser_length, condenser_length, 0, 0]
    y_base = [0, 0, condenser_width, condenser_width, 0]
    z_base = [0, 0, 0, 0, 0]
    
    fig.add_trace(go.Scatter3d(
        x=x_base, y=y_base, z=z_base,
        mode='lines',
        line=dict(color='gray', width=2),
        name='Condenser Base',
        showlegend=False
    ))
    
    # Sensor positions (realistic placement on condenser)
    sensors_3d = {
        'RGB Camera 1': {'pos': (0.1, 0.2, 0.3), 'color': 'blue', 'coverage': 0.15},
        'RGB Camera 2': {'pos': (0.5, 0.2, 0.3), 'color': 'blue', 'coverage': 0.15},
        'UV Camera': {'pos': (0.3, 0.1, 0.25), 'color': 'purple', 'coverage': 0.12},
        'Thermal IR': {'pos': (0.2, 0.3, 0.28), 'color': 'red', 'coverage': 0.18},
        'Structured Light': {'pos': (0.4, 0.3, 0.35), 'color': 'green', 'coverage': 0.20},
        'Acoustic Sensor': {'pos': (0.5, 0.1, 0.2), 'color': 'orange', 'coverage': 0.10},
        'Pressure/Temp': {'pos': (0.15, 0.15, 0.05), 'color': 'cyan', 'coverage': 0.08}
    }
    
    # Plot sensors
    sensor_names = []
    sensor_x = []
    sensor_y = []
    sensor_z = []
    sensor_colors = []
    
    for name, info in sensors_3d.items():
        x, y, z = info['pos']
        sensor_names.append(name)
        sensor_x.append(x)
        sensor_y.append(y)
        sensor_z.append(z)
        sensor_colors.append(info['color'])
        
        # Add coverage sphere (simplified as circle)
        theta = np.linspace(0, 2*np.pi, 50)
        phi = np.linspace(0, np.pi, 50)
        coverage = info['coverage']
        
        # Draw coverage area (projection on condenser surface)
        coverage_x = x + coverage * np.cos(theta)
        coverage_y = y + coverage * np.sin(theta)
        coverage_z = np.zeros_like(coverage_x)
        
        fig.add_trace(go.Scatter3d(
            x=coverage_x, y=coverage_y, z=coverage_z,
            mode='lines',
            line=dict(color=info['color'], width=1, dash='dash'),
            name=f'{name} Coverage',
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Add sensor markers
    fig.add_trace(go.Scatter3d(
        x=sensor_x, y=sensor_y, z=sensor_z,
        mode='markers+text',
        marker=dict(
            size=12,
            color=sensor_colors,
            symbol='circle',
            line=dict(width=2, color='black')
        ),
        text=sensor_names,
        textposition='top center',
        name='Sensors',
        hovertemplate='<b>%{text}</b><br>Position: (%{x:.2f}, %{y:.2f}, %{z:.2f})<extra></extra>'
    ))
    
    # Add fins (simplified representation)
    for i in range(10):
        fin_x = 0.05 + i * 0.055
        fig.add_trace(go.Scatter3d(
            x=[fin_x, fin_x], y=[0, condenser_width], z=[0.02, 0.02],
            mode='lines',
            line=dict(color='lightblue', width=1),
            name='Fins' if i == 0 else '',
            showlegend=(i == 0),
            hoverinfo='skip'
        ))
    
    fig.update_layout(
        title="Condenser 3D Model with Sensor Array",
        scene=dict(
            xaxis_title='Length (m)',
            yaxis_title='Width (m)',
            zaxis_title='Height (m)',
            aspectmode='manual',
            aspectratio=dict(x=1, y=0.67, z=0.5),
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.2)
            )
        ),
        height=700
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Sensor selection for details
    st.markdown("---")
    st.subheader("Sensor Details")
    
    selected_sensor = st.selectbox(
        "Select a sensor to view specifications:",
        options=list(sensors_3d.keys())
    )
    
    if selected_sensor:
        sensor_info = sensors_3d[selected_sensor]
        x, y, z = sensor_info['pos']
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("X Position", f"{x:.2f} m")
        with col2:
            st.metric("Y Position", f"{y:.2f} m")
        with col3:
            st.metric("Z Position", f"{z:.2f} m")
        
        st.metric("Coverage Radius", f"{sensor_info['coverage']:.2f} m")
        
        # Sensor-specific information
        sensor_details = {
            'RGB Camera 1': 'Primary visual inspection, detects bent fins and surface defects. 4K resolution, 30 fps.',
            'RGB Camera 2': 'Secondary visual inspection, complementary angle for full coverage. 4K resolution, 30 fps.',
            'UV Camera': 'Detects UV-visible dye leaks. Specialized for refrigerant leak detection. 2K resolution, 15 fps.',
            'Thermal IR': 'Monitors temperature distribution. Detects thermal anomalies and blocked sections. 640x480, 25 fps.',
            'Structured Light': '3D geometry measurement. Detects structural deformities and mounting misalignment. 1920x1080, 60 fps.',
            'Acoustic Sensor': 'Structural integrity via acoustic signature analysis. Detects internal defects. 44.1 kHz sampling.',
            'Pressure/Temp': 'Flow dynamics monitoring. Detects pressure drops and temperature variations. 16-bit resolution, 100 Hz.'
        }
        
        st.write(f"**Description:** {sensor_details.get(selected_sensor, 'Sensor information not available.')}")
    
    # Defect overlay toggle
    st.markdown("---")
    st.subheader("Defect Simulation")
    
    defect_type = st.selectbox(
        "Simulate defect overlay:",
        options=['None', 'Bent Fin', 'Blocked Section', 'UV Leak', 'Thermal Anomaly']
    )
    
    if defect_type != 'None':
        st.info(f"💡 **{defect_type}** would be highlighted in the 3D model. In a full implementation, this would show the exact location and affected area on the condenser.")

# ============================================================================
# DEFECT DETECTION FLOW
# ============================================================================
elif section == "🔄 Defect Detection Flow":
    st.title("Defect Detection Flow")
    
    st.write("""
    Step-by-step process of how the AI system detects defects in real-time. Click through each stage to understand 
    the complete inspection pipeline.
    """)
    
    # Flowchart stages
    stages = [
        {
            'name': '1. Unit Arrival',
            'description': 'Condenser unit arrives at inspection station via conveyor',
            'time': '0.5 sec',
            'output': 'Unit positioned and ready'
        },
        {
            'name': '2. Sensor Activation',
            'description': 'All 6 sensors simultaneously activate and begin data capture',
            'time': '0.2 sec',
            'output': 'Multi-modal data streams initiated'
        },
        {
            'name': '3. Data Acquisition',
            'description': 'Sensors capture images, thermal data, acoustic signals, and pressure readings',
            'time': '1.0 sec',
            'output': 'Raw sensor data collected'
        },
        {
            'name': '4. Preprocessing',
            'description': 'Data normalization, noise reduction, and format standardization',
            'time': '0.3 sec',
            'output': 'Preprocessed feature maps'
        },
        {
            'name': '5. Feature Extraction',
            'description': 'CNN-based feature extraction for each sensor modality',
            'time': '0.8 sec',
            'output': 'Extracted feature vectors'
        },
        {
            'name': '6. Mesh Transformer Processing',
            'description': 'Cross-modal attention and feature fusion through transformer blocks',
            'time': '1.2 sec',
            'output': 'Fused multimodal features'
        },
        {
            'name': '7. Defect Classification',
            'description': 'Specialized heads classify defects and generate confidence scores',
            'time': '0.4 sec',
            'output': 'Defect predictions with scores'
        },
        {
            'name': '8. Decision Fusion',
            'description': 'Final decision layer combines all predictions with confidence weighting',
            'time': '0.1 sec',
            'output': 'Final inspection result'
        },
        {
            'name': '9. Result Output',
            'description': 'Pass/Fail decision with detailed defect report',
            'time': '0.5 sec',
            'output': 'Inspection complete, unit proceeds'
        }
    ]
    
    # Interactive stage selection
    selected_stage_idx = st.selectbox(
        "Select a stage to view details:",
        options=range(len(stages)),
        format_func=lambda x: stages[x]['name']
    )
    
    selected_stage = stages[selected_stage_idx]
    
    # Display selected stage details
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(selected_stage['name'])
        st.write(f"**Description:** {selected_stage['description']}")
        st.write(f"**Output:** {selected_stage['output']}")
    
    with col2:
        st.metric("Processing Time", selected_stage['time'])
        progress = (selected_stage_idx + 1) / len(stages)
        st.progress(progress)
        st.caption(f"Stage {selected_stage_idx + 1} of {len(stages)}")
    
    # Visual flowchart
    st.markdown("---")
    st.subheader("Process Flowchart")
    
    # Create a simple flowchart visualization
    flow_y_positions = np.linspace(0, len(stages) * 2, len(stages))
    
    fig = go.Figure()
    
    # Draw flow arrows
    for i in range(len(stages) - 1):
        fig.add_annotation(
            x=0, y=flow_y_positions[i],
            ax=0, ay=flow_y_positions[i+1],
            arrowhead=2,
            arrowsize=1.5,
            arrowwidth=3,
            arrowcolor='#1f77b4'
        )
    
    # Draw stage boxes
    for i, stage in enumerate(stages):
        color = '#2ca02c' if i == selected_stage_idx else '#1f77b4'
        fig.add_trace(go.Scatter(
            x=[0], y=[flow_y_positions[i]],
            mode='markers+text',
            marker=dict(size=50, color=color, symbol='square'),
            text=[f"{i+1}"],
            textposition='middle center',
            textfont=dict(size=14, color='white'),
            name=stage['name'],
            hovertemplate=f'<b>{stage["name"]}</b><br>{stage["description"]}<br>Time: {stage["time"]}<extra></extra>'
        ))
    
    fig.update_layout(
        title="Defect Detection Pipeline",
        xaxis=dict(showgrid=False, showticklabels=False, range=[-0.5, 0.5]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[-1, len(stages) * 2 + 1]),
        height=600,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Timing breakdown
    st.markdown("---")
    st.subheader("Timing Breakdown")
    
    timing_data = pd.DataFrame({
        'Stage': [s['name'] for s in stages],
        'Time (sec)': [float(s['time'].split()[0]) for s in stages]
    })
    
    fig_bar = px.bar(
        timing_data,
        x='Stage',
        y='Time (sec)',
        title="Processing Time per Stage",
        color='Time (sec)',
        color_continuous_scale='Blues'
    )
    fig_bar.update_xaxes(tickangle=-45)
    st.plotly_chart(fig_bar, use_container_width=True)
    
    total_time = sum([float(s['time'].split()[0]) for s in stages])
    st.metric("Total Processing Time", f"{total_time:.1f} seconds")

# ============================================================================
# ROI CALCULATOR
# ============================================================================
elif section == "💰 ROI Calculator":
    st.title("ROI Calculator")
    
    st.write("""
    Interactive calculator to estimate Return on Investment (ROI) for the AI Mesh Transformer inspection system.
    Adjust the parameters below to see how they impact the financial returns.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Investment Parameters")
        initial_investment = st.slider(
            "Initial Investment (₹ Lakhs)",
            min_value=10,
            max_value=100,
            value=25,
            step=1
        )
        
        monthly_savings = st.slider(
            "Monthly Savings (₹ Lakhs)",
            min_value=1,
            max_value=10,
            value=3,
            step=0.5
        )
        
        monthly_o_and_m = st.slider(
            "Monthly O&M Cost (₹ Lakhs)",
            min_value=0.5,
            max_value=5,
            value=1.5,
            step=0.1
        )
    
    with col2:
        st.subheader("Operational Parameters")
        units_per_month = st.slider(
            "Units Inspected per Month",
            min_value=1000,
            max_value=50000,
            value=15000,
            step=500
        )
        
        cost_per_unit_manual = st.slider(
            "Manual Inspection Cost per Unit (₹)",
            min_value=50,
            max_value=500,
            value=150,
            step=10
        )
        
        cost_per_unit_ai = st.slider(
            "AI System Cost per Unit (₹)",
            min_value=10,
            max_value=100,
            value=45,
            step=5
        )
    
    # Calculate ROI
    monthly_net_savings = monthly_savings - monthly_o_and_m
    monthly_cost_savings = (cost_per_unit_manual - cost_per_unit_ai) * units_per_month / 100000  # Convert to lakhs
    
    total_monthly_savings = monthly_net_savings + monthly_cost_savings
    
    # Calculate cumulative ROI over 36 months
    months = list(range(1, 37))
    cumulative_roi = []
    cumulative_savings = []
    breakeven_month = None
    
    for month in months:
        cumulative_saving = total_monthly_savings * month - initial_investment
        cumulative_savings.append(cumulative_saving)
        roi_percent = (cumulative_saving / initial_investment) * 100 if initial_investment > 0 else 0
        cumulative_roi.append(roi_percent)
        
        if breakeven_month is None and cumulative_saving >= 0:
            breakeven_month = month
    
    # Display key metrics
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Monthly Net Savings", f"₹ {total_monthly_savings:.2f} L")
    with col2:
        st.metric("Breakeven Month", f"Month {breakeven_month}" if breakeven_month else ">36 months")
    with col3:
        roi_36_month = cumulative_roi[-1]
        st.metric("36-Month ROI", f"{roi_36_month:.1f}%")
    with col4:
        total_36_savings = cumulative_savings[-1]
        st.metric("36-Month Net Savings", f"₹ {total_36_savings:.2f} L")
    
    # ROI Chart
    st.markdown("---")
    st.subheader("ROI Over Time")
    
    roi_df = pd.DataFrame({
        'Month': months,
        'Cumulative Savings (₹ L)': cumulative_savings,
        'ROI (%)': cumulative_roi
    })
    
    fig = go.Figure()
    
    # Add breakeven line
    fig.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Breakeven")
    
    # Add savings line
    fig.add_trace(go.Scatter(
        x=roi_df['Month'],
        y=roi_df['Cumulative Savings (₹ L)'],
        mode='lines+markers',
        name='Cumulative Savings',
        line=dict(color='#2ca02c', width=3),
        fill='tozeroy',
        fillcolor='rgba(44, 160, 44, 0.2)'
    ))
    
    if breakeven_month:
        fig.add_vline(
            x=breakeven_month,
            line_dash="dot",
            line_color="red",
            annotation_text=f"Breakeven: Month {breakeven_month}",
            annotation_position="top"
        )
    
    fig.update_layout(
        title="Cumulative ROI Over 36 Months",
        xaxis_title="Month",
        yaxis_title="Cumulative Savings (₹ Lakhs)",
        height=500,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # ROI Percentage Chart
    st.subheader("ROI Percentage Over Time")
    
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=roi_df['Month'],
        y=roi_df['ROI (%)'],
        mode='lines+markers',
        name='ROI %',
        line=dict(color='#1f77b4', width=3),
        fill='tozeroy',
        fillcolor='rgba(31, 119, 180, 0.2)'
    ))
    
    fig2.add_hline(y=0, line_dash="dash", line_color="gray")
    
    if breakeven_month:
        fig2.add_vline(
            x=breakeven_month,
            line_dash="dot",
            line_color="red",
            annotation_text=f"Breakeven: Month {breakeven_month}",
            annotation_position="top"
        )
    
    fig2.update_layout(
        title="ROI Percentage Over 36 Months",
        xaxis_title="Month",
        yaxis_title="ROI (%)",
        height=400
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # Cost breakdown
    st.markdown("---")
    st.subheader("Cost Breakdown Analysis")
    
    cost_breakdown = pd.DataFrame({
        'Category': [
            'Initial Investment',
            'Monthly O&M',
            'Cost per Unit (AI)',
            'Cost per Unit (Manual)',
            'Monthly Cost Savings',
            'Net Monthly Benefit'
        ],
        'Amount (₹ L)': [
            initial_investment,
            monthly_o_and_m,
            cost_per_unit_ai * units_per_month / 100000,
            cost_per_unit_manual * units_per_month / 100000,
            monthly_cost_savings,
            total_monthly_savings
        ]
    })
    
    st.dataframe(cost_breakdown, use_container_width=True)

# ============================================================================
# IMPLEMENTATION TIMELINE
# ============================================================================
elif section == "📅 Implementation Timeline":
    st.title("Implementation Timeline & Milestones")
    
    st.write("""
    Project timeline showing key milestones, deliverables, and current status.
    """)
    
    # Timeline data
    timeline_data = [
        {
            'Phase': 'Phase 1: Planning & Design',
            'Start': '2024-01-01',
            'End': '2024-03-31',
            'Status': 'Completed',
            'Deliverables': ['System architecture design', 'Sensor selection', 'Requirements specification'],
            'Progress': 100
        },
        {
            'Phase': 'Phase 2: Hardware Setup',
            'Start': '2024-02-15',
            'End': '2024-05-15',
            'Status': 'Completed',
            'Deliverables': ['Sensor installation', 'Data acquisition system', 'Calibration'],
            'Progress': 100
        },
        {
            'Phase': 'Phase 3: Data Collection',
            'Start': '2024-04-01',
            'End': '2024-07-31',
            'Status': 'Completed',
            'Deliverables': ['50,000+ labeled samples', 'Defect database', 'Validation dataset'],
            'Progress': 100
        },
        {
            'Phase': 'Phase 4: Model Development',
            'Start': '2024-06-01',
            'End': '2024-09-30',
            'Status': 'Completed',
            'Deliverables': ['Mesh Transformer model', 'Training pipeline', 'Model optimization'],
            'Progress': 100
        },
        {
            'Phase': 'Phase 5: Integration & Testing',
            'Start': '2024-08-15',
            'End': '2024-11-30',
            'Status': 'In Progress',
            'Deliverables': ['System integration', 'End-to-end testing', 'Performance validation'],
            'Progress': 75
        },
        {
            'Phase': 'Phase 6: Deployment',
            'Start': '2024-11-01',
            'End': '2025-01-31',
            'Status': 'Planned',
            'Deliverables': ['Production deployment', 'Operator training', 'Documentation'],
            'Progress': 0
        },
        {
            'Phase': 'Phase 7: Monitoring & Optimization',
            'Start': '2025-02-01',
            'End': '2025-06-30',
            'Status': 'Planned',
            'Deliverables': ['Performance monitoring', 'Continuous improvement', 'ROI validation'],
            'Progress': 0
        }
    ]
    
    # Display timeline
    for phase in timeline_data:
        with st.expander(f"{phase['Phase']} - {phase['Status']}", expanded=(phase['Status'] == 'In Progress')):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.write(f"**Duration:** {phase['Start']} to {phase['End']}")
                st.write(f"**Status:** {phase['Status']}")
                st.progress(phase['Progress'] / 100)
                
                st.write("**Deliverables:**")
                for deliverable in phase['Deliverables']:
                    st.write(f"- {deliverable}")
            
            with col2:
                status_color = {
                    'Completed': '🟢',
                    'In Progress': '🟡',
                    'Planned': '⚪'
                }
                st.markdown(f"### {status_color.get(phase['Status'], '⚪')}")
    
    # Gantt-style visualization
    st.markdown("---")
    st.subheader("Timeline Visualization")
    
    # Create Gantt chart data
    gantt_data = []
    for phase in timeline_data:
        start_date = datetime.strptime(phase['Start'], '%Y-%m-%d')
        end_date = datetime.strptime(phase['End'], '%Y-%m-%d')
        duration = (end_date - start_date).days
        
        gantt_data.append({
            'Phase': phase['Phase'],
            'Start': phase['Start'],
            'End': phase['End'],
            'Duration': duration,
            'Status': phase['Status']
        })
    
    gantt_df = pd.DataFrame(gantt_data)
    
    # Create Gantt chart using Plotly
    fig = go.Figure()
    
    colors = {'Completed': '#2ca02c', 'In Progress': '#ff7f0e', 'Planned': '#d3d3d3'}
    
    for i, phase in enumerate(timeline_data):
        start_date = datetime.strptime(phase['Start'], '%Y-%m-%d')
        end_date = datetime.strptime(phase['End'], '%Y-%m-%d')
        
        fig.add_trace(go.Scatter(
            x=[start_date, end_date, end_date, start_date, start_date],
            y=[i, i, i+0.8, i+0.8, i],
            fill='toself',
            fillcolor=colors.get(phase['Status'], 'gray'),
            line=dict(color='black', width=1),
            mode='lines',
            name=phase['Phase'],
            text=[phase['Phase']],
            hovertemplate=f'<b>{phase["Phase"]}</b><br>Status: {phase["Status"]}<br>Duration: {phase["Start"]} to {phase["End"]}<extra></extra>'
        ))
    
    fig.update_layout(
        title="Project Timeline - Gantt Chart",
        xaxis_title="Date",
        yaxis=dict(
            tickmode='array',
            tickvals=list(range(len(timeline_data))),
            ticktext=[p['Phase'] for p in timeline_data],
            autorange='reversed'
        ),
        height=500,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Current status summary
    st.markdown("---")
    st.subheader("Current Project Status")
    
    completed = len([p for p in timeline_data if p['Status'] == 'Completed'])
    in_progress = len([p for p in timeline_data if p['Status'] == 'In Progress'])
    planned = len([p for p in timeline_data if p['Status'] == 'Planned'])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Completed Phases", completed)
    with col2:
        st.metric("In Progress", in_progress)
    with col3:
        st.metric("Planned", planned)
    
    overall_progress = sum([p['Progress'] for p in timeline_data]) / len(timeline_data)
    st.metric("Overall Project Progress", f"{overall_progress:.1f}%")

# ============================================================================
# REFERENCES
# ============================================================================
elif section == "📚 References":
    st.title("References & Resources")
    
    st.subheader("Research Papers & Documentation")
    
    references = [
        {
            'Title': 'Mesh Transformer Architecture for Multimodal Sensor Fusion',
            'Type': 'Research Paper',
            'Link': 'https://example.com/mesh-transformer-paper',
            'Description': 'Detailed technical paper on the Mesh Transformer architecture and its application to multimodal defect detection.'
        },
        {
            'Title': 'AI Mesh Transformer - Full Presentation',
            'Type': 'Presentation',
            'Link': 'https://example.com/presentation',
            'Description': 'Complete project presentation with all slides, diagrams, and technical details.'
        },
        {
            'Title': 'Defect Detection Dataset',
            'Type': 'Dataset',
            'Link': 'https://example.com/dataset',
            'Description': 'Labeled dataset of 50,000+ condenser images with defect annotations.'
        },
        {
            'Title': 'System Architecture Documentation',
            'Type': 'Technical Documentation',
            'Link': 'https://example.com/architecture-docs',
            'Description': 'Comprehensive documentation of system architecture, sensor specifications, and integration details.'
        },
        {
            'Title': 'ROI Analysis Report',
            'Type': 'Business Report',
            'Link': 'https://example.com/roi-report',
            'Description': 'Detailed financial analysis and ROI projections for the inspection system.'
        }
    ]
    
    for ref in references:
        with st.expander(f"{ref['Type']}: {ref['Title']}"):
            st.write(ref['Description'])
            st.markdown(f"[📄 Download/View Resource]({ref['Link']})")
    
    st.markdown("---")
    st.subheader("Additional Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **Videos & Media:**
        - [System Demonstration Video](https://example.com/demo-video)
        - [Harrier Assembly Line Tour](https://example.com/assembly-tour)
        - [Defect Detection in Action](https://example.com/detection-video)
        """)
    
    with col2:
        st.write("""
        **Code & Repositories:**
        - [GitHub Repository](https://github.com/example/mesh-transformer)
        - [Model Weights](https://example.com/model-weights)
        - [Inference Code](https://example.com/inference-code)
        """)
    
    st.markdown("---")
    st.subheader("Contact Information")
    
    st.write("""
    **Project Lead:** Dr. Arvind Mathur  
    **Organization:** Tata Motors Ltd.  
    **Location:** Pimpri-Chinchwad Manufacturing Plant  
    **Email:** contact@example.com  
    **Project Website:** https://example.com/condenser-inspection
    """)
    
    st.markdown("---")
    st.subheader("Acknowledgments")
    
    st.write("""
    This project was developed in collaboration with:
    - Tata Motors Engineering Team
    - AI Research Laboratory
    - Manufacturing Quality Assurance Team
    - Production Line Operators
    
    Special thanks to all mentors, advisors, and team members who contributed to this project.
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "AI Mesh Transformer for Condenser Firewall Inspection | Tata Motors | 2024"
    "</div>",
    unsafe_allow_html=True
)

