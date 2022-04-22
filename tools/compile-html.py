from jinja2 import Environment, FileSystemLoader, select_autoescape
import base64
import glob
import toml

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())
template = env.get_template("index.html")

with open("queries.toml") as f:
    queries = toml.load(f).get("query", [])
queries_for_templates = {}
for query in queries:
    queries_for_templates[query["name"]] = base64.b64encode(query["query"].encode('ascii')).decode('ascii')


models = {}

# these lines used to load the "pre-compiled" models w/o SHACL reasoning
# # find models in 223p repo
# for model_file in glob.glob("223standard/data/*.ttl"):
#     model_name = model_file.split("/")[-1].split(".")[0].replace("-", " ")
#     models[model_name] = model_file
#
# # extra models
# for model_file in glob.glob("instance-models/*.ttl"):
#     model_name = model_file.split("/")[-1].split(".")[0].replace("-", " ")
#     models[model_name] = model_file

for model_file in glob.glob("compiled-models/*.ttl"):
    model_name = model_file.split("/")[-1].split(".")[0].replace("-", " ")
    models[model_name] = model_file


with open("index.html", "w") as f:
    f.write(template.render(models=models, queries=queries_for_templates))
