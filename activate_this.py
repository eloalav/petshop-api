def filtrar_por_product(products, product_name):
    lista_filtrada = []

    for product in products:
        if product['product_name'].lower() == product_name.lower():
            lista_filtrada.append(product)

    return lista_filtrada

def filtrar_por_description(products, product_description):
    lista_filtrada = []

    for product in products:
        if product['product_description'].lower() == product_description.lower():
            lista_filtrada.append(product)

    return lista_filtrada

def filtrar_por_price(products, product_price):
    lista_filtrada = []

    for product in products:
        if product['product_price'] == product_price:
            lista_filtrada.append(product)

    return lista_filtrada

def filtrar_por_valor_min_max(products, valor_min, valor_max):
    lista_filtrada = []

    for product in products:
        if valor_min <= product['product_price'] <= valor_max:
            lista_filtrada.append(product)

    return lista_filtrada
