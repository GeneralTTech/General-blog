from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter(name='truncate_html')
def truncate_html(value, length=100):
 
    if not value:
        return ''
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(value, 'html.parser')
    truncated_content = ''
    total_length = 0

    # Helper function to handle truncating text inside tags without breaking HTML structure
    def truncate_element(element, current_length):
        nonlocal truncated_content, total_length
        if isinstance(element, str):
            remaining_length = length - current_length
            if current_length + len(element) > length:
                truncated_content += element[:remaining_length] + '...'
                total_length += remaining_length
                return True  # We stop processing here since we've reached the truncation length
            else:
                truncated_content += element
                total_length += len(element)
                return False
        else:
            # Add the tag (with attributes if any) to the truncated content
            truncated_content += str(element).split('>')[0] + '>'
            for child in element.children:
                if truncate_element(child, total_length):
                    truncated_content += f'</{element.name}>'
                    return True  # Stop processing once truncation limit is reached
            truncated_content += f'</{element.name}>'
            return False
    
    # Loop through all top-level elements in the soup and truncate as needed
    for element in soup.children:
        if truncate_element(element, total_length):
            break

    # Return the truncated HTML content
    return truncated_content

