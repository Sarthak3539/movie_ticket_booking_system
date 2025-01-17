from PIL import Image
import climage
import time
from image import DrawImage
import qrcodeT

def qr_code():
    qrcodeT.qrcodeT('https://github.com/Khalil-Youssefi/qrcodeT')


def payment_window(payment):
    output = climage.convert('img/qr.jpg')
    print(output)


    total=payment
    print(f"Amount to be paid: ₹{total}")
    d=input("Please press Y/y if paid:\n")

    def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        if iteration == total: 
            print()


    if d=="Y" or d=="y":
        #buffer
        items = list(range(0, 57))
        l = len(items)
        printProgressBar(0, l, prefix = 'Progress:', suffix = '  Complete', length = 50)
        for i, item in enumerate(items):
            time.sleep(0.05)
            printProgressBar(i + 1, l, prefix = 'Verifying', length = 50)
        print("\n\nBooking Successful!\n\n")
        

    else:
        exit()

# payment_window()
# qr_code()
