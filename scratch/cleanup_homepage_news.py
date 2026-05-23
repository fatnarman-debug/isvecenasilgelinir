import os
import re

def clean_homepage():
    filepath = "index.html"
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Locate the news-grid section
    grid_start_tag = '<div class="news-grid">'
    grid_start_idx = content.find(grid_start_tag)
    if grid_start_idx == -1:
        print("Error: Could not find news-grid container.")
        return

    # Find the end of the news-grid (we can look for the closing div before view-all-wrapper)
    wrapper_tag = '<div class="view-all-wrapper"'
    wrapper_idx = content.find(wrapper_tag, grid_start_idx)
    if wrapper_idx == -1:
        print("Error: Could not find view-all-wrapper.")
        return

    # Find the closing </div> of news-grid before wrapper_idx
    # Since there are multiple inner divs, let's search for the last </div> before wrapper_idx
    grid_content_end = content.rfind('</div>', grid_start_idx, wrapper_idx)
    if grid_content_end == -1:
        print("Error: Could not find end of news-grid.")
        return

    grid_section = content[grid_start_idx + len(grid_start_tag):grid_content_end]

    # Find all <article>...</article> blocks inside grid_section
    # We use a non-greedy regex to match articles
    articles = re.findall(r'(<article[^>]*>.*?</article>)', grid_section, re.DOTALL)
    print(f"Found {len(articles)} articles inside homepage news-grid.")

    if not articles:
        print("Error: No articles found.")
        return

    # Keep only the first 5 articles
    kept_articles = articles[:5]
    print(f"Keeping {len(kept_articles)} articles.")

    # Clean the first (featured) article's image style
    # We want to remove style="height: 400px; object-fit: cover;" or similar inline styles
    first_article = kept_articles[0]
    cleaned_first_article = re.sub(
        r'style="height:\s*400px;\s*object-fit:\s*cover;"',
        '',
        first_article
    )
    # Also double check in case of slightly different spacing/quotes
    cleaned_first_article = re.sub(
        r'style=\'height:\s*400px;\s*object-fit:\s*cover;\'',
        '',
        cleaned_first_article
    )
    kept_articles[0] = cleaned_first_article

    # Reconstruct the grid section
    new_grid_content = "\n" + "\n".join(kept_articles) + "\n                    "

    # Replace the old grid section with the new grid section in the main content
    new_content = (
        content[:grid_start_idx + len(grid_start_tag)] +
        new_grid_content +
        content[grid_content_end:]
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Successfully cleaned index.html homepage news section!")

if __name__ == "__main__":
    clean_homepage()
