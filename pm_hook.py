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
    client_id_mailfrom = select([Client])

    try:
        with engine.connect() as conn:
            client_query = conn.execute(client_id_mailfrom).fetchall()

            for client_email_query in client_query:
                if client_email_query.client_email:
                    if mailfrom_lwr.count(client_email_query.client_email.lower()) > 0:
                        client_id = client_email_query.client_id
            else:
                for client_name in client_query:
                    if mailfrom_lwr.count(client_name.client_name.lower()) > 0:
                        client_id = client_name.client_id
                        break
                else:
                    for client_syn1 in client_query:
                        if client_syn1.synonym1:
                            if mailfrom_lwr.count(client_syn1.synonym1.lower()) > 0:
                                client_id = client_syn1.client_id
                                break
                    else:
                        for client_syn2 in client_query:
                            if client_syn2.synonym2:
                                if mailfrom_lwr.count(client_syn2.synonym2.lower()) > 0:
                                    client_id = client_syn2.client_id
                                    break
                        else:
                            for client_syn3 in client_query:
                                if client_syn3.synonym3:
                                    if mailfrom_lwr.count(client_syn3.synonym3.lower()) > 0:
                                        client_id = client_syn3.client_id
                                        break

            if client_id:

                print("Client ID: " + str(client_id))




            else:

                print("Client not found.")

    except Exception as error:
        print(error)

