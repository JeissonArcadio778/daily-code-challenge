"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""

"""
[
    {
        "bread": "panchocha",
        "cooking": "TODAY",
        "factory_price": 1000
        
    },
    {
        "bread": "pan200",
        "cooking": "YESTERDAY",
        "factory_price": 200
        
    },{
        "bread": "empanada",
        "cooking": "TODAY",
        "factory_price": 500
    },
]

"""

def sales_bread(data:list) -> list:
    record_sales_bread = []
    for item in data:
        if item["cooking"] == "TODAY":
            item["sale_price"] = item["factory_price"]
        elif item["cooking"] == "YESTERDAY":
            sale_price = int(item["factory_price"] * (40/100))
            item["sale_price"] = sale_price
        else: 
            item["sale_price"] = 0
        record_sales_bread.append(item)
        
    return record_sales_bread



inventory = [
    {
        "bread": "panchocha",
        "cooking": "TODAY",
        "factory_price": 1000
        
    },
    {
        "bread": "pan200",
        "cooking": "YESTERDAY",
        "factory_price": 200
        
    },{
        "bread": "empanada",
        "cooking": "TODAY",
        "factory_price": 500
    },
]


print(sales_bread(inventory))

