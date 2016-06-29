from sqlalchemy import select

from mail_orm import Client, Site


def process_message_hook(self, peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")

    connection = engine.connect()

    client_id = None
    client_name = None
    site_ID = None
    mailfrom_lwr = mailfrom.lower()

    print(mailfrom_lwr)

    # Use this query to test if mailfrom value can be found in client_email column of clients table
    # and output client_id.
    client_id_mailfrom = select([Client])

    try:
        with engine.connect() as conn:
            client_query = conn.execute(client_id_mailfrom).fetchall()

            for client_email_list in client_query:
                if client_email_list.client_email:
                    if mailfrom_lwr.count(client_email_list.client_email.lower()) > 0:
                        client_id = client_email_list.client_id
            else:
                for client_name_list in client_query:
                    if mailfrom_lwr.count(client_name_list.client_name.lower()) > 0:
                        client_id = client_name_list.client_id
                        break
                else:
                    for client_syn1_list in client_query:
                        if client_syn1_list.synonym1:
                            if mailfrom_lwr.count(client_syn1_list.synonym1.lower()) > 0:
                                client_id = client_syn1_list.client_id
                                break
                    else:
                        for client_syn2_list in client_query:
                            if client_syn2_list.synonym2:
                                if mailfrom_lwr.count(client_syn2_list.synonym2.lower()) > 0:
                                    client_id = client_syn2_list.client_id
                                    break
                        else:
                            for client_syn3_list in client_query:
                                if client_syn3_list.synonym3:
                                    if mailfrom_lwr.count(client_syn3_list.synonym3.lower()) > 0:
                                        client_id = client_syn3_list.client_id
                                        break

            if client_id:
                print("Client ID: " + str(client_id))
                site_id_clientID = select([Site.site_name]).where(Site.client_id == client_id)
                site_query = conn.execute(site_id_clientID).fetchall(site_id_clientID)

                for site_name_list in site_query:
                    if site_name_list.site_name:
                        if mailfrom_lwr.count(site_name_list.site_name.lower()) > 0:
                            site_ID = site_name_list.site_id
                            break
                    

                print("Site ID: " + str(site_ID))
            else:
                print("Client not found.")

    except Exception as error:
        print(error)

