from sqlalchemy import select

from mail_orm import Client


def process_message_hook(mailfrom, engine):
    print("\nMessage processed.")

    s = select([Client.client_name]).where(Client.client_email == (str(mailfrom)))
    results = engine.execute(s)

    for row in results:
        # print("\n".join(row))

        if len(row) > 0:
            print("Found.")
        else:
            print("Not found.")
