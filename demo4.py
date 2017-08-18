# coding=utf-8
import rsa
import random
import string


def Create_publi_priv_file():
    """
    创建密钥文件
    :return:
    """
    (pubkey, privkey) = rsa.newkeys(1024)

    pub = pubkey.save_pkcs1()
    pubfile = open("public.pem", "w+")
    pubfile.write(pub)
    pubfile.close()

    pri = privkey.save_pkcs1()
    prifile = open("private.pem", "w+")
    prifile.write(pri)
    prifile.close()


def Load_publi_priv_file():
    """
    加载密钥文件
    :return:
    """
    with open("public.pem") as publickfile:
        p = publickfile.read()
        pubkey = rsa.PublicKey.load_pkcs1(p)

    with open("private.pem") as privatefile:
        p = privatefile.read()
        prikey = rsa.PrivateKey.load_pkcs1(p)

    return pubkey, prikey

def activation_code(id, mac_addr, end_time, length):
    '''
    id + mac地址 + 到期时间(2015-01-01)
    :return:激活码
    '''
    prefix = hex(int(id))[2:] + mac_addr + end_time
    print len(prefix)
    length = length - len(prefix)
    chars = string.ascii_letters + string.digits
    return prefix + ''.join([random.choice(chars) for i in range(length)])

if __name__ == "__main__":
    # 生成邀请码
    code = activation_code(1,"000c29ac76e3","2015-01-01", 30)
    print code
    # 先生成一对密钥，然后保存.pem格式文件
    Create_publi_priv_file()
    # load 公钥和密钥
    (pubkey, prikey) = Load_publi_priv_file()
    # 用密钥加密
    crypto = rsa.encrypt(code,pubkey)
    # 用公钥解密
    message = rsa.decrypt(crypto, prikey)
    print crypto
    print code
