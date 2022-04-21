import argparse
import pyshacl
import ontoenv
import rdflib

env = ontoenv.OntoEnv()
graph = rdflib.Graph()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Handle imports and perform SHACL reasoning)")
    parser.add_argument('input', nargs='+')
    parser.add_argument("-o", "--output", help="Output file", required=True)
    args = parser.parse_args()

    for f in args.input:
        graph.parse(f, format=rdflib.util.guess_format(f))

    env.import_dependencies(graph, recursive_limit=2)
    # valid, _, report = pyshacl.validate(graph, advanced=True, js=True, allow_warnings=True)
    # if not valid:
    #     print(report)
    if args.output:
        graph.serialize(args.output, format='turtle')
    else:
        print(graph.serialize(format="turtle"))
