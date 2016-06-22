from sqlalchemy import select

from mail_orm import Client, Site


def process_message_hook(self, peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")

    client_id = ''
    client_name = ''
    site_id = ''

    # Use this query to test if mailfrom value can be found in client_email column of clients table
    # and output client_name.
    client_name_mailfrom = select([Client.client_name]).where(Client.client_email == (str(mailfrom)))

    # Use this query to test if mailfrom value can be found in client_email column of clients table
    # and output client_id.
    client_id_mailfrom = select([Client.client_id]).where(Client.client_email == (str(mailfrom)))

    # Use this query to test if client_id value is found in sites table and output site_id.
    client_name_sites = select([Site.client_id]).where(Site.client_id) == (str(client_id))

    results_client_name = engine.execute(client_name_mailfrom)
    engine.close()
    results_client_id = engine.execute(client_id_mailfrom)
    engine.close()
    results_site_id = engine.execute(client_name_sites)
    engine.close()

    for client_id in results_client_id:
        print(''.join(map(str, client_id)))

    for client_name in results_client_name:
        print(''.join(client_name))

    for site_id in results_site_id:
        print(''.join(map(str, site_id)))

    if len(client_id) > 0:
        print("Client Found: " + client_name + client_id)
        if len(site_id) > 0:
            print("Site Found: " + site_id)
        else:
            print("Site not found.")
    else:
        print("Client not found.")

