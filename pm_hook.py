from sqlalchemy import select

from mail_orm import Client, Site


def process_message_hook(self, peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")

    connection = engine.connect()

    client_id = ''
    client_name = ''
    site_name = ''
    mailfrom_lwr = mailfrom.lower()

    print(mailfrom_lwr)

    # Use this query to test if mailfrom value can be found in client_email column of clients table
    # and output client_id.
    client_id_mailfrom = select([Client.client_id]).where(Client.client_email == mailfrom_lwr)

    try:
        with engine.connect() as conn:
            results_client_id = conn.execute(client_id_mailfrom).first()
            print(type(results_client_id))
            print(results_client_id)

            if not results_client_id:
                print("also a string")
                client_names = select([Client.client_id, Client.client_name])
                client_names_list = conn.execute(client_names).fetchall()
                for client in client_names_list:
                    print("another string")
                    if mailfrom_lwr.count(client[1]) > 0:
                        client_id = client[0]
                        print("a string")
                        print(type(client_id))
                        print(client_id)


            site_name_fromClient = select([Site.site_name]).where(Site.client_id == results_client_id[0])
            results_site_name = conn.execute(site_name_fromClient).first()
            print(type(results_site_name))
            print(results_site_name)



    except IndexError:
        print("Client ID not found using mailfrom.")

    else:
        print("Client not found.")
