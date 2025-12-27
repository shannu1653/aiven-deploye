from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Event
import cloudinary.uploader


# ==============================
# CREATE EVENT (CLOUDINARY)
# ==============================
@csrf_exempt
def create_event(request):
    if request.method == "POST":
        title = request.POST.get("title")
        date = request.POST.get("date")
        price = request.POST.get("price")
        category = request.POST.get("category")
        description = request.POST.get("description")
        image_file = request.FILES.get("image")

        if not title or not date:
            return JsonResponse({"error": "Title and Date required"}, status=400)

        image_url = None

        # ✅ Upload to Cloudinary
        if image_file:
            upload = cloudinary.uploader.upload(
                image_file,
                folder="events",
                use_filename=True,
                unique_filename=True
            )
            image_url = upload["secure_url"]

        event = Event.objects.create(
            title=title,
            date=date,
            price=price,
            category=category,
            description=description,
            image=image_url
        )

        return JsonResponse({
            "message": "Event created successfully",
            "id": event.id,
            "image": image_url
        })

    return JsonResponse({"error": "Invalid request"}, status=405)


# ==============================
# GET EVENTS
# ==============================
def get_events(request):
    events = Event.objects.all()

    data = []
    for e in events:
        data.append({
            "id": e.id,
            "title": e.title,
            "date": e.date,
            "price": e.price,
            "category": e.category,
            "description": e.description,
            "image": e.image.url if e.image else None  # ✅ FIX
        })

    return JsonResponse(data, safe=False)



# ==============================
# UPDATE EVENT (CLOUDINARY)
# ==============================
@csrf_exempt
def update_event(request, id):
    if request.method == "POST":
        try:
            event = Event.objects.get(id=id)

            event.title = request.POST.get("title")
            event.date = request.POST.get("date")
            event.price = request.POST.get("price")
            event.category = request.POST.get("category")
            event.description = request.POST.get("description")

            image_file = request.FILES.get("image")

            # ✅ Upload new image only if provided
            if image_file:
                upload = cloudinary.uploader.upload(
                    image_file,
                    folder="events",
                    use_filename=True,
                    unique_filename=True
                )
                event.image = upload["secure_url"]

            event.save()

            return JsonResponse({"message": "Event updated successfully"})

        except Event.DoesNotExist:
            return JsonResponse({"error": "Event not found"}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=405)


# ==============================
# DELETE EVENT
# ==============================
@csrf_exempt
def delete_event(request, id):
    try:
        event = Event.objects.get(id=id)
        event.delete()
        return JsonResponse({"message": "Event deleted successfully"})
    except Event.DoesNotExist:
        return JsonResponse({"error": "Event not found"}, status=404)
