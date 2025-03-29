from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def recipes():
    return render_template("recipes.html")

@app.route("/recipe/<recipe_name>")
def recipe_detail(recipe_name):
    templates_map = {
        "tort-straciatella": "recipe_detail/tort_straciatella.html",
        "kotleciki-jaglane": "recipe_detail/kotleciki_jaglane.html",
        "pankejksy": "recipe_detail/pankejksy.html",
        "tarta-warzywniak": "recipe_detail/tarta_warzywniak.html",
        "tofu-chinskie": "recipe_detail/tofu_chinskie.html",
        "pasta-z-pomidorami": "recipe_detail/pasta_z_pomidorami.html",
    }
    # Default to a 'not_found' page if the recipe_name isn't recognized
    template_page = templates_map.get(recipe_name, "recipe_detail/not_found.html")
    return render_template(template_page)

if __name__ == "__main__":
    app.run(debug=True)