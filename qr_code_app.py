import qrcode
from PIL import Image


def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


def decode_qr_code(filename):
    img = Image.open(filename)
    result = qrcode.QRCode()
    result.add_data(img)
    return result.data.decode("utf-8")


def main():
    while True:
        print("QR Code Generator and Decoder")
        print("----------------------------")
        print("1. Generate QR Code")
        print("2. Decode QR Code")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            data = input("Enter the data to encode: ")
            filename = input("Enter the filename to save the QR code as: ")
            generate_qr_code(data, filename)
            print(f"QR code generated and saved as {filename}!")

        elif choice == "2":
            filename = input("Enter the filename of the QR code to decode: ")
            data = decode_qr_code(filename)
            print(f"Decoded data: {data}")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
