import os
os.system(
    'git clone https://github.com/lifeInZUCC/ZUCC-intersection public --depth=1'
)
os.system('mkdocs build --clean')
if os.path.exists('public'):
    os.chdir('public')
    os.system('git add -A')
    os.system('git commit -m "update site"')
    os.system('git push origin master')
    print('update site success.')
else:
    print(
        'Failed to run, report your problem to us: https://github.com/lifeInZUCC/ZUCC-intersection/issues'
    )
