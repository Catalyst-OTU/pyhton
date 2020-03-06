stock = {}
class Invent:
    def  __init__(self, p_id,p_name):
        self.p_id = p_id
        self.p_name= p_name
def add_product(prod):
    if not stock.get(prod.p_id):
            stock[prod.p_id] = 1
    else:
            stock[prod.p_id] += 1

prod = Invent('chairs',1)
add_product(prod)
print (stock)

add_product(prod)
add_product(prod)
add_product(prod)
print (stock)



















'''
empty_devices = {}
e_devices= {}
e_devices= {'name':'computers','id':'e#1'}
print(e_devices)


prod = {}
def add_device(dv):
    if not prod.get(dv.pid):
            prod[dv.pid] = 1
    else:
            prod[dv.pid] += 1
print(add_device())'''
