import streamlit as st
import qrcode
from PIL import Image
import io

st.title("QR Code Generator")

data = st.text_input("Enter the text or URL for the QR Code:", "")

box_size = st.slider("Box Size (size of each box in the grid)", 1, 20, 10)
border = st.slider("Border Size (thickness of the border)", 1, 10, 4)

if st.button("Generate QR Code"):
    if data:
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)

        
        img = qr.make_image(fill_color="black", back_color="white")

        
        img_buffer = io.BytesIO()              # Convert the PIL image to a bytes-like object
        img.save(img_buffer, format="PNG")
        img_buffer.seek(0)

       
        st.image(img_buffer, caption="Your QR Code", use_column_width=True)  #result

       
        st.download_button(                                #download function
            label="Download QR Code",
            data=img_buffer,
            file_name="qrcode.png",
            mime="image/png",
        )
    else:
        st.error("Please enter some text or a URL to generate a QR Code.")
