.PHONY: update-223pstandard compile-models all

all: 223p.ttl index.html

update-223pstandard:
	./tools/get-or-update-223p.sh
	./tools/ontoenv-init-or-refresh.sh

223p.ttl: 223standard
	python tools/compile.py -o 223p.ttl 223standard/collections/MODEL_SP223_all-v1.0.ttl

gather-files:
	./tools/gather-files.sh

compile-models:
	./tools/compile-all.sh

index.html: 223p.ttl templates/index.html tools/compile-html.py queries.toml compile-models
	python tools/compile-html.py

clean:
	rm -f compiled-models/*.ttl
	rm -f index.html
	rm -f 223p.ttl
	rm -f compiled-models/*
