from django import template
from django.utils.safestring import mark_safe
from main.models import Product, VideoLaptop, OperatingSystemLaptop, Category
from django.db.models import Q
from operator import or_, and_
from django.db.models import Count
from django.db import models
from django.db.models import Count, Avg, Sum

register = template.Library()
TABLE_HEAD = """
      
        <table class="table-base-product-full-information">
          <tbody>
        """
TABLE_TALE = """
          </tbody>
        </table>
     
     """
TABLE_CONTENT = """
          <tr>
           <td class="td-base-product-name" style="color: #ff0; font-family: 'Sprite Graffiti', serif;">{name}</td>
           <td class="td-base-product-value" style="color: #cccc00; font-family: 'Sprite Graffiti', serif;">{value}
           <hr class="div-base-product-line"></td>
           
         </tr>
         
       """
PRODUCT_SPEC = {
    'smartphone': {
        'Operating System': 'operating_system_smartphone',
        'Diagonal': 'diagonal',
        'Type screen': 'type_screen',
        'Resolution': 'resolution_smartphone',
        'Camera': 'camera',
        'Battery charge': 'battery_charge_smartphone',
        'Processor': 'processor_smartphone',
        'RAM': 'ram_smartphone',
        'SD': 'sd',
        'SD volume max': 'sd_volume_max'
        },
    'headphone': {
        'Color': 'color',
        'Fit Type': 'fit_type',
        'Item Dimensions': 'item_dimensions',
        'Item Weight': 'item_weight',
        'Battery': 'battery'
        },
    'laptop': {
        'By series': 'by_series',
        'Operating system': 'operating_system',
        'Screen size': 'screen_size',
        'Resolution': 'resolution',
        'Storage drive size': 'storage_drive_size',
        'Processor': 'processor',
        'RAM': 'ram',
        'Graphics': 'graphics',
        'Touch': 'touch',
        'Battery charge': 'battery_charge'
        }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    laptop_specifications = Product.objects.filter(category_id=1)
    smartphone_specifications = Product.objects.filter(category_id=2)
    headphone_specifications = Product.objects.filter(category_id=3)
    if product.category_id == 1:
        PRODUCT_SPEC['laptop'] = laptop_specifications
    if product.category_id == 2:
        PRODUCT_SPEC['smartphone'] = smartphone_specifications
    if product.category_id == 3:
        PRODUCT_SPEC['headphone'] = headphone_specifications
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TALE)


@register.filter(name='get_val')
def get_val(dict, key):

    return dict.get(key)







