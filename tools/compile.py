import re
import string
import random
import argparse
import pyshacl
import ontoenv
import rdflib

env = ontoenv.OntoEnv()
graph = rdflib.Graph()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Handle imports and perform SHACL reasoning)"
    )
    parser.add_argument("input", nargs="+")
    parser.add_argument("-o", "--output", help="Output file", required=True)
    parser.add_argument(
        "-r", "--reason", help="Run SHACL reasoning + validation", action="store_true"
    )
    parser.add_argument(
        "-i", "--do-import", help="Perform imports", action="store_true"
    )
    args = parser.parse_args()

    for f in args.input:
        graph.parse(f, format=rdflib.util.guess_format(f))

    if args.do_import:
        env.import_dependencies(graph, recursive_limit=2)

    # remove QUDT prefix because it breaks things
    graph.bind("qudtprefix21", rdflib.Namespace("http://qudt.org/2.1/vocab/prefix/"))
    graph.bind("qudtprefix", rdflib.Namespace("http://qudt.org/vocab/prefix/"))

    if args.reason:
        valid, _, report = pyshacl.validate(
            graph, advanced=True, js=True, allow_warnings=True
        )
        valid, _, report = pyshacl.validate(
            graph, advanced=True, js=True, allow_warnings=True
        )
        if not valid:
            print(report)
    if args.output:
        graph.serialize(args.output, format="turtle")
    else:
        print(graph.serialize(format="turtle"))
