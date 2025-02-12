import json
import data_fetcher


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


def generate_html(animals_data, html_template, animal_name):
    """Generates HTML content by serializing animal data and replacing placeholders in the template."""
    if not animals_data:
        error_message = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
        return html_template.replace("__REPLACE_ANIMALS_INFO__", error_message)

    animal_html = "".join(serialize_animal(animal) for animal in animals_data)
    return html_template.replace("__REPLACE_ANIMALS_INFO__", animal_html)


def main():
    """Main function to load data, generate HTML and write it to a file."""

    animal_name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_animals(animal_name)
    with open("animals_template.html", "r") as file:
        html_template = file.read()

    # Generate HTML output
    html_output = generate_html(animals_data, html_template, animal_name)

    # Write the generated HTML to a new file
    with open("animals.html", "w") as file:
        file.write(html_output)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()


