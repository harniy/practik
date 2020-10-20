from django import template
from categories.models import Category
register = template.Library()


@register.inclusion_tag('tags/category.html')
def get_categories():
    category = Category.objects.all()
    return {'categories': category}

# @register.simple_tag()
# def get_categories():
#     return Category.objects.all()