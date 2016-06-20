from mail_orm import Client
from sqlalchemy import select, column


def process_message_hook(peer, mailfrom, rcpttos, data, engine):
    print("\nMessage processed.")
    print(mailfrom)

    s = select([Client.client_name]).where(Client.client_email == (str(mailfrom)))
    results = engine.execute(s)
    for row in results:
        print("\n".join(row))

        if s is None:
            print("No match found. Please resend email.")
        if s is not None:
            print("Match(es) found:")
            print("\n".join(row))
        else:
            print("Error. Please debug.")
