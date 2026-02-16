# config.py

# Configurações para os embeds (mensagens formatadas)
EMBED_CONFIG = {
    "title": "",  # Maine Embed Title here
    "description": "",  # Main Embed Description here
    "color": 0xFF5733,  # Change embed color if you want (red)
    "fields": [
        {"name": "test", "value": "test", "inline": False},  # Embed Field → Juste Modify → Just edit the empty places
        {"name": "test", "value": "test", "inline": False},
        {"name": "test", "value": "test", "inline": False},  # Exemple → "name": "Title 1", "value": "Hello, here is my message", "inline": False
    ],
    "image": "",  # Embed Icon url here → https://image.jpg
    "footer": "",  # Embed Footer here
}

# Configurações para alterar o servidor
SERVER_CONFIG = {
    "new_name": "P1-THE PROJECT NEXUS",  # New Server Name here
    "new_icon": "",  # New Server Icon url here → https://image.jpg
    "new_description": "",  # New Server Description here
}

# Configurações para o comando auto_raid
AUTO_RAID_CONFIG = {
    "num_channels": 200,  # Número de canais
    "channel_type": "text",  # Tipo de canal: 'text' ou 'voice'
    "channel_name": "P1 ON TOP ",  # Nome do canal (recomendo preencher para evitar erros)
    "num_messages": 20,  # Número de mensagens a enviar
    "message_content": "P1 ON TOP"  # Conteúdo da mensagem (recomendo preencher para evitar erros)
}

# Lista de IDs que não devem ser banidos
NO_BAN_KICK_ID = [
    000000000000,  # Substitua pelo ID real de usuários protegidos
    111111111111,
    222222222222,
]

# Configurações de presença do bot
BOT_PRESENCE = {
    "type": "playing",  # Pode ser 'playing', 'watching', 'listening', etc.
    "text": "NxStorm | !help"
}
