# 
from fake_useragent import UserAgent

# 不校验ssl信息
ua = UserAgent(verify_ssl=False)

print(ua.chrome)
print(ua.safari)
print(ua.ie)

print(ua.random)