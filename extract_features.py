import re
import tldextract

# 1. IP address in URL
def has_ip(url):
    return 1 if re.search(r'(\d{1,3}\.){3}\d{1,3}', url) else 0

# 2. URL length
def url_length(url):
    return len(url)

# 3. Use of @ symbol
def has_at_symbol(url):
    return 1 if '@' in url else 0

# 4. Number of subdomains
def count_subdomains(url):
    ext = tldextract.extract(url)
    return len(ext.subdomain.split('.')) if ext.subdomain else 0

# 5. Uses HTTPS
def has_https(url):
    return 1 if url.startswith("https") else 0

# 6. Double slash redirect (after protocol)
def has_redirect(url):
    return 1 if '//' in url[8:] else 0

# 7. Hyphen in domain
def has_hyphen(url):
    ext = tldextract.extract(url)
    return 1 if '-' in ext.domain else 0

# 8. Suspicious TLD (.tk, .ml, .ga, .cf, .gq)
def suspicious_tld(url):
    ext = tldextract.extract(url)
    bad_tlds = ['tk', 'ml', 'ga', 'cf', 'gq', 'biz', 'ru']
    return 1 if ext.suffix in bad_tlds else 0

# 9. Keyword trap: contains "login", "verify", "secure"
def has_keywords(url):
    keywords = ['login', 'verify', 'secure', 'update', 'free', 'account']
    return 1 if any(word in url.lower() for word in keywords) else 0

# 10. URL starts with http (not https)
def starts_with_http(url):
    return 1 if url.startswith("http://") else 0

# 11. Dot count
def dot_count(url):
    return url.count('.')

# 12. Slash count
def slash_count(url):
    return url.count('/')

# 13. URL ends with strange extension
def ends_strangely(url):
    return 1 if re.search(r'\.(exe|scr|zip|php)$', url.lower()) else 0

# 14. Port number used
def has_port(url):
    return 1 if re.search(r':\d{2,5}', url) else 0

# 15. Length of domain name
def domain_length(url):
    ext = tldextract.extract(url)
    return len(ext.domain)

# 👇 Master feature extractor
def extract_all(url):
    return [
        has_ip(url),
        url_length(url),
        has_at_symbol(url),
        count_subdomains(url),
        has_https(url),
        has_redirect(url),
        has_hyphen(url),
        suspicious_tld(url),
        has_keywords(url),
        starts_with_http(url),
        dot_count(url),
        slash_count(url),
        ends_strangely(url),
        has_port(url),
        domain_length(url)
    ]
