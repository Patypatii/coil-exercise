import requests
from bs4 import BeautifulSoup
import re

def download_page_recursive(url, base_url="https://brickset.com"):
    # Using a session for persistence if needed, but simple requests here
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        page = requests.get(url, headers=headers, timeout=10)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []
        
    if page.status_code != 200:
        return []
    
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("section", {"class": "setlist minifiglist"})
    if not results:
        return []
        
    image_list = []
    articles = results.find_all("article", {"class": "set"})
    for article in articles:
        image = article.find("img", src=True)
        if image:
            image_list.append((image["src"], image["title"]))

    # Pagination lookup
    next_li = soup.find("li", {"class": "next"})
    if next_li:
        link = next_li.find("a", href=True)
        if link:
            next_url = link['href']
            # Prepend base if relative
            if not next_url.startswith('http'):
                next_url = base_url + next_url
            # Recursive call
            image_list += download_page_recursive(next_url, base_url)
        
    return image_list

def analyze_minifigs():
    main_url = "https://brickset.com/browse/minifigs"
    base_url = "https://brickset.com"
    
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(main_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch minifigs main page: {response.status_code}")
        return
        
    soup = BeautifulSoup(response.content, "html.parser")
    content_div = soup.find("div", class_="content")
    if not content_div:
        # Fallback if structure is slightly different
        content_div = soup.find("main")
        
    if not content_div:
        print("Could not find content container")
        return
        
    links = content_div.find_all("a", href=True)
    
    # Filter years (4 digits)
    year_re = re.compile(r'^\d{4}$')
    
    themes = []
    seen_hrefs = set()
    for link in links:
        name = link.text.strip()
        href = link['href']
        if not year_re.match(name) and '/minifigs/category-' in href:
            if href not in seen_hrefs:
                themes.append((name, href))
                seen_hrefs.add(href)
            
    print(f"Total themes found: {len(themes)}")
    
    # Limit to first 3 themes to be efficient
    limit = 3
    for i, (theme_name, theme_href) in enumerate(themes[:limit]):
        url = base_url + theme_href
        print(f"\nScraping Theme {i+1}/{limit}: {theme_name}...")
        minifigs = download_page_recursive(url, base_url)
        print(f"  Successfully gathered {len(minifigs)} minifigs.")
        for img_url, title in minifigs[:3]:
            print(f"    - {title} (URL: {img_url})")

if __name__ == "__main__":
    analyze_minifigs()
