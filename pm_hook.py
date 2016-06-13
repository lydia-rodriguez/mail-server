from mail_orm import Client
from sqlalchemy import select


def process_message_hook(peer, mailfrom, rcpttos, data):
    print("Message processed.")
    print(mailfrom)

    clientsList = select([Client.c.client_email]).where(
        Client.c.client_email.in_(mailfrom)
    )

    for x in clientsList:
        print(x)
