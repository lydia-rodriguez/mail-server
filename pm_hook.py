from mail_orm import Client
from sqlalchemy import select, column


def process_message_hook(peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")

    s = select([Client.client_name]).where(Client.client_email == (str(mailfrom)))
    results = engine.execute(s)

    for row in results:
        print("\n".join(row))
