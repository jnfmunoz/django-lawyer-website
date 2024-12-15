from .models import SocialNetwork, Address, ContactInfo

def social_network(request, *args, **kwargs):
    social_networks = SocialNetwork.objects.all()

    formatted_social_networks = []
    for network in social_networks:
        formatted_icon_value = network.get_social_network_formatted_icon()
        formatted_social_networks.append({
            'description': network.description,
            'icon': formatted_icon_value,
            'link': network.link,
        })

    context = {
        'social_network': formatted_social_networks
    }

    return context

def address(request, *args, **kwargs):
    address = Address.objects.all()

    context = {
        'address': address
    }
    
    return context

def contact_info(request, *args, **kwargs):
    contact_info = ContactInfo.objects.all()

    context = {
        'contact_info': contact_info,
    }

    return context