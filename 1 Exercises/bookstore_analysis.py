import requests
from bs4 import BeautifulSoup

def get_bookstore_data():
    base_url = "http://books.toscrape.com/"
    index_url = base_url + "index.html"
    
    # Use headers to be polite
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    response = requests.get(index_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch {index_url} (Status: {response.status_code})")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the categories container
    side_categories = soup.find('div', class_='side_categories')
    if not side_categories:
        print("Could not find categories div")
        return
    
    categories_ul = side_categories.find('ul').find('ul')
    category_links = categories_ul.find_all('a')
    
    print(f"{'Category':<30} | {'Count'}")
    print("-" * 38)

    for link in category_links:
        category_name = link.text.strip()
        # Relative link starts with 'catalogue/category/books/...'
        href = link['href']
        if not href.startswith('http'):
            category_url = base_url + href
        else:
            category_url = href
            
        cat_response = requests.get(category_url, headers=headers)
        if cat_response.status_code == 200:
            cat_soup = BeautifulSoup(cat_response.content, 'html.parser')
            # Look for the strong tag within the form indicating results count
            form = cat_soup.find('form', class_='form-horizontal')
            if form:
                count_tag = form.find('strong')
                count = count_tag.text if count_tag else "0"
                print(f"{category_name:<30} | {count}")
            else:
                # Some categories might have the count elsewhere
                res_count_tag = cat_soup.find('strong')
                count = res_count_tag.text if res_count_tag else "0"
                print(f"{category_name:<30} | {count}")
        else:
            print(f"Failed to fetch {category_url} (Status: {cat_response.status_code})")

if __name__ == "__main__":
    get_bookstore_data()
