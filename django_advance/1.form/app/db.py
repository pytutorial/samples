products = [
    {'id':1, 'code': '10001', 'name': 'P1', 'description': '', 'price': 10000},
    {'id':2, 'code': '10002', 'name': 'P2', 'description': '', 'price': 20000}
]

def getProductById(id):
    for p in products:
        if p['id'] == id:
            return p

def getProductByCode(code):
    for p in products:
        if p['code'] == code:
            return p

def addProduct(form):
    params = form.cleaned_data
    p = params
    maxid = products[-1]['id']
    p['id'] = maxid + 1
    products.append(p)

def updateProduct(id, form):
    params = form.cleaned_data
    p = getProductById(id)
    if p:
        p.update(params)

def deleteProduct(id):
    for p in products:
        if p['id'] == id:
            products.remove(p)
