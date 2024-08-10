import qrcode
data = 'https://media.tenor.com/n2fnv0PQHCYAAAAC/avdf.gif'
qr = qrcode.make(data)
qr.save('C:/Users/Cutie/PycharmProjects/Pythonpractice/qrcode.png')
