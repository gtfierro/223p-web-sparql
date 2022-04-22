.PHONY: update-223pstandard
VPATH = instance-models:223pstandard/data
SOURCEFILES=$(wildcard 223standard/data/*.ttl)
MODELFILES=$(addprefix instance-models/,$(notdir $(SOURCEFILES)))
REASONEDFILES=$(addprefix compiled-models/,$(notdir $(MODELFILES)))

update-223pstandard:
	./tools/get-or-update-223p.sh
	./tools/ontoenv-init-or-refresh.sh

223p.ttl: 223standard
	python tools/compile.py -o 223p.ttl 223standard/collections/MODEL_SP223_all-v1.0.ttl

$(MODELFILES): $(SOURCEFILES)
	./tools/gather-files.sh

$(REASONEDFILES): $(MODELFILES) 223p.ttl
	python tools/compile.py -r -o $@ $(addprefix compiled-models/,$(notdir $@)) 223p.ttl

index.html: 223p.ttl templates/index.html tools/compile-html.py $(REASONEDFILES) $(MODELFILES) queries.toml
	python tools/compile-html.py

print-%  : ; @echo $* = $($*)

clean:
	rm -f compiled-models/*.ttl
	rm -f index.html
	rm -f 223p.ttl
	rm -f compiled-models/*
