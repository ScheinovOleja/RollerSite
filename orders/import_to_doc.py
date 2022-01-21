import os
import pathlib
from pprint import pprint

from django.core.files import File
from django.http import HttpResponse
from docxtpl import DocxTemplate

from RollerSiteCms.settings import MEDIA_URL
from orders.models import Order


def get_context(pk):
    order = Order.objects.get_or_none(id=pk)
    all_prod = order.productlist_set.all()
    if order.prepayment == 0:
        remnant = order.order_price
    else:
        remnant = order.order_price - order.prepayment
    discount = abs(order.extra_charge) if order.extra_charge < 0 else 0.0
    context = {
        'num_order': order.num_order,
        'full_name': order.user.last_name + ' ' + order.user.first_name + ' ' + order.user.patronymic,
        'phone_number': order.user.phone,
        'address': order.user.address,
        'additional_information': order.user.additional_information if order.user.additional_information else '-',
        'tbl_contents': [prod for prod in all_prod],
        'note': order.note,
        'delivery_price': order.delivery_price,
        'install_price': order.installation_price,
        'order_price': order.order_price,
        'prepayment': order.prepayment,
        'remnant': remnant,
        'ready_day': order.terms_of_readiness,
        'install_day': order.installation_time,
        'discount': discount
    }
    doc = DocxTemplate(os.path.abspath('orders/docs/Specification.docx'))
    doc.render(context)
    save_file = os.path.abspath(f'media/contracts/Spec_{order.num_order.replace("/", "_")}.docx')
    doc.save(save_file)
    file = open(save_file)
    order.contract.save(save_file, File(file))
    order.save()
    return f'Spec_{order.num_order.replace("/", "_")}.docx'
