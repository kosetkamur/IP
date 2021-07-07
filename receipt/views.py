from django.http import HttpResponse
from django.shortcuts import redirect


def redirect_receipt(request):
    return redirect('receipts_list_urls', permanent=True)
    from django.shortcuts import render
