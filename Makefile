.PHONY: compile-223p
VPATH = instance-models:223pstandard/data
MODELFILES=$(wildcard instance-models/*.ttl) $(wildcard 223standard/data/*.ttl)
REASONEDFILES=$(addprefix compiled-models/,$(notdir $(MODELFILES)))

compile-223p: 223standard
	./tools/get-or-update-223p.sh
	./tools/ontoenv-init-or-refresh.sh
	python tools/compile.py -o 223p.ttl 223standard/collections/MODEL_SP223_all-v1.0.ttl

$(REASONEDFILES): $(MODELFILES)
	python tools/compile.py -r -o $@ $* 223standard/collections/MODEL_SP223_all-v1.0.ttl

index.html: templates/index.html tools/compile-html.py $(REASONEDFILES) $(MODELFILES)
	python tools/compile-html.py

print-%  : ; @echo $* = $($*)
