.PHONY: compile-223p

compile-223p: 223standard
	./tools/get-or-update-223p.sh
	./tools/ontoenv-init-or-refresh.sh
	python tools/compile.py -o 223p.ttl 223standard/collections/MODEL_SP223_all-v1.0.ttl

index.html:
	python tools/compile-html.py
