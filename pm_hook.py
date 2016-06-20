from mail_orm import Client
from sqlalchemy import select, column


def process_message_hook(peer, mailfrom, rcpttos, data, engine):
    print("Message processed.")
    # print(mailfrom)

    client_email = column('client_email')
    s = select([Client.client_email]).where(Client.client_email == (str(mailfrom)))

    results = engine.execute(s)

    for row in results:
        print("".join(row))
