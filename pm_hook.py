from sqlalchemy import select

from mail_orm import Client


def process_message_hook(mailfrom, engine):
    print("\nMessage processed.")

    s = select([Client.client_name]).where(Client.client_email == (str(mailfrom)))
    results = engine.execute(s)

    for row in results:
        # print("\n".join(row))
        
        c = str(row)

        if "FSG" in c:
            print("Found.")
        else:
            print("Not found.")
