from django.shortcuts import render, get_object_or_404, redirect
from .models import ExcelData
from .forms import ExcelDataForm

# List View
def excel_data_table(request):
    query = request.GET.get('q', '')  # Search functionality
    if query:
        data = ExcelData.objects.filter(city__icontains=query)  # Filter by city
    else:
        data = ExcelData.objects.all()  # Show all entries
    return render(request, 'excel_data_table.html', {'data': data, 'query': query})

# Detail View
def excel_data_detail(request, pk):
    data = get_object_or_404(ExcelData, pk=pk)
    return render(request, 'excel_data_detail.html', {'data': data})

# Create View
def excel_data_create(request):
    if request.method == 'POST':
        form = ExcelDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('excel_data_table')
    else:
        form = ExcelDataForm()
    return render(request, 'excel_data_form.html', {'form': form, 'title': 'Create New Entry'})

# Update View
def excel_data_update(request, pk):
    data = get_object_or_404(ExcelData, pk=pk)
    if request.method == 'POST':
        form = ExcelDataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('excel_data_table')
    else:
        form = ExcelDataForm(instance=data)
    return render(request, 'excel_data_form.html', {'form': form, 'title': 'Update Entry'})

# Delete Confirmation View
def excel_data_delete(request, pk):
    data = get_object_or_404(ExcelData, pk=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('excel_data_table')
    return render(request, 'excel_data_confirm_delete.html', {'data': data})
