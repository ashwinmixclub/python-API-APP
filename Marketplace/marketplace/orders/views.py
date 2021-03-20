from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from orders.models import Order
from lxml import etree
#, Order_status
 
def index(request): 

    x = []
    y = []
    z = []
    t = []
    w = []
    l = []
    
    tree = etree.parse("http://test.lengow.io/orders-test.xml")

    for order1 in tree.xpath("/statistics/orders/order/marketplace"):
        x.append(order1.text)

    for order1 in tree.xpath("/statistics/orders/order/idFlux"):
        y.append(order1.text)

    for order1 in tree.xpath("/statistics/orders/order/order_id"):
        z.append(order1.text)

    for order1 in tree.xpath("/statistics/orders/order/order_amount"):
        t.append(order1.text)

    for i in range(5):
        l.append(x[i])
        l.append(y[i])
        l.append(z[i])
        l.append(t[i])

    l1 = l[0:4]
    l2 = l[4:8]
    l3 = l[8:12]
    l4 = l[12:16]
    l5 = l[16:20]

    order1=Order(marketplace=l1[0],idFlux=l1[1], order_id =l1[2], order_amount = l1[3])
    order1.save()
    order2=Order(marketplace=l2[0],idFlux=l2[1], order_id =l2[2], order_amount = l2[3])
    order2.save()
    order3=Order(marketplace=l3[0],idFlux=l3[1], order_id =l3[2], order_amount = l3[3])
    order3.save()
    order4=Order(marketplace=l4[0],idFlux=l4[1], order_id =l4[2], order_amount = l4[3])
    order4.save()
    order5=Order(marketplace=l5[0],idFlux=l5[1], order_id =l5[2], order_amount = l5[3])
    order5.save()
    

    objects=Order.objects.raw( 'SELECT *, COUNT(*) FROM orders_order GROUP BY order_id HAVING COUNT(*) > 1' )
    html='All orders: <br>'
    for i in objects :
       html = html + '  marketplace: ' + i.marketplace + '  idFlux: ' + i.idFlux + '    order_id : '+ i.order_id + '    order_amount: ' + i.order_amount + '<br>'

    return HttpResponse(html)

