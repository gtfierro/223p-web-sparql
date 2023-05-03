for file in `ls instance-models/*.ttl` ; do
    echo $file
    dest=compiled-models/$(basename $file)
    python tools/compile.py -r -i -o $dest $file 223p.ttl
done
