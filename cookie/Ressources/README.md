# Cookie

We inspect page shearching for cookies
we found a cookie called I_am_admin lets decrypt the value
>the value is md5 68934a3e9455fa72420237eb05902327 =md5 decrypt> false


>lets encrypt true =md5 encrypt> b326b5062b2f0e69046810717534cb09


last step change the cookie value and refresh the page

We got Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

## Preventing cookie tampering

To avoid this vulnerability we need to avoid trivial names like I_am_admin
and also use a strong encryption
