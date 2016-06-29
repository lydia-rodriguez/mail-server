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
                client_id = results_client_id[0]
            else:
                client_names = select([Client])
                client_names_list = conn.execute(client_names).fetchall()
                for client_name in client_names_list:
                    print(1)
                    if mailfrom_lwr.count(client_name.client_name.lower()) > 0:
                        print(2)
                        client_id = client_name.client_id
                        break
                else:
                    for client_syn1 in client_names_list:
                        print(3)
                        print(client_syn1)
                        if mailfrom_lwr.count(client_syn1.synonym1.lower()) > 0:
                            client_id = client_syn1.client_id
                            print("a string")
                            print(client_syn1.synonym1)
                            break
                    else:
                        for client_syn2 in client_names_list:
                            print(4)
                            print(client_syn2)
                            if mailfrom_lwr.count(client_syn2.synonym2.lower()) > 0:
                                print("b string")
                                print(client_syn2)
                                client_id = client_syn2.client_id
                                break
                        else:
                            for client_syn3 in client_names_list:
                                print(5)
                                print(client_syn3)
                                if mailfrom_lwr.count(client_syn3.synonym3.lower()) > 0:
                                    client_id = client_syn3.client_id
                                    print("c string")
                                    print(client_syn3)
                                    break

    except Exception as error:
        print(error)
    if client_id:
        print("Client ID: " + str(client_id))
    else:
        print("Client not found.")
