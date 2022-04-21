from jinja2 import Environment, FileSystemLoader, select_autoescape
import glob

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)
template = env.get_template("index.html")

models = {}

# find models in 223p repo
for model_file in glob.glob("223standard/data/*.ttl"):
    model_name = model_file.split("/")[-1].split(".")[0].replace("-", " ")
    models[model_name] = model_file

# extra models
for model_file in glob.glob("instance-models/*.ttl"):
    model_name = model_file.split("/")[-1].split(".")[0].replace("-", " ")
    models[model_name] = model_file


with open("index.html", "w") as f:
    f.write(template.render(models=models))
