import streamlit as st
import cv2
import numpy as np
from fpdf import FPDF

def overlay_grid(image, grid_step, show_grid):
    if show_grid:
        grid_image = image.copy()
        for x in range(0, image.shape[1], grid_step):
            cv2.line(grid_image, (x, 0), (x, image.shape[0]), (255, 0, 0), 1)
        for y in range(0, image.shape[0], grid_step):
            cv2.line(grid_image, (0, y), (image.shape[1], y), (255, 0, 0), 1)
        return grid_image
    return image

def measure_image(image, grid_step):
    img_height, img_width, _ = image.shape

    measurements = []
    for y in range(0, img_height, grid_step):
        for x in range(0, img_width, grid_step):
            cell_width = min(x + grid_step, img_width) - x
            cell_height = min(y + grid_step, img_height) - y
            measurements.append({
                "x": x,
                "y": y,
                "width": cell_width,
                "height": cell_height
            })

    return {
        "image_width": img_width,
        "image_height": img_height,
        "grid_step": grid_step,
        "grid_measurements": measurements
    }

def save_as_pdf(output_dict):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Image Measurements", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, f"Image Width: {output_dict['image_width']} pixels", ln=True)
    pdf.cell(200, 10, f"Image Height: {output_dict['image_height']} pixels", ln=True)
    pdf.cell(200, 10, f"Grid Step: {output_dict['grid_step']} pixels", ln=True)
    pdf.ln(10)

    pdf.cell(200, 10, "Grid Measurements:", ln=True)
    for measurement in output_dict['grid_measurements']:
        pdf.cell(200, 10, f"Cell at ({measurement['x']}, {measurement['y']}):", ln=True)
        pdf.cell(200, 10, f"  Width: {measurement['width']} pixels", ln=True)
        pdf.cell(200, 10, f"  Height: {measurement['height']} pixels", ln=True)

    pdf.output("image_measurements.pdf")

def main():
    st.title("Image Measurement Tool")
    
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)
        grid_step = st.slider("Grid Step", 10, 100, 20)
        show_grid = st.checkbox("Show Grid")

        image_with_grid = overlay_grid(image, grid_step, show_grid)
        output_dict = measure_image(image, grid_step)
        save_as_pdf(output_dict)

        st.image(image_with_grid, channels="BGR")
        st.download_button("Download PDF Report", data=open("image_measurements.pdf", "rb").read(), file_name="image_measurements.pdf")

if __name__ == "__main__":
    main()
