from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def index(request):
    return render(request, 'main/index.html')


def alert(request):
    return render(request, 'main/alert.html')


def remote(request):
    if request.method == 'POST':
        # Получаем ID ачивки из формы
        achievement_id = request.POST.get('achievement_id', '1')

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "alert_group",
            {
                "type": "alert_message",
                "achievement_id": achievement_id,  # Передаем ID дальше
            }
        )
        return render(request, 'main/remote.html', {'sent': True})

    return render(request, 'main/remote.html')