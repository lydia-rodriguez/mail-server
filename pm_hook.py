from mail_orm import Client
from sqlalchemy import select, column


def process_message_hook(peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")
    # print(mailfrom)

    s = select([Client.client_name]).where(Client.client_email == (str(mailfrom)))
    results = engine.execute(s)
<<<<<<< HEAD

    for row in results:
        # print("\n".join(row))
        # print(row)
        if 'FSG_TEST' in row:
            print("Found")
        else:
            print("Error. Please debug.")
=======
    if s is not None:
        for row in results:
            print("Match found: ".join(row))
    else:
        print("No match found. Please resend email.")
>>>>>>> parent of 3976c1e... added print statements to test added conditional statements, updated
