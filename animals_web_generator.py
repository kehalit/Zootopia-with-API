import json
import requests

API_KEY = "CdYYw0zODjWdMdm9rdeXeg==GjH45xRiPvGqfrSp"
animal_name =input("Enter a name of an animal: ")
def fetch_animals():
    url = f'https://api.api-ninjas.com/v1/animals?X-Api-Key={API_KEY}&name={animal_name}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data from API")


def serialize_animal(animal_obj):
    """Serializes a single animal object into an HTML list item."""
    output = ''
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal_obj["name"]}</div>'
    output += '   <div class="card__text">\n'
    output += ' <ul class="card__details">\n'
    output += f'   <li class="card__detail-item"><strong>Diet: </strong> {animal_obj["characteristics"]["diet"]}</li>\n'
    output += f'   <li class="card__detail-item"><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n'
    if 'type' in animal_obj.get('characteristics', {}):
        output += f'<li class="card__detail-item"><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n'
    output += f'    </ul>\n'
    output += f'  </div>\n'
    output += f'</li>\n'
    return output


def generate_html(animals_data, html_template):
    """Generates HTML content by serializing animal data and replacing placeholders in the template."""
    output= ''
    for animal in animals_data:
        output += serialize_animal(animal)

    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", output)
    return html_output


def main():
    """Main function to load data, generate HTML and write it to a file."""


    animals_data = fetch_animals()
    with open("animals_template.html", "r") as file:
        html_template = file.read()

    # Generate HTML output
    html_output = generate_html(animals_data, html_template)

    # Write the generated HTML to a new file
    with open("animals.html", "w") as file:
        file.write(html_output)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()


