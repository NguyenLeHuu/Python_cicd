# app/controllers/add_controller.py

def minute_process(request):
    a = int(request.args.get('sothunhat'))
    b = int(request.args.get('sothuhai'))
    kq = a - b
    return 'Kết quả là: ' + str(kq)
