import requests
info = requests.get('https://api.github.com/events')

info.headers

{'date': 'Thu, 04 Jun 2020 22:09:33 GMT',
 'content-type': 'application/json; charset=utf-8',
 'server': 'GitHub.com', 'status': '200 OK',
 'cache-control': 'public, max-age=60, s-maxage=60',
 'vary': 'Accept, Accept-Encoding, Accept, X-Requested-With, Accept-Encoding',
 'etag': 'W/"078bb18598ef42449c62d7d39a8f303a"', 'last-modified': 'Thu, 04 Jun 2020 22:04:33 GMT',
 'x-poll-interval': '60', 'x-github-media-type': 'github.v3; format=json', 'link': '<https://api.github.com/events?page=2>; rel="next", <https://api.github.com/events?page=10>; rel="last"',
 'access-control-expose-headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset',
 'access-control-allow-origin': '*', 'strict-transport-security': 'max-age=31536000; includeSubdomains; preload', 'x-frame-options': 'deny', 'x-content-type-options': 'nosniff',
 'x-xss-protection': '1; mode=block', 'referrer-policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'content-security-policy': "default-src 'none'",
 'content-encoding': 'gzip', 'X-Ratelimit-Limit': '60', 'X-Ratelimit-Remaining': '58',
 'X-Ratelimit-Reset': '1591310892', 'Accept-Ranges': 'bytes', 'Transfer-Encoding': 'chunked',
 'X-GitHub-Request-Id': 'EAF6:7629:700E8:A32A6:5ED9711D'}

print(info.headers['date']) # Data de extração

print(info.headers['server']) # Servidor de origem

print(info.headers['status']) # Status HTTP da extração, 200 é ok

print(info.encoding) # Encoding do texto

print(info.headers['last-modified']) # Data da última modificação da informação