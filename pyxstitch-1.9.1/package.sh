#!/bin/bash
DIST=dist/
REPO=""
if [ ! -z "$1" ]; then
    if [[ "$1" == "pypi-test" ]]; then
        REPO="-r testpypi"
    fi
fi
if [ ! -d $DIST ]; then
    echo "no dist found..."
    exit 1
fi

file=$(ls $DIST | grep ".tar.gz$")
if [ -z "$file" ]; then
    echo "no package found"
    exit 1
fi
cnt=$(echo $file | wc -l)
if [ $cnt -ne 1 ]; then
    echo "unable to find unique package: $file"
    exit 1
fi
python3 setup.py check -s
if [ $? -ne 0 ]; then
    echo "check failed"
    exit 1
fi
python3 setup.py check -s --restructuredtext
if [ $? -ne 0 ]; then
    echo "rst check failed"
    exit 1
fi
git log -n 1 --decorate | grep -q "tag: v"
if [ $? -ne 0 ]; then
    echo "need to be on a tag to release a package"
    exit 1
fi
echo "going forward with: $DIST$file ($REPO)"
twine upload ${DIST}* $REPO
if [ $? -ne 0 ]; then
    echo "unable to upload"
    exit 1
fi
