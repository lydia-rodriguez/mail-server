from mail_orm import Client
from sqlalchemy import select


def process_message_hook(peer, mailfrom, rcpttos, data):
    print("Message processed.")
    print(mailfrom)

    clients_list = select([Client.client_email]).having(mailfrom)
    print(clients_list)
