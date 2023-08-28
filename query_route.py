from atomic_queries import _query_route

if __name__ == '__main__':

    headers = {
        "Cookie": "JSESSIONID=8E9BE1C0200062BCC222B796EAFE31E9; YsbCaptcha=5F97746467E94B3182EB52C36BEBCC62",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTY5MzE5OTIxNSwiZXhwIjoxNjkzMjAyODE1fQ.BIv3mfTjJmmKL7wRikM08BSTYhtSn3AqGlAOqCnbpKk",
        "Content-Type": "application/json"
    }

    _query_route(headers=headers)
