git clone https://github.com/lifeInZUCC/lifeInZUCC.github.io ../lifeInZUCC.github.io --depth=1
mkdocs build --clean
cd ../lifeInZUCC.github.io
git add *
git commit -m "update"
git push origin master
