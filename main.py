import requests
import json

def search_book(search_term):
    url = "https://openlibrary.org/search.json"
    headers = {"User-Agent": "PrivateLibrary/0.1 (github10@gibmir.net)"}
    
    params = {'title': search_term}
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        results = response.json()
        with open("books.json", "w") as f:
            json.dump(results, f, indent=2)
        if results.get('numFound', 0) > 0:
            top_match = results['docs'][0]
            
            title = top_match.get('title', 'No Title')
            authors = top_match.get('author_name', ['Unknown'])
            author = authors[0]
            
            cover_id = top_match.get('cover_i')
            
            output = f"Top Match: {title} by {author}"
            if cover_id:
                output += f"\nCover: https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
            return output
        else:
            return "No books found."
            
    except requests.exceptions.RequestException as e:
        return f"Connection error: {e}"

# 3. Actually call the function
if __name__ == "__main__":
    pass

def adding_book():
    pass

def create_list():
    # Placeholder for list creation logic
    pass

def view_list():
    # Placeholder for list viewing logic
    pass

def update_list():
    # Placeholder for list updating logic
    pass