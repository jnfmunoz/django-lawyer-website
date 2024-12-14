def get_practice_formatted_icon(icon_value):
        """
        Retorna el campo `icon` formateado correctamente para la clase Practice.
        """
        icon_value = str(icon_value)  # Convertir a cadena para procesarlo
        parts = [part.strip() for part in icon_value.split(',')]  # Separar y limpiar las partes

        # Creamos una lista de clases, primero se agregará el tamaño fa-2x
        formatted_icon = []

        # Recorrer las partes y verificar si hay un prefijo de tipo de icono (fab, fas, etc.)
        for part in parts:
            # Si el prefijo no está presente, lo agregamos (para casos como "accusoft")
            if not part.startswith('fa-'):
                if part.startswith('fab') or part.startswith('fas') or part.startswith('far'):
                    formatted_icon.append(part)  # Si ya tiene "fab", "fas", "far", lo agregamos tal cual
                else:
                    formatted_icon.append(f"fa-{part}")  # Si no, le agregamos el prefijo "fa-"
            else:
                formatted_icon.append(part)  # Si ya tiene "fa-", lo agregamos tal cual

        # Si el icono no tiene un tamaño, se le agrega "fa-2x" después del prefijo
        if formatted_icon[0] not in ['fa-2x']:
            formatted_icon.insert(1, 'fa-2x')  # Insertamos "fa-2x" después del tipo (fab, fas, etc.)

        return ' '.join(formatted_icon)  # Unimos las partes formateadas para el icono

def get_social_network_formatted_icon(icon_value):
        """
        Retorna el campo `icon` formateado correctamente para la clase SocialNetwork.
        Entrada -> fas, envelope
        Salida -> fas fa-envelope
        """
        icon_value = str(icon_value)

