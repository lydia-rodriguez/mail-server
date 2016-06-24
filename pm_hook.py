from sqlalchemy import select

from mail_orm import Client, Site


def process_message_hook(self, peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")

    connection = engine.connect()

    client_id = '1'
    client_name = ''
    site_id = ''



    # Use this query to test if mailfrom value can be found in client_email column of clients table
    # and output client_name.
    client_name_mailfrom = select([Client.client_name]).where(Client.client_email == (str(mailfrom)))

    # Use this query to test if mailfrom value can be found in client_email column of clients table
    # and output client_id.
    client_id_mailfrom = select([Client.client_id]).where(Client.client_email == (str(mailfrom)))

    site_id = 5

    with engine.connect() as conn:
        results_client_name = conn.execute(client_name_mailfrom)
        ## some code
    with engine.connect() as conn:
        results_client_id = conn.execute(client_id_mailfrom)
        ## some code

    # Use this query to test if client_id value is found in sites table and output site_id.
    client_sites = select([Site.client_id]).where(Site.client_id == int(client_id))

    with engine.connect() as conn:
        results_site_id = conn.execute(client_sites)
        ## some code

    for client_id in results_client_id:
        print(''.join(map(str, client_id)))

    for client_name in results_client_name:
        print(''.join(client_name))

    for site_id in results_site_id:
        print(''.join(map(str, site_id)))

    if len(client_name) > 0:
        print("Client Found: " + str(client_name) + str(client_id))
        if site_id > 0:
            print("Site Found: " + str(site_id))
        else:
            print("Site not found.")
    else:
        print("Client not found.")
