import qrcode
from io import BytesIO
from django.core.files import File

def make_qr(user_token, showtime_data):
    data = str(user_token) + str(showtime_data.replace(' ', '_'))
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    filename = f"qr_{user_token}_{showtime_data.replace(' ', '_')}.png"
    return File(buffer, name=filename)
    