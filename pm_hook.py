from sqlalchemy import select

from mail_orm import Client, Site


def process_message_hook(self, peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")

    client = ''

    # Use this query to test if mailfrom value can be found in client_email column of clients table
    # client_email_mailfrom = select([Client.client_name]).where(Client.client_email == (str(mailfrom)))
    client_email_mailfrom = select([Client.client_id]).where(Client.client_email == (str(mailfrom)))
    # Use this query to test if client_name value is found
    # client_name_sites = select([Site.client_id])

    results = engine.execute(client_email_mailfrom)
    for client in results:
        print(client)

    if len(client) > 0:
        print("Found.")

    else:
        print("Not found.")
