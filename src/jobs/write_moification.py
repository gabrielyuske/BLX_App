def write_notfy(email: str,message=""):
    with open("log.txt",mode="a")as email_file:
        conteudo = f"Email: {email} - msg: {message}\n"
        email_file.write(conteudo)