from .models import SocialNetwork

def social_network(request, *args, **kwargs):
    social_networks = SocialNetwork.objects.all()

    # Crear una lista con los valores formatedos
    formatted_social_networks = []
    for network in social_networks:
        formatted_icon_value = network.get_social_network_formatted_icon()
        formatted_social_networks.append({
            'formatted_icon': formatted_icon_value,
            'description': network.description,
            'social_type': network.social_type,
            'social_value': network.social_value,
        })

    # Separar por tipo
    emails = [n for n in formatted_social_networks if n['social_type'] == 'email']
    phone = [n for n in formatted_social_networks if n['social_type'] == 'phone']
    social = [n for n in formatted_social_networks if n['social_type'] == 'social']

    # Combinar en el orden deseado
    ordered_social = emails + phone + social

    # print(ordered_social)

    context = {
        'social_network': ordered_social,
    }
    
    return context
