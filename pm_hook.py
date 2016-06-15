from mail_orm import Client
from sqlalchemy import select, column


def process_message_hook(peer, mailfrom, rcpttos, data, engine):
    print("Message processed.")
    print(mailfrom)

    clients_list = select([Client.client_email]).having(mailfrom)
    print(clients_list)

    client_email = column('client_email')
    s = select([Client.c.client_email]).where(Client.c.client_email == (str(mailfrom)))

    results = engine.execute(s)

    for row in results:
        print(row)
