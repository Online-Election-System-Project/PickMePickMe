from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Promotion
from .forms import PromotionForm


def promotion_list(request):
    promotions = Promotion.objects.filter().order_by()
    return render(request, "promotion/promotion_list.html", {"promotions": promotions})


def promotion_detail(request, pk):
    promotion = get_object_or_404(Promotion, pk=pk)
    return render(request, "promotion/promotion_detail.html", {"promotion": promotion})


def promotion_new(request):
    if request.method == "POST":
        form = PromotionForm(request.POST)
        print("hello1")
        print(form.errors)
        if form.is_valid():
            print("hello2")
            promotion = form.save(commit=False)
            promotion.user = request.user
            promotion.status = Promotion.STATUS_WATING
            promotion.save()
            return redirect("promotion_detail", pk=promotion.pk)
    else:
        form = PromotionForm()
    return render(request, "promotion/promotion_edit.html", {"form": form})


def promotion_edit(request, pk):
    promotion = get_object_or_404(Promotion, pk=pk)
    if request.method == "POST":
        form = PromotionForm(instance=promotion)
        if form.is_valid():
            promotion = form.save(commit=False)
            promotion.status = Promotion.STATUS_WATING
            promotion.save()
            return redirect("promotion_detail", pk=promotion.pk)
    else:
        form = PromotionForm(instance=promotion)
    return render(request, "promotion/promotion_edit.html", {"form": form})
