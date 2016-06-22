from sqlalchemy import select

from mail_orm import Client


def process_message_hook(self, peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")

    client = ''

    # Use this query to test if mailfrom value can be found in client_email column of clients table
    client_email_mailfrom = select([Client.client_name]).where(Client.client_email == (str(mailfrom)))

    # Use this query to test if client_name value is found
    # client_name_sites = select([])
    
    results = engine.execute(client_email_mailfrom)
    for r in results:
        print(r)

    if len(results.fetchall()) > 0:
        print("Found.")

    else:
        print("Not found.")
