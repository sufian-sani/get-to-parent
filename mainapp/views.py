from django.shortcuts import render
from .models import *

from django.http import JsonResponse
import json
# Create your views here.


def findchildcatagory(category_all,category_id):
    # print('category_all',category_all)
    cate_list = []
    cate_list.append(category_id)
    category_id_u = 0
    category_id_u_id = 0
    # print('category_id',category_id)
    for i in category_all:
        if i.parent_id:
            category_id = category_id
            # print('i',i)
            # print(i,i.id, i.parent_id)
            # print('parent_id',i.parent_id)
            
            if i.parent_id == category_id:
                # print(i.id)
                # category_id = i.id
                # print('i.parent_id',category_id)
                cate_list.append(i.id)
                # print('category_id_u_id',category_id_u_id)
        # category_id=category_id
    # print(cate_list)
    if len(cate_list) != 0:
        for i in cate_list:
            for j in category_all:
                if j.parent_id:
                    category_id_update = i
                    if j.parent_id == category_id_update:
                        # print('j',j.id)
                        cate_list.append(j.id)
    # print(cate_list)
    my_finallist = [i for j, i in enumerate(cate_list) if i not in cate_list[:j]] 
    print(my_finallist)

    return my_finallist
    


                
            
    #         category_id_u = category_id
    #         if i.parent_id == category_id_u:
    #             print(i.parent_id, category_id_u)
    #             cate_list.append(category_id_u)
    #         category_id_u = i.id
    # print(cate_list)
    # print(category_all, category_id)
    
    # print(type(category_i),category_id)
    # if category_i.parent_id == category_id:
    #     if category_i.parent:
            
    # for i in category_i:
    #     if i.parent == category_id:
    #         print(i)
    # print(cat_id_list)

def getproduct(request, pk):
    # print('pk',pk)
    category = Category.objects.get(id=pk)
    print('category',category)

    # product = Product.objects.filter(category=category)
    # print(product)

    # findchildcatagory

    category_all = Category.objects.all().exclude(id=category.id)
    cate_list = findchildcatagory(category_all, category.id)
    # print('cate_list',cate_list)

    product = []

    for i in cate_list:
        product += Product.objects.filter(category=i)
        # print(product)

    for j in product:
        print('j',j, j.id)

    context = {
        'product':product,
        'cate_list':cate_list,
    }

    # print('product',type(product))


    # for i in category_all:
    #     if i.parent:
    #         # print(i, 'yes')
    #         findchildcatagory(i, category.id)


    # if category.children:
    #     print('yes')
    return render(request, 'products.html', context)

    


def index(request):

    product = Product.objects.all()
    category = Category.objects.all()
    # TreeNodeChoiceField
    # products = Product.objects.filter(category__in=category.get_descendants(include_self=True))
    # products = Product.objects.filter(category__in=category.get_descendant_count())

    # for i in product:
    #     print(i.title, i.category)

    # for i in products:
    #     print(i.title, i.category)

    # products = Product.objects.filter(category__in=category.get_descendants(include_self=True))

    # categories = Category.objects.filter(products__in=products.get_descendants(include_self=True))
    # category = Category.objects.filter(id=1)
    # print(category)

    # for i in categories:
    #     print(i.name)

    # getproduct()


    context = {
        'product':product,
        'category':category,
    }

    return render(request, 'index.html',context)

# def ajaxindex(request):
#     print('dfmfkhk')
#     product = Product.objects.all()
#     category = Category.objects.all()
#     # TreeNodeChoiceField
#     products = Product.objects.filter(category__in=category.get_descendants(include_self=True))
#     # products = Product.objects.filter(category__in=category.get_descendant_count())

#     # for i in product:
#     #     print(i.title, i.category)

#     for i in products:
#         print(i.title, i.category)


#     context = {
#         'product':product,
#         'category':category,
#         'products':products,
#     }
#     print(context)

#     return JsonResponse(context)

# def index(request):
#     if request.method == 'GET':
#         category_id = int(request.GET.get('category_id', default=1))
#         print('category_id',category_id)
#         current_category = Category.objects.get(pk=category_id)

#         children = current_category.get_children()
#         ancestors = current_category.get_ancestors()
#         products = current_category.products.all()

#         context = {
#             'categories': children,
#             'current_category': current_category,
#             'ancestors': ancestors,
#             'products': products,
#         }

#     return render(request, 'index.html', context)

# def index(request):

#     product = Product.objects.all()
#     category = Category.objects.all()
#     print('category',category)
#     context = {
#         'product':product,
#         'category':category,
#     }

#     return render(request, 'index.html',context)