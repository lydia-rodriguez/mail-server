from sqlalchemy import select

from mail_orm import Client, Site


def process_message_hook(self, peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")

    client_id = ''

    # Use this query to test if mailfrom value can be found in client_email column of clients table
    # and output client_name.
    client_name_mailfrom = select([Client.client_name]).where(Client.client_email == (str(mailfrom)))

    # Use this query to test if mailfrom value can be found in client_email column of clients table
    # and output client_id.
    client_id_mailfrom = select([Client.client_id]).where(Client.client_email == (str(mailfrom)))

    # Use this query to test if client_id value is found in sites table
    # client_name_sites = select([Site.client_id])

    results_name = engine.execute(client_name_mailfrom)
    results_id = engine.execute(client_id_mailfrom)

    for client_id in results_id:
        print(''.join(map(str, client_id)))

    for client_name in results_name:
        print(''.join(client_name))

    if len(client_id) > 0:
        print("Found.")

    else:
        print("Not found.")
