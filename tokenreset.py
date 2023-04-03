from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(rollno,seconds):
    s=Serializer('djsnbsmjm@1123',seconds)
    return s.dumps({'user':rollno}).decode('utf-8')
    
