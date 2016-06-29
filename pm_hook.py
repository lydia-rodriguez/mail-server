from sqlalchemy import select

from mail_orm import Client, Site


def process_message_hook(self, peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")

    connection = engine.connect()

    client_id = None
    client_name = None
    site_name = None
    mailfrom_lwr = mailfrom.lower()

    print(mailfrom_lwr)

    # Use this query to test if mailfrom value can be found in client_email column of clients table
    # and output client_id.
    client_id_mailfrom = select([Client.client_id]).where(Client.client_email == mailfrom_lwr)

    try:
        with engine.connect() as conn:
            results_client_id = conn.execute(client_id_mailfrom).first()

            if results_client_id:
                client_id = results_client_id
            else:
                client_names = select([Client])
                client_names_list = conn.execute(client_names).fetchall()
                for client in client_names_list:
                    if mailfrom_lwr.count(client.client_name.lower()) > 0:
                        client_id = client.client_id
                        break
    except:
        print("Client ID not found using mailfrom.")
    if client_id:
        print("Client ID: " + str(client_id))
    else:
        print("Client not found.")
