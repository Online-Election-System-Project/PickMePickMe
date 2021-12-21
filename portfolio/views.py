from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Portfolio
from .forms import PortfolioForm

def portfolio_list(request):
    portfolios = Portfolio.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'portfolio/portfolio_list.html', {'portfolios' : portfolios})

def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio' : portfolio})

def portfolio_new(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            # portfolio.candidate = request.user
            portfolio.save()
            return redirect('portfolio_detail', pk=portfolio.pk)
    else:
        form = PortfolioForm()
    return render(request, 'portfolio/portfolio_edit.html', {'form': form})

def portfolio_edit(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if request.method == "POST":
        form = PortfolioForm(instance=portfolio)
        if form.is_valid():
            portfolio = form.save(commit=False)
            # portfolio.candidate = request.user
            portfolio.save()
            return redirect('portfolio_detail', pk=portfolio.pk)
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'portfolio/portfolio_edit.html', {'form': form})