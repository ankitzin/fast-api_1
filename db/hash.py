from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes='bcrypt', deprecated='auto')


class Hash:

    def bcrypt(password: str):
        return pwd_cxt.hash(password)


    def verify(hashed_pwd: str, plain_pwd: str):
        return pwd_cxt.verify(plain_pwd, hashed_pwd)


