from mail_orm import Client
from sqlalchemy import select, column


def process_message_hook(peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")
    # print(mailfrom)

    s = select([Client.client_name]).where(Client.client_email == (str(mailfrom)))
    results = engine.execute(s)


    for row in results:
        client = row
        print(client)

    if 'FSG' in client:
        print("Found>")
    else:
        print("Error. Please debug.")








            #     # print(row)
    #     if 'FSG_TEST' in results:
    #         print("Match(es) found:")
    #         print("\n".join(row))
    #     else:
    #         print("Error. Please debug.")
