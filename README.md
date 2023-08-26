# Grid-OverlayApp
An interactive Python tool with a web interface that overlays grids on images, measures grid cells, and generates PDF reports. Ideal for analyzing structured image content. Powered by Gradio, OpenCV, and FPDF.
# Image Grid Measurement and Visualization Tool
This repository contains a Python script and an interactive web interface built using the Gradio library, OpenCV, and FPDF. The tool allows users to upload an image, overlay a grid on it, measure different cells in the grid, and generate a PDF report with the image measurements.

# Features
Interactive UI: The Gradio interface provides an intuitive way to upload an image, adjust the grid step size, and choose whether to show the grid lines.

Grid Overlay: The uploaded image can be overlaid with a grid, helping to divide the image into manageable cells for measurement.

Grid Measurement: The script calculates measurements (width, height) for each cell in the grid, providing insights into the content's spatial distribution.

PDF Report Generation: The tool generates a PDF report containing image dimensions, grid step size, and measurements for each cell.

# How to Use
Clone the repository and install the required dependencies: gradio, opencv-python, numpy, and fpdf.
Run the script to start the Gradio interface.
Upload an image.
Adjust the grid step size using the slider.
Choose whether to show the grid lines by checking the checkbox.
The interface will display the uploaded image with the grid overlaid.
The PDF report with image measurements will be generated and saved.
This tool is especially useful for understanding structured content within images, such as maps, diagrams, or layouts, by breaking them down into measurable cells.

# Dependencies
Gradio
OpenCV
NumPy
FPDF
