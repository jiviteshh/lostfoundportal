from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import FoundItem, LostItem  # Import your models

# ✅ Home Page
def home(request):
    return render(request, 'Homepage.html')

# ✅ Lost Page
def lost(request):
    return render(request, 'Lostpage.html')

# ✅ Found Page
def found(request):
    return render(request, 'Foundpage.html')

# ✅ List Found Items
def listfound(request):
    found_items = FoundItem.objects.all()
    return render(request, 'listfounditems.html', {'found_items': found_items})

# ✅ List Lost Items
def listlost(request):
    lost_items = LostItem.objects.all()
    return render(request, 'listlostitems.html', {'lost_items': lost_items})


def submit_found_item(request):
    if request.method == "POST":
        item_description = request.POST.get("item-description")
        location_found = request.POST.get("location-found")
        date_found = request.POST.get("date-found")
        upload_photo = request.FILES.get("upload-photo")
        contact_info = request.POST.get("contact-info")

        FoundItem.objects.create(
            item_description=item_description,
            location_found=location_found,
            date_found=date_found,
            upload_photo=upload_photo,
            contact_info=contact_info
        )

        messages.success(request, "✅ Found item added successfully!")  
        return redirect('listfound')

    return render(request, 'Foundpage.html')

# ✅ Report Lost Item
def report_lost_item(request):
    if request.method == "POST":
        item_description = request.POST.get("item-description")
        location_lost = request.POST.get("location-lost")
        date_lost = request.POST.get("date-lost")
        upload_photo = request.FILES.get("upload-photo")
        contact_info = request.POST.get("contact-info")

        LostItem.objects.create(
            item_description=item_description,
            location_lost=location_lost,
            date_lost=date_lost,
            upload_photo=upload_photo,
            contact_info=contact_info
        )

        messages.success(request, "✅ Lost item reported successfully!")  
        return redirect('listlost')

    return render(request, 'Lostpage.html')

# ✅ Delete Found Item
def delete_found_item(request, item_id):
    item = get_object_or_404(FoundItem, id=item_id)
    
    if request.method == "POST":
        item.delete()
        messages.success(request, "❌ Found item deleted successfully.")
        return redirect("listfound")  
    
    return render(request, "Confirmdelete.html", {"item": item})

# ✅ Delete Lost Item
def delete_lost_item(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)
    
    if request.method == "POST":
        item.delete()
        messages.success(request, "❌ Lost item deleted successfully.")
        return redirect("listlost")  

    return render(request, "Confirmdelete.html", {"item": item})
