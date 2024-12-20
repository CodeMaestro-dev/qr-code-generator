from django.shortcuts import render
from io import BytesIO
import qrcode
import base64
from .forms import CreateQRCode

def index(request):
    qr_code_image = None  # To hold the base64 representation of the QR code image
    
    if request.method == 'POST':
        form = CreateQRCode(request.POST)
        
        if form.is_valid():
            # Extract the value from the form
            website_link = form.cleaned_data['qr_code_text']

            # Generate the QR code
            qr = qrcode.QRCode(version=1, box_size=5, border=5)
            qr.add_data(website_link)
            qr.make()

            # Create the QR code image
            img = qr.make_image(fill_color='black', back_color='white')

            # Convert the image to base64 for embedding in the template
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            qr_code_image = f"data:image/png;base64,{image_base64}"
    else:
        form = CreateQRCode()
    
    return render(request, 'home.html', {'form': form, 'qr_code_image': qr_code_image})
