for file in `ls instance-models/*.ttl` ; do
    dest=compiled-models/$(basename $file)
    python tools/compile.py -r -o $dest $file 223p.ttl
done
